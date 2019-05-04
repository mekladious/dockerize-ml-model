from flask import Flask, jsonify, request, send_file, render_template

import pickle
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

import csv
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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
        reqjson = json.loads(request.form.get("text"))
        reqDf = pd.DataFrame(reqjson, index=[0])
        reqDf.insert(loc=0, column='API', value=['1'])
        y_pred = model.predict(reqDf)
        return jsonify({"y_pred":y_pred.tolist()[0]})
    else:
        return render_template('./template.html', description=
        "{Liquid_x:MonthIdx 1 Liquid, Water_x:MonthIdx 1 Water,DaysOn_x:MonthIdx 1 DaysOn,Liquid_y:MonthIdx 2 Liquid,Water_y:MonthIdx 2 Water,DaysOn_y:MonthIdx 2 DaysOn,Liquid:MonthIdx 3 Liquid,Water:MonthIdx 3 Water,DaysOn:MonthIdx 3 DaysOn,LATERAL_LENGTH_BLEND:Well's LATERAL_LENGTH_BLEND}"
        )

@app.route("/pred_well_arr", methods=['GET', 'POST'])
def pred_well_arr():
    if request.method == 'POST':
        reqjson = json.loads(request.form.get("text"))
        reqDf = pd.DataFrame(reqjson)
        y_pred = model.predict(reqDf)
        pred_dict = dict(zip(reqDf['API'] , y_pred.tolist()))
        return jsonify({"y_pred":pred_dict})
    else:
        return render_template('./template.html', description=        
        "{API:[Well's API],\nLiquid_x:[MonthIdx 1 Liquid],\nWater_x:[MonthIdx 1 Water]\n,DaysOn_x:[MonthIdx 1 DaysOn],\nLiquid_y:[MonthIdx 2 Liquid],\nWater_y:[MonthIdx 2 Water],\nDaysOn_y:[MonthIdx 2 DaysOn],\nLiquid:[MonthIdx 3 Liquid],\nWater:[MonthIdx 3 Water],\nDaysOn:[MonthIdx 3 DaysOn],\nLATERAL_LENGTH_BLEND:[Well's LATERAL_LENGTH_BLEND]}"
        )

@app.route("/pred_well_csv", methods=['GET', 'POST'])
def pred_well_csv():
    if request.method == 'POST':
        reqDf = pd.read_csv(request.files.get("data_file"),low_memory=False)
        y_pred = model.predict(reqDf)
        pred_dict = dict(zip(reqDf['API'] , y_pred.tolist()))
        rows = zip(reqDf['API'] , y_pred.tolist())
        
        with open('predictions.csv', "w") as f:
            writer = csv.writer(f)
            writer.writerow(['Id', 'Predicted'])
            for row in rows:
                writer.writerow(row)

        return  send_file('predictions.csv')
    else:
        return render_template('./template_csv.html', description=        
        "Upload csv file with these columns:    {Liquid_x:MonthIdx 1 Liquid, Water_x:MonthIdx 1 Water,DaysOn_x:MonthIdx 1 DaysOn,Liquid_y:MonthIdx 2 Liquid,Water_y:MonthIdx 2 Water,DaysOn_y:MonthIdx 2 DaysOn,Liquid:MonthIdx 3 Liquid,Water:MonthIdx 3 Water,DaysOn:MonthIdx 3 DaysOn,LATERAL_LENGTH_BLEND:Well's LATERAL_LENGTH_BLEND}"
        )

if __name__  == "__main__":
    model = pickle.load(open("forecasting_model.pkl", "rb"))
    print(model)

    app.run(debug=True, host='0.0.0.0', port=8080)