from flask import *

app=Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/page')
def page():
  return render_template("page.html")

@app.route('/page')
def page1():
  return render_template("page1.html")

@app.route('/page')
def page2():
  return render_template("page2.html")

@app.route('/page')
def page3():
  return render_template("page3.html")

if __name__ == '__main__':
  app.run()