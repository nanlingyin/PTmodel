from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# 加载模型
model_path = os.path.join('models', 'demand_forecast_model.pkl')
model = joblib.load(model_path)
print("预测模型已加载。")

@app.route('/predict', methods=['POST'])
def predict():
    """
    接收JSON数据，返回预测的销售额。
    """
    data = request.get_json()
    
    # 验证输入数据
    required_fields = ['month', 'year', 'units_sold']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    try:
        month = int(data['month'])
        year = int(data['year'])
        units_sold = float(data['units_sold'])
    except ValueError:
        return jsonify({'error': 'Invalid data types.'}), 400
    
    # 创建输入DataFrame
    input_data = pd.DataFrame({
        'month': [month],
        'year': [year],
        'units_sold': [units_sold]
    })
    
    # 进行预测
    predicted_sales = model.predict(input_data)[0]
    
    return jsonify({'predicted_sales': round(predicted_sales, 2)})

if __name__ == '__main__':
    app.run(debug=True)