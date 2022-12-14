from backend.model import db, app, api, LogUsers
from flask import request, json, jsonify

@app.route('/flutter/register', methods=["GET", "POST"])
def flutter_register():
    d={}
    if request.method =="POST":
        username = request.form["username"]
        namalengkap = request.form["namalengkap"]
        mail = request.form["email"]
        password = request.form["password"]
        tanggal = datetime.now()
        tanggal_baru = tanggal.strftime('%Y-%m-%d %H:%M:%S')

        email = LogUsers.query.filter_by(email=mail).first()

        if email is None:
            register = LogUsers(username=username, namalengkap=namalengkap, email=mail, password=generate_password_hash(password),
                                    tanggal=tanggal_baru)

            db.session.add(register)
            db.session.commit()
           
            return jsonify(["Register success"])
        else:
            # already exist
            
            return jsonify(["user alredy exist"])


@app.route('/flutter/login', methods=["GET", "POST"])
def flutter_login():
    d = {}
    if request.method == "GET":
        mail = request.form["email"]
        password = request.form["password"]

        login = LogUsers.query.filter_by(email=mail, password=password).first()

        if login is None:
            return jsonify(["Wrong Credentials"]) 
        else:
            result = login.encode('utf-8')
            return result