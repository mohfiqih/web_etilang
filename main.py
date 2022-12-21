from backend.model import app, db, ma
from flask import Flask, render_template, request, jsonify
from backend.API import tilang
from backend import backend
from backend.backend import login, dasbor, logout, tilang, users_form, add_user, landing, video, video_page, generate_frames, delete_tilang, video_testing
from chatbot.chat import chatbot_response, getResponse, get_bot_response, words, home, np, bow, lemmatizer, intents, classes, predict_class, WordNetLemmatizer, clean_up_sentence, model, load_model

from backend.API.users import flutter_register, flutter_login, UserAPI

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)

if __name__ == '__main__':
    app.run(debug=True,port=5000)