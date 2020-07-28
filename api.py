from flask import Flask, request
from numpy import genfromtxt
from sklearn.metrics import accuracy_score


app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    y_pred = genfromtxt(request.files['file'], delimiter=',')
    y_test = genfromtxt('./data/test2.csv', delimiter=',')

    print(y_pred)

    return str(accuracy_score(y_test, y_pred))
