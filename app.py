from flask import Flask, render_template, request, url_for
from pymongo import MongoClient
import random, os, json, datetime
from bson import json_util


app = Flask(__name__)


# Run the app
if __name__ == '__main__':
    app.run(threaded=True,
        host="0.0.0.0",
        port=int("3805")
    )
