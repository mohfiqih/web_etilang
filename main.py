from backend.model import app, db, ma
from flask import Flask, render_template, request, jsonify
from backend.API import tilang, users

import nltk
nltk.download('popular')
import nltk
nltk.download('popular')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('assets/model_chatbot/chatbot_model.h5')
import json
import random

from backend import chatbot
from backend.chatbot import model, load_model,chatbot_response,getResponse,get_bot_response,clean_up_sentence,predict_class,lemmatizer
from backend.chatbot import intents, words, classes

from backend import backend
from backend.backend import login, register, dasbor, tilang, users_form, landing, chatbot, video, video_page, generate_frames
from backend.API.tilang import getAllTilang, TilangAPI
from backend.API.users import getAllUsers, UserAPI

from backend.API.loginregister_flask import flutter_register, flutter_login
from backend.API.user_tabel import UserTable, UserSchema, create_user, add_user, getAllUserTabel, getUserByid, UpdateUser, DeleteUserById

# Route API
@app.route("/api/tilang")
# @app.route("/api/register")
# @app.route("/api/login")

# Route Chatbot
@app.route("/dasbor/chatbot")
def home():
    return render_template("tampilan/chat/chatbot.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == '__main__':
    app.run(debug=True,port=5000)