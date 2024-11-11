from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('../models/demand_forecast_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    month = data.get('month')
    year = data.get('year')
    units_sold = data.get('units_sold')
    
    input_data = pd.DataFrame({
        'month': [month],
        'year': [year],
        'units_sold': [units_sold]
    })
    
    prediction = model.predict(input_data)[0]
    return jsonify({'predicted_sales': prediction})

if __name__ == '__main__':
    app.run(debug=True)