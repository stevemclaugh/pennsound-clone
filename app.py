from flask import Flask, render_template, request, url_for, Markup
from pymongo import MongoClient
import random
import os
import markdown

app = Flask(__name__)


@app.route('/')
def index():
  content = """
Chapter
=======

Section
-------

* Item 1
* Item 2
"""
  content = Markup(markdown.markdown(content))
  return render_template('page.html', **locals())



@app.route('/x/<page_id>.html')
def page(page_id):
  content = open('PennSound_pages/'+page_id+'.md').read().decode('utf-8')
  content = Markup(markdown.markdown(content))
  return render_template('page.html', **locals())




# Run the app
if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int("3805")
    )
