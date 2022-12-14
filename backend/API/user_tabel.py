from backend.model import db, app, ma
from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse

# User Table Model 
class UserTable(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  namalengkap = db.Column(db.String(100))
  email = db.Column(db.String(100), unique=True)

  def __init__(self,namalengkap,email) :
    self.namalengkap=namalengkap
    self.email=email

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'namalengkap', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/create_user", methods=["GET"])
def create_user():
    with app.app_context():
        db.create_all()
        return "Database Telah dibuat" + ' <a href="/"> Kembali</a>'

# Add New User
@app.route('/user_table',methods=['POST'])
def add_user():
  namalengkap=request.json['namalengkap']
  email=request.json['email']
  new_user=UserTable(namalengkap,email)
  db.session.add(new_user)
  db.session.commit()
  return user_schema.jsonify(new_user)

# Show All User
@app.route('/user_table',methods=['GET'])
def getAllUserTabel():
  all_users=UserTable.query.all()
  result=users_schema.dump(all_users)
  return jsonify(result)

# Show User By ID
@app.route('/user_table/<id>',methods=['GET'])
def getUserByid(id):
  user=UserTable.query.get(id)
  return user_schema.jsonify(user)

# Update User By ID
@app.route('/user_table/<id>',methods=['PUT'])
def UpdateUser(id):
  user=UserTable.query.get(id)
  namalengkap=request.json['namalengkap']
  email=request.json['email']
  user.namalengkap=namalengkap
  user.email=email
  db.session.commit()
  return user_schema.jsonify(user)

# Delete User By ID
@app.route('/user_table/<id>',methods=['DELETE'])
def DeleteUserById(id):
  user=UserTable.query.get(id)
  db.session.delete(user)
  db.session.commit()
  return user_schema.jsonify(user)