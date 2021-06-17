from flask import Flask,request
import util

app= Flask(__name__)

@app.route('/get_feature_name')
def get_feature_names():
    response = {'Columns ': util.show_data_columns()}
    return response

@app.route('/predict_price',methods=['POST'])
def predict_price():
    year = float(request.form['age'])
    kms = float(request.form['kms'])
    mig = float(request.form['mig'])
    engine= float(request.form['engine'])
    power = float(request.form['power'])
    seats = float(request.form['seats'])
    fuel = request.form['fuel']
    trans = request.form['trans']
    owner = request.form['owner']
    city = request.form['city']
    name = request.form['name']

    response = {'Estimated Price':util.predict_price(year,kms,mig,engine,power,seats,fuel,trans,owner,city,name)}
    return response
    


app.run(host='localhost')
