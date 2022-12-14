from backend.model import db, app, api, LogUsers, parserParamUsers, parserBodyUsers, SchemaUsers
from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.security import generate_password_hash
from datetime import datetime

@app.route("/api/create_user", methods=["GET"])
def users_db():
    with app.app_context():
        db.create_all()
        return "Database User Telah dibuat" + ' <a href="/"> Kembali</a>'


@app.route("/api/user", methods=["GET"])
def getAllUsers():
    history = LogUsers.query.all()
    users_schema = SchemaUsers(many=True)
    output = users_schema.dump(history)
    return jsonify({'users': output})


@api.route('/api/user', methods=["GET", "POST"])
class UserAPI(Resource):
    def get(self):
        log_data = db.session.execute(
            db.select(LogUsers.id, LogUsers.namalengkap, LogUsers.email, LogUsers.password)).all()
        if (log_data is None):
            return f"Tidak Ada Data User!"
        else:
            data = []
            for user in log_data:
                data.append({
                    'id': user.id,
                    # 'username': user.username,
                    'namalengkap': user.namalengkap,
                    'email': user.email,
                    'password': user.password
                    # 'tanggal': history.tanggal
                })
            return data

    @api.expect(parserBodyUsers)
    def post(self):
        d = {}
        if request.method == "POST":
            args = parserBodyUsers.parse_args()
            # username = args["username"]
            namalengkap = args["namalengkap"]
            mail = args["email"]
            password = args["password"]
            # level = args["level"]
            tanggal = datetime.now()
            tanggal_baru = tanggal.strftime('%Y-%m-%d %H:%M:%S')

            email = LogUsers.query.filter_by(email=mail).first()

            if email is None:
                register = LogUsers(namalengkap=namalengkap, email=mail, password=generate_password_hash(password),
                                    tanggal=tanggal_baru)

                db.session.add(register)
                db.session.commit()

                return jsonify(["Register success"])
            else:
                return jsonify(["Data Sudah Terdaftar"])
            # return render_template('frontend/register/register.html')

# Delete Image
@api.route('/user/<string:email>')
class UserAPI(Resource):
    def delete(self, email):
        users = db.session.execute(db.select(LogUsers).filter_by(email=email)).first()
        if (users is None):
            return f"Data User dengan Email {email} tidak ditemukan!"
        else:
            tilang = users[0]
            db.session.delete(tilang)
            db.session.commit()
            return f"Data User dengan Email {email} berhasil dihapus!"