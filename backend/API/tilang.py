from backend.model import db, app, api, LogTilang, TilangSchema, parser4Param, parser4Body
from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from datetime import datetime
import pytesseract
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from keras.models import load_model
from PIL import Image, ImageOps #Install pillow instead of PIL


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
                      LogTilang.pelanggaran, LogTilang.akurasi, LogTilang.tanggal)).all()
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
                    'akurasi': history.akurasi,
                    'tanggal': history.tanggal.strftime('%Y-%m-%d %H:%M:%S')
                })
            return data

    @api.expect(parser4Body)
    def post(self):
        args = parser4Body.parse_args()

        # Plat
        file = args['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['FOLDER_TILANG'], filename))

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
        i = 0
        klasifikasi = cv2.CascadeClassifier(
                'C:/web_capstone/assets/model_tilang/indian_license_plate.xml')

        # pelanggaran
        np.set_printoptions(suppress=True)
        model = load_model('C:/web_capstone/assets/model_tilang/keras_model.h5', compile=False)
        class_names = open('C:/web_capstone/assets/model_tilang/labels.txt').readlines()
        
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
        fotopelanggaran = Image.open("C:/web_capstone/assets/image/tilang/" + file.filename).convert('RGB')

        size = (224, 224)
        image = ImageOps.fit(fotopelanggaran, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array

        prediction = model.predict(data)
        index = np.argmax(prediction)
        pelanggaran = class_names[index]
        confidence_score = prediction[0][index]
        akurasi = confidence_score * 100

        foto = cv2.imread("C:/web_capstone/assets/image/tilang/" + file.filename)
        plate = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
        # reader = easyocr.Reader(['en'])
        # result = reader.readtext(foto)
        # no_plat = result[0][1]

        # for i in range(len(result)-1):
        #     print('Nomor Plat : ', no_plat)

        # top_left = tuple(result[0][0][0])
        # bottom_right = tuple(result[0][0][2])

        # i = i + 1
        # filePlate = "image/Plate-" + str(i) + ".png"

        # img = cv2.imread(filePlate, no_plat)
        # img = cv2.rectangle(img,top_left,bottom_right,(255,0,0),3)

        dafPlate = klasifikasi.detectMultiScale(plate, scaleFactor=1.3, minNeighbors=2)
        for (x, y, w, h) in dafPlate:
            cv2.rectangle(foto, (x, y), (x + w, y + h), (0, 250, 0), 3)
        
            i = i + 1
            filePlate = "image/Plate-" + str(i) + ".png"
        
            cut2 = foto[y:y + h, x:x + w]
            cv2.imwrite(filePlate, cut2)
            img = cv2.imread(filePlate)
            no_plat = pytesseract.image_to_string(img)

            # reader = easyocr.Reader(['en'])
            # no_plat = reader.readtex(img)
    

# ---------------------------------------------------------------
        tanggal = datetime.now()
        tanggal_baru = tanggal.strftime('%Y-%m-%d %H:%M:%S')

        tilang = LogTilang(
            filename_pelanggaran = filename,
            filename = filePlate,
            pelanggaran = pelanggaran,
            no_plat = no_plat,
            akurasi = akurasi,
            tanggal = tanggal_baru,
        )
        db.session.add(tilang)
        db.session.commit()
        return {
            
            'Nomor Plat' : no_plat,
            'Pelanggaran': pelanggaran,
            # 'Akurasi Pelanggaran': round(akurasi, 2),
            '\n Tanggal': tanggal_baru,
            # 'status'     : 200,
            # 'message'    : f"Data tilang masuk dengan nomor plat : {no_plat}"
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

