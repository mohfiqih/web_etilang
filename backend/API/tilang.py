from backend.model import db, app, api, LogTilang, TilangSchema, parser4Param, parser4Body
from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from datetime import datetime
import pytesseract
import cv2
from PIL import Image
import os
import numpy as np
from keras.models import load_model
from keras.models import Sequential

# create db tilang
@app.route("/api/create_image", methods=["GET"])
def create_db():
    with app.app_context():
        db.create_all()
        return "Database Telah dibuat" + ' <a href="/"> Kembali</a>'

# get for mobile apps
@app.route("/api/flutter", methods=["GET"])
def getAllTilang():
    history = LogTilang.query.all()
    tilang_schema = TilangSchema(many=True)
    output = tilang_schema.dump(history)
    return jsonify({'tilang': output})

@api.route('/api/tilang')
class TilangAPI(Resource):
    def get(self):
        log_data = db.session.execute(
            db.select(LogTilang.id, LogTilang.no_plat, LogTilang.filename, LogTilang.filename_pelanggaran,
                      LogTilang.pelanggaran)).all()
        if (log_data is None):
            return f"Tidak Ada Data Tilang!"
        else:
            data = []
            for history in log_data:
                data.append({
                    'id': history.id,
                    'no_plat': history.no_plat,
                    'filename': history.filename,
                    'filename_pelanggaran': history.filename_pelanggaran,
                    'pelanggaran': history.pelanggaran,
                })
            return data

    @api.expect(parser4Body)
    def post(self):
        args = parser4Body.parse_args()

        # Plat
        file = args['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['FOLDER_TILANG'], filename))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        i = 0
        model = load_model('C:/web_capstone/assets/model_tilang/keras_model.h5')
        labels = open('C:/web_capstone/assets/model_tilang/labels.txt', 'r').readlines()

        klasifikasi = cv2.CascadeClassifier(
                'C:/web_capstone/assets/model_tilang/haarcascade_russian_plate_number.xml')

        foto = cv2.imread("C:/web_capstone/assets/image/tilang/" + file.filename)

        image = cv2.resize(foto, (224, 224), interpolation=cv2.INTER_AREA)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1
        pelanggaran = labels[np.argmax(model.predict(image))]

            # plate = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
        plate = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
        dafPlate = klasifikasi.detectMultiScale(plate, scaleFactor=1.3, minNeighbors=2)
        for (x, y, w, h) in dafPlate:
            cv2.rectangle(foto, (x, y), (x + w, y + h), (0, 250, 0), 3)
            filePlate = "C:/web_capstone/assets/image/tilang/plat/Plate-" + str(i) + ".png"
            i = i + 1
            cut2 = foto[y:y + h, x:x + w]
            cv2.imwrite(filePlate, cut2)
            img = cv2.imread(filePlate)
            no_plat = pytesseract.image_to_string(img)

# ---------------------------------------------------------------
        tanggal = datetime.now()
        tanggal_baru = tanggal.strftime('%Y-%m-%d %H:%M:%S')

        tilang = LogTilang(
            filename_pelanggaran=filename,
            filename=filePlate,
            pelanggaran = pelanggaran,
            no_plat=no_plat,
            tanggal=tanggal_baru,
        )
        db.session.add(tilang)
        db.session.commit()
        return {
            'filename_pelanggaran': filename,
            'filename': filePlate,
            'no_plat':no_plat,
            'pelanggaran': pelanggaran,
            # 'no_plat': foto,
            'tanggal': tanggal_baru,
            'status': 200,
            'message': f"Data Tilang dengan Nomor Plat {no_plat} telah ditambah"
        }

# Delete
@api.route('/api/<string:no_plat>')
class TilangAPI(Resource):
    def delete(self, no_plat):
        tilangs = db.session.execute(db.select(LogTilang).filter_by(no_plat=no_plat)).first()
        if (tilangs is None):
            return f"Data Tilang dengan Nomor Plat {no_plat} tidak ditemukan!"
        else:
            tilang = tilangs[0]
            db.session.delete(tilang)
            db.session.commit()
            return f"Data Tilang dengan Nomor Plat {no_plat} berhasil dihapus!"

