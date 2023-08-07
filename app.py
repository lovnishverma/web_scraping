from flask import *
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html", now=datetime.now())

@app.route('/page')
def page():
  return render_template("page.html")

@app.route('/page1')
def page1():
  return render_template("page1.html")

@app.route('/page2')
def page2():
  return render_template("page2.html")

@app.route('/page3')
def page3():
  return render_template("page3.html")

if __name__ == '__main__':
  app.run()