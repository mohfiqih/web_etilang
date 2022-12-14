from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
api = Api(app, title='API E-Tilang', default='API', default_label='E-Tilang', )

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/db_capstone'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['FOLDER_TILANG'] = 'assets/image/tilang'
app.config['FOLDER_PELANGGARAN'] = "assets/image/pelanggaran"

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

db = SQLAlchemy(app)
ma = Marshmallow(app)

##################################### Database Tilang ###########################################
class LogTilang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    no_plat = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    filename_pelanggaran = db.Column(db.String(200), nullable=False)
    pelanggaran = db.Column(db.String(50), nullable=False)
    tanggal = db.Column(db.DATETIME, nullable=False)

    def __init__(self, no_plat, filename, filename_pelanggaran, pelanggaran, tanggal):
        self.no_plat = no_plat
        self.filename = filename
        self.filename_pelanggaran = filename_pelanggaran
        self.pelanggaran = pelanggaran
        self.tanggal = tanggal

class TilangSchema(ma.SQLAlchemyAutoSchema):
     class Meta:
        model = LogTilang
        load_instance = True

parser4Param = reqparse.RequestParser()
parser4Param.add_argument('filename', location='files', help='Filename Plat', type=FileStorage, required=True)
# parser4Param.add_argument('file_pelanggaran', location='files', help='Filename Pelanggaran', type=FileStorage,
#                           required=True)
parser4Body = reqparse.RequestParser()
parser4Body.add_argument('file', location='files', help='Filename Plat', type=FileStorage, required=True)
# parser4Body.add_argument('file_pelanggaran', location='files', help='Filename Pelanggaran', type=FileStorage,
#                          required=True)

################################# Database User ###########################################
class LogUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(100), nullable=False)
    namalengkap = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # level = db.Column(db.String, nullable=False)
    tanggal = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, namalengkap, email, password, tanggal):
        # self.username = username
        self.namalengkap = namalengkap
        self.email = email
        self.password = password
        # self.level = level
        self.tanggal = tanggal


class SchemaUsers(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LogUsers
        load_instance = True

parserParamUsers = reqparse.RequestParser()
# parserParamUsers.add_argument('username', type=str, help='Masukan Username', location='args')
parserParamUsers.add_argument('namalengkap', type=str, help='Masukan Nama', location='args')
parserParamUsers.add_argument('email', type=str, help='Masukan Email', location='args')
parserParamUsers.add_argument('password', type=str, help='Masukan Password', location='args')
# parserParamUsers.add_argument('level', type=str, help='Masukan Level', location='args')

parserBodyUsers = reqparse.RequestParser()
# parserBodyUsers.add_argument('username', type=str, help='Masukan Username', location='args')
parserBodyUsers.add_argument('namalengkap', type=str, help='Masukan Nama', location='args')
parserBodyUsers.add_argument('email', type=str, help='Masukan Email', location='args')
parserBodyUsers.add_argument('password', type=str, help='Masukan Password', location='args')
# parserBodyUsers.add_argument('level', type=str, help='Masukan Level', location='args')