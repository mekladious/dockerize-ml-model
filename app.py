from flask import Flask, jsonify, request
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
    app.run(debug=True, port=8080)