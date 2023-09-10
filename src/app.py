from flask import Flask, render_template, request
import pickle
import pandas as pd

app= Flask(__name__)
#load model
model =pickle.load(open(r'C:\Users\gwgse\Documents\LH2\Final\savemodel.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    fixedacidity =float(request.form['fixed acidity'])
    volatileacidity=float(request.form['volatile acidity'])
    citricacid=float(request.form['citric acid'])
    residualsugar=float(request.form['residual sugar'])
    chlorides=float(request.form['chlorides'])
    freesulfurdioxide=float(request.form['free sulfur dioxide'])
    totalsulfurdioxide=float(request.form['total sulfur dioxide'])
    density=float(request.form['density'])
    pH=float(request.form['pH'])
    sulphates=float(request.form['sulphates'])
    alcohol=float(request.form['alcohol'])

    
    data = {'fixed acidity':[fixedacidity], 'volatile acidity':[volatileacidity], 'citric acid':[citricacid], 'residual sugar':[residualsugar],
       'chlorides':[chlorides], 'free sulfur dioxide':[freesulfurdioxide], 'total sulfur dioxide':[totalsulfurdioxide], 'density':[density],
       'pH':[pH], 'sulphates':[sulphates], 'alcohol':[alcohol]}
    pred_df = pd.DataFrame(data)

    result = model.predict(pred_df)[0]
    #return render_template('index.html',**locals)
    return f'QualityPrediction:{result}'



if __name__=='__main__':
    app.run(debug=True)