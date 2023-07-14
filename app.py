from flask import *

app=Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/page')
def page():
  return render_template("page.html")

if __name__ == '__main__':
  app.run()