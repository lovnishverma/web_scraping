from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


app=Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/page')
def home():
  return render_template("page.html")

if __name__ == '__main__':
  app.run()