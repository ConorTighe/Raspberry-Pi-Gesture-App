import argparse
import os.path
import json
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# For setting the flags for app
FLAGS = None

# Get the current directory
cwd = os.getcwd();

# Home route
@app.route("/")
def index():
    print("serving index...")
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return """<html><body>
        Something went horribly wrong
        </body></html>""", 404
    
def main(_):
    print("Running gesture based app...")
    app.run()
    