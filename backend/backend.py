import time
from backend.model import db, app, allowed_file, LogTilang, LogUsers
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

from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from werkzeug.security import generate_password_hash

# app = Flask(__name__)

app.secret_key = '$capsTone_pRoject_'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_capstone'

mysql = MySQL(app)


model = load_model('C:/web_capstone/assets/model_tilang/keras_model.h5')
labels = open('C:/web_capstone/assets/model_tilang/labels.txt', 'r').readlines()

klasifikasi = cv2.CascadeClassifier(
                'C:/web_capstone/assets/model_tilang/haarcascade_russian_plate_number.xml')

# @app.route('/generate_frames')
def generate_frames():
    camera = cv2.VideoCapture(0)

    while (camera.isOpened()):
        ret, img = camera.read()

        if ret == True:
            
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
            image = (image / 127.5) - 1
            probabilities = model.predict(image)
            print(labels[np.argmax(probabilities)])
            
            dafPlate = klasifikasi.detectMultiScale(img, scaleFactor=1.3, minNeighbors=2)
            for (x, y, w, h) in dafPlate:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 250, 0), 3)
                img = cv2.putText(img, probabilities, (10,450), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3,cv2.LINE_AA)
                print(probabilities)

            frame = cv2.imencode('.jpg', img)[1]
            encode = frame.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + encode + b'\r\n')
            time.sleep(0.1) 
        else:
            break

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/response')
# def respon():
#     return redne()

# Template Live
@app.route('/video_page')
def video_page():
    return render_template("tampilan/video/live.html")

# Template Video
@app.route('/video_testing')
def video_testing():
    # import cv2
    # import numpy as np
    # from keras.models import load_model

    # Load the model
    # model = load_model('assets/model_tilang/keras_model.h5')

    # # CAMERA can be 0 or 1 based on default camera of your computer.
    # camera = cv2.VideoCapture('backend/static/video/video_testing.mp4')

    # # Grab the labels from the labels.txt file. This will be used later.
    # labels = open('assets/model_tilang/labels.txt', 'r').readlines()

    # while True:
    #     # Grab the webcameras image.
    #     ret, image1 = camera.read()
    #     image1 = cv2.resize(image1, (0,0), fx=0.5, fy=0.5)
    #     image = cv2.resize(image1, (224, 224), interpolation=cv2.INTER_AREA)
    #     image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    #     image = (image / 127.5) - 1
    #     probabilities = model.predict(image)
    #     print(labels[np.argmax(probabilities)])

    return render_template("tampilan/video/video.html")
    # camera.release()
    # cv2.destroyAllWindows()

# Register
@app.route("/add_user", methods=('GET', 'POST'))
def add_user():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # tanggal = request.form['tanggal']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM log_users WHERE username = % s', (username, ))
        log_users = cursor.fetchone()
        if log_users:
            msg = 'User already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO log_users VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return redirect(url_for('users_form'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('tampilan/users/add.html', msg = msg)
    # return render_template("tampilan/register/register.html")

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM log_users WHERE username = % s AND password = % s', (username, password, ))
        log_users = cursor.fetchone()
        if log_users:
            session['loggedin'] = True
            session['id'] = log_users['id']
            session['username'] = log_users['username']
            msg = 'logged in successfully !'
            return redirect(url_for('dasbor', msg = msg))
        else:
            msg = 'Username dan Password tidak cocok!'
    return render_template('tampilan/login/login.html', msg = msg)

# Dasbor
@app.route('/dasbor', methods=['GET', 'POST'])
def dasbor():
    session.pop('loggedin', None)
    return render_template("tampilan/dasbor/dashboard.html")

# Logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

# Template Tilang
@app.route('/tilang', methods=['GET', 'POST'])
def tilang():
    if request.method == "GET":
        rv = LogTilang.query.all()
        return render_template("tampilan/tilang/data.html", tilang=rv)

# Form User
@app.route('/users_form', methods=['GET', 'POST'])
def users_form():
    if request.method == "GET":
        us = LogUsers.query.all()
        return render_template("tampilan/users/user.html", user=us)

# Add User
# @app.route('/add_user')
# def add_user():
# 	return render_template("tampilan/users/add.html")

# Delet Data Tilang
@app.route('/delete', methods=['GET', 'POST'])
def delete_tilang(no_plat):
    tilangs = db.session.execute(db.select(LogTilang).filter_by(no_plat=no_plat)).first()
    if (tilangs is None):
        return f"Data User dengan email {no_plat} tidak ditemukan!"
    else:
        tilang = tilangs[0]
        db.session.delete(tilang)
        db.session.commit()
        return render_template("tampilan/tilang/data.html")

# Template Upload
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    
	return render_template("tampilan/upload/upload.html")

# Landing Page
@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template("tampilan/landing/landing_page.html")
