from flask import Flask, render_template, request
import pickle
from sklearn.ensemble import RandomForestClassifier
app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])

def predict():

    if request.method == 'POST':

        sg=request.form['sg']
        hemo=request.form['hemo']
        htn=request.form['htn']
        dm=request.form['dm']
        pcv=request.form['pcv']
        al=request.form['al']
        sc=request.form['sc']
        bgr=request.form['bgr']
       
        
        data=[[float(sg),float(hemo),float(htn),float(dm),float(pcv),float(al),float(sc),float(bgr)]]
        print(data)
        rfc=pickle.load(open('ckdproj.pickle','rb'))
        prediction_res=rfc.predict(data)[0]
        if(prediction_res==1):
            pred="YES"
        else:
            pred="No"
        
    return render_template('index.html',prediction=pred)

if __name__ =='__main__':
    app.run()