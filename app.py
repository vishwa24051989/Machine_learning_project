
from crypt import methods
from pickle import GET
from flask import Flask
import flask
from flask.helpers import flash

app=Flask(__name__)

@app.route("/",methods['GET','POST']
def index():
    return "starting machine learning project"

if __name__=="__main__":
    app.run(debug=True)
