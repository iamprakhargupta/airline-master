from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = pickle.load(open('rf.pkl', 'rb'))
le = pickle.load(open('le.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        ['quarter', 'month', 'dayofmonth', 'dayofweek', 'originairportseqid',
         'destairportseqid', 'iata_code_reporting_airline_code']
        print(request.form)
        month = int(request.form['Month'])
        dayofmonth=int(request.form['dayofmonth'])
        dayofweek=int(request.form['dayofweek'])

        quarter=int(request.form['quater'])
        iata_code_reporting=request.form['iata_code_reporting_airline']
        iata_code_reporting_airline_code=le.transform([iata_code_reporting])[0]
        originairportseqid = int(request.form['originairportseqid'])
        destairportseqid=int(request.form['destairportseqid'])
        prediction=model.predict_proba([[quarter, month, dayofmonth, dayofweek, originairportseqid,destairportseqid, iata_code_reporting_airline_code]])
        output=int(prediction[:,1][0]*100)
        #print(output)
        #output=output*10000
        if output<0:
            return render_template('index.html',prediction_texts="Sorry try again")
        else:
            return render_template('index.html',prediction_text="Yuur Flight Delay chances {} %".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

