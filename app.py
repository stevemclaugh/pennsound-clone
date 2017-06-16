from flask import Flask, render_template, request, url_for, Markup
from pymongo import MongoClient
import os
import markdown

app = Flask(__name__)

mongo_client=MongoClient('mongo', 27017)
db=mongo_client.pennsound


def display_record(record_dict):
    print(
    record_dict['author']+' | '+ \
    record_dict['title']+' | '+ \
    record_dict['album']+' | '+ \
    record_dict['year']+' | '+ \
    '''<a href="'''+record_dict['url']+'''">link</a>'''
    )

def search_author(author_name):
    cursor = db.record.find({ 'author' :  {'$regex':'.*'+author_name+'.*'}})
    search_results=[]
    for item in cursor:
        search_results.append(display_record(item))
    return search_results



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



@app.route('/x/<page_id>.php')
def page_php(page_id):
  return page(page_id)


@app.route('/search/',methods=['POST','GET'])
def search():
  search_term=request.form['q']
  content = '\n\n'.join(search_author(search_term))
  content = Markup(markdown.markdown(content))
  return render_template('page.html', **locals())



# Run the app
if __name__ == '__main__':
    app.run(
        threaded=True,
        debug=True,
        host="0.0.0.0",
        port=int("3805")
    )
