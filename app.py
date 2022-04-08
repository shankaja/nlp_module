from project.nlp_analyzing_module import *
import flask
from flask import request
print(__name__)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/index', methods=['GET'])
def home():
    return "<h1>NLP tool by Shankaja</h1><p>This service intends to compare texts using NLP aspects.</p>"


@app.route('/word-frequncy', methods=['POST'])
def build_word_freq():
    url = request.get_json()['url']
    if url == "":
        return "Please input a valid url!"
    return buildFreqDist(url)


app.run()
