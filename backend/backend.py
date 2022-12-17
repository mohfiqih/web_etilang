import time

from backend.model import db, app, api, LogUsers, LogTilang, allowed_file
from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session, Response
from werkzeug.security import generate_password_hash
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import pytesseract
import cv2
import os
import numpy as np
from keras.models import load_model


def generate_frames():
    camera = cv2.VideoCapture(0)

    while (camera.isOpened()):
        ret, img = camera.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.1)
        else:
            break
        ## read the camera frame
        # success,frame=camera.read()
        # if not success:
        #     break
        # else:
        #     ret,buffer=cv2.imencode('.jpg',frame)
        #     frame=buffer.tobytes()
        #
        # yield(b'--frame\r\n'
        #            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_page')
def video_page():
    return render_template("tampilan/video/video.html")

# Register
@app.route("/register", methods=('GET', 'POST'))
def register():
    d = {}
    if request.method == "POST":
        # args = parserBodyUsers.parse_args()
        username = request.form["username"]
        namalengkap = request.form["namalengkap"]
        mail = request.form["email"]
        password = request.form["password"]
        # level = request.form["level"]
        # generate_password_hash(password)

        tanggal = datetime.now()
        tanggal_baru = tanggal.strftime('%Y-%m-%d %H:%M:%S')

        email = LogUsers.query.filter_by(email=mail).first()

        if email is None:
            register = LogUsers(
                username=username,
                namalengkap=namalengkap,
                email=mail,
                password=generate_password_hash(password),
                # level=level,
                tanggal=tanggal_baru
            )

            db.session.add(register)
            db.session.commit()

            return redirect("dasbor")
        else:
            return redirect(url_for("dasbor"))
    return render_template("tampilan/register/register.html")

def users():
    if request.method == "GET":
        user = LogTilang.query.all()
        return render_template("tampilan/tilang/data.html", us = user)


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    d = {}
    if request.method == "POST":
        mail = request.form["email"]
        password = request.form["password"]

        login = LogUsers.query.filter_by(email=mail, password=password).first()

        if login is None:
            # acount not found

            return redirect("dasbor")
        else:
            # acount found
            return redirect("register")
    return render_template("tampilan/login/login.html")
    # if request.method == 'POST':
    #     mail = request.form["email"]
    #     password = request.form["password"].encode('utf-8')
    #
    #     data = LogUsers.query.filter_by(email=mail).first()
    #
    #     if data is not None and len(data) > 0:
    #         if not check_password_hash(data[4], password):
    #             session['loggedin'] = True
    #             session['email'] = data[3]
    #             session['level'] = data[5]
    #             #   return 'Berhasil'
    #             return redirect("app.dasbor")
    #         else:
    #             #   flash("Gagal, Email dan Password Tidak Cocok")
    #             return render_template('frontend/login/login.html')
    #         # return 'Password tidak cocok'
    #     else:
    #         #  flash("Gagal, User tidak ditemukan")
    #         return render_template('frontend/login/login.html')
    #     # return 'User tidak ditemukan'
    # else:
    #     return render_template('frontend/login/login.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.get(form.email.data)
#         if user:
#             if bcrypt.check_password_hash(user.password, form.password.data):
#                 user.authenticated = True
#                 db.session.add(user)
#                 db.session.commit()
#                 login_user(user, remember=True)
#                 return redirect(url_for("app.dasbor"))
#     return render_template("frontend/login/login.html", form=form)

# Dasbor
@app.route('/dasbor', methods=['GET', 'POST'])
def dasbor():
    return render_template("tampilan/dasbor/dashboard.html")

@app.route('/tilang', methods=['GET', 'POST'])
def tilang():
    if request.method == "GET":
        rv = LogTilang.query.all()
        return render_template("tampilan/tilang/data.html", tilang=rv)

@app.route('/users_form', methods=['GET', 'POST'])
def users_form():
    if request.method == "GET":
        us = LogUsers.query.all()
        return render_template("tampilan/users/user.html", user=us)

@app.route('/tilang/delete', methods=['GET', 'POST'])
def delete_tilang(no_plat):
    tilangs = db.session.execute(db.select(LogTilang).filter_by(no_plat=no_plat)).first()
    if (tilangs is None):
        return f"Data User dengan email {no_plat} tidak ditemukan!"
    else:
        tilang = tilangs[0]
        db.session.delete(tilang)
        db.session.commit()
        return render_template("tampilan/tilang/data.html")

@app.route('/upload')
def upload():
	return render_template("tampilan/upload/upload.html")

# @app.route('/python-flask-files-upload', methods=['POST'])
# def upload_file():
# 	# check if the post request has the file part
# 	if 'files[]' not in request.files:
# 		resp = jsonify({'message' : 'No file part in the request'})
# 		resp.status_code = 400
# 		return resp
	
# 	files = request.files.getlist('files[]')
	
# 	errors = {}
# 	success = False
	
# 	for file in files:
# 		if file and allowed_file(file.filename):
# 			filename = secure_filename(file.filename)
# 			file.save(os.path.join(app.config['FOLDER_TILANG'], filename))
            
# 			success = True
# 		else:
# 			errors[file.filename] = 'File type is not allowed'
	
# 	if success and errors:
# 		errors['message'] = 'File(s) successfully uploaded'
# 		resp = jsonify(errors)
# 		resp.status_code = 206
# 		return resp
# 	if success:
# 		resp = jsonify({'message' : 'Files successfully uploaded'})
# 		resp.status_code = 201
# 		return resp
# 	else:
# 		resp = jsonify(errors)
# 		resp.status_code = 400
# 		return resp

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == "POST":
#         # no_plat = request.form['no_plat']
#         file = request.form['filename']
#         # filename_pelanggaran = request.form['filename_pelanggaran']
#         # pelanggaran = request.form['pelanggaran']
        
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['FOLDER_TILANG'], filename))
#         pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#         i = 0
#         model = load_model('C:/web_capstone/assets/model_tilang/keras_model.h5')
#         labels = open('C:/web_capstone/assets/model_tilang/labels.txt', 'r').readlines()

#         klasifikasi = cv2.CascadeClassifier(
#                 'C:/web_capstone/assets/model_tilang/haarcascade_russian_plate_number.xml')

#         foto = cv2.imread("C:/web_capstone/assets/image/tilang/" + file.filename)

#         image = cv2.resize(foto, (224, 224), interpolation=cv2.INTER_AREA)
#         image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
#         image = (image / 127.5) - 1
#         pelanggaran = labels[np.argmax(model.predict(image))]

#         plate = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
#         dafPlate = klasifikasi.detectMultiScale(plate, scaleFactor=1.3, minNeighbors=2)
#         for (x, y, w, h) in dafPlate:
#             cv2.rectangle(foto, (x, y), (x + w, y + h), (0, 250, 0), 3)
#             filePlate = "C:/web_capstone/assets/image/tilang/plat/Plate-" + str(i) + ".png"
#             i = i + 1
#             cut2 = foto[y:y + h, x:x + w]
#             cv2.imwrite(filePlate, cut2)
#             img = cv2.imread(filePlate)
#             no_plat = pytesseract.image_to_string(img)

#         tanggal = datetime.now()
#         tanggal_baru = tanggal.strftime('%Y-%m-%d %H:%M:%S')

#         tilang = LogTilang(
#             filename_pelanggaran=filename,
#             filename=filePlate,
#             pelanggaran = pelanggaran,
#             no_plat=no_plat,
#             tanggal=tanggal_baru,
#         )
#         db.session.add(tilang)
#         db.session.commit()
#     return render_template("tampilan/upload/upload.html")

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'files[]' not in request.files:
#         resp = jsonify({'message': 'No file part in request'})
#         resp.status_code == 400
#         return resp

#     files = request.files.getlist('files[]')

    # errors = {}
    # success = False

    # for file in files:
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['FOLDER_TILANG'], filename))
    #         success = True
    #     else:
    #         errors[file.filename] = 'File type is not allowed'
        
    # if success and errors:
    #     errors['message'] = 'File(s) successfully uploaded'
    #     resp = jsonify(errors)
    #     resp.status_code = 206
    #     return resp

    # if success:
    #     resp = jsonify({'message' : 'Files succesfully uploaded'})
    #     resp.status_code = 201
    #     return resp
    # else:
    #     resp = jsonify(errors)
    #     resp.status_code = 400
    #     return resp




@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template("tampilan/landing/landing_page.html")

# @app.route('/landing/chatbot', methods=['GET', 'POST'])
# def chatbot():
#     return render_template("tampilan/chat/chatbot2.html")