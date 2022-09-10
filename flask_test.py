from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd
import numpy as np

import pickle


#load in pipeline
pipeline_file = './pipeline/gb_pipeline.pkl'
model = pickle.load(open(pipeline_file,'rb'))

# app
app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def home():
    if request.method == 'POST':
        # get data and convert data into dataframe
        Gender = request.form['Gender']
    
    #define dataframe
    data_df = pd.DataFrame([['Boy','21-25','University','Non Government','Yes','Mid','Wifi','4G','3-6','Computer']],
                               columns=['Gender', 'Age', 'Education Level', 'Institution Type','IT Student',
                                        'Financial Condition', 'Internet Type','Network Type','Class Duration','Device'])
    
    # predictions
    result = model.predict(data_df)
        
    #load in the y_label_encoder
    y_enc_file = './pipeline/target_encoder.pkl'
    y_enc = pickle.load(open(y_enc_file,'rb'))
        
        
    output = y_enc.inverse_transform(result)
    
    #calculate probability
    proba = model.predict_proba(data_df)
    probs = np.round(proba.max()*100,1)
    
    return ('We predict your Adaptibility level to be: {} with a probability of {}'.format(output[0],probs))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)