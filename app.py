from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC by kleoz (https://yeswehack.com/hunters/kleoz)"
