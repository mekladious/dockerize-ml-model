from flask import Flask, jsonify, request

import pickle
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
    "Single well prediction":{"route":"127.0.0.1:8080/pred_well", "method":"POST"},
    "/pred_well usage":{"route":"127.0.0.1:8080/pred_well", "method":"GET"},
    "Array of wells prediction":{"route":"127.0.0.1:8080/pred_well_arr", "method":"POST"},
    "/pred_well_arr usage":{"route":"127.0.0.1:8080/pred_well_arr", "method":"GET"},
    "CSV of wells prediction":{"route":"127.0.0.1:8080/pred_well_csv", "method":"POST"},
    "/pred_well_csv usage":{"route":"127.0.0.1:8080/pred_well_csv", "method":"GET"}
    })

@app.route("/pred_well", methods=['GET', 'POST'])
def pred_well():
    if request.method == 'POST':
        reqjson = request.get_json()
        print(reqjson)
        return jsonify({"m":"ijk"})
    else:
        return jsonify({"well":"a single comma separated value"})

@app.route("/pred_well_arr")
def pred_well_arr():
    if request.method == 'POST':
        reqjson = request.get_json()
        return jsonify({"m":"ijk"})
    else:
        return jsonify({"wells":"[]"})

@app.route("/pred_well_csv")
def pred_well_csv():
    if request.method == 'POST':
        reqjson = request.get_json()
        return jsonify({"m":"ijk"})
    else:
        return jsonify({"wells":"csv file"})

if __name__  == "__main__":
    model = pickle.load(open("forecasting_model.pkl", "rb"))
    print(model)

    app.run(debug=True, host='0.0.0.0', port=8080)