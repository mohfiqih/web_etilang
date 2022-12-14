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
@app.route("/api/tilang", methods=["GET"])
def getAllTilang():
    history = LogTilang.query.all()
    tilang_schema = TilangSchema(many=True)
    output = tilang_schema.dump(history)
    return jsonify({'tilang': output})

@api.route('/api/tilang')
class TilangAPI(Resource):
    def get(self):
        log_data = db.session.execute(
            db.select(LogTilang.id, LogTilang.no_plat, LogTilang.filename_plat, LogTilang.filename_pelanggaran,
                      LogTilang.pelanggaran)).all()
        if (log_data is None):
            return f"Tidak Ada Data Tilang!"
        else:
            data = []
            for history in log_data:
                data.append({
                    'id': history.id,
                    'no_plat': history.no_plat,
                    'filename_plat': history.filename_plat,
                    'filename_pelanggaran': history.filename_pelanggaran,
                    'pelanggaran': history.pelanggaran,
                })
            return data

    @api.expect(parser4Body)
    def post(self):
        args = parser4Body.parse_args()

        # Plat
        file = args['file']
        filename_plat = secure_filename(file.filename)
        file.save(os.path.join(app.config['FOLDER_TILANG'], filename_plat))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        plate = cv2.imread(
            "C:/Users/dell/PycharmProjects/web_capstone/assets/image/tilang/" + file.filename)
        plate = cv2.cvtColor(plate, cv2.COLOR_BGR2RGB)
        no_plat = pytesseract.image_to_string(plate)

        # Pelanggaran
        file_pelanggaran = args['file_pelanggaran']
        filename_pelanggaran = secure_filename(file_pelanggaran.filename)
        file.save(os.path.join(app.config['FOLDER_TILANG'], filename_pelanggaran))
        model = load_model('C:/Users/dell/PycharmProjects/web_capstone/assets/model_tilang/keras_model.h5')
        labels = open('C:/Users/dell/PycharmProjects/web_capstone/assets/model_tilang/labels.txt','r').readlines()

    # Library OpenCV
        Langgar = cv2.imread(
            "C:/Users/dell/PycharmProjects/web_capstone/assets/image/tilang/" + file.filename)
        cv2.imshow('Langgal', Langgar)
        image = cv2.resize(Langgar, (224, 224))
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1

    # library PILLOW
    #     path = 'C:/Users/dell/PycharmProjects/web_capstone/assets/image/tilang/'
        # langgar = cv2.imread(
        #     "C:/Users/dell/PycharmProjects/web_capstone/assets/image/pelanggaran/"+file_pelanggaran.filename)
        # Langgar = Image.open(langgar)
        # Langgar = Image.open(path + file_pelanggaran.filename)
        # Langgar.show()
        # image = Langgar.resize((244,244))
        # image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        pelanggaran = labels[np.argmax(model.predict(image))]
        # print (text)
# ---------------------------------------------------------------
        tanggal = datetime.now()
        tanggal_baru = tanggal.strftime('%Y-%m-%d %H:%M:%S')

        tilang = LogTilang(
            no_plat=no_plat,
            filename_plat=filename_plat,
            filename_pelanggaran=filename_pelanggaran,
            pelanggaran=pelanggaran,
            tanggal=tanggal_baru,
        )
        db.session.add(tilang)
        db.session.commit()
        return {
            'no_plat': no_plat,
            'filename_plat': filename_plat,
            'filename_pelanggaran': filename_pelanggaran,
            'pelanggaran': pelanggaran,
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