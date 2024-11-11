import unittest
import pandas as pd
import os
from src.demand_forecasting import prepare_features, train_model
from sklearn.ensemble import RandomForestRegressor

class TestDemandForecasting(unittest.TestCase):
    
    def setUp(self):
        # 创建测试数据
        data = {
            'month': [1, 2, 3, 4, 5],
            'year': [2023, 2023, 2023, 2023, 2023],
            'units_sold': [50, 75, 100, 125, 150],
            'sales': [1000, 1500, 2000, 2500, 3000]
        }
        self.df = pd.DataFrame(data)
    
    def test_prepare_features(self):
        X, y = prepare_features(self.df.copy())
        self.assertEqual(X.shape[0], 5, "特征数量错误。")
        self.assertEqual(y.shape[0], 5, "目标变量数量错误。")
    
    def test_model_training(self):
        X, y = prepare_features(self.df.copy())
        train_model(X, y)
        model_path = os.path.join('models', 'demand_forecast_model.pkl')
        self.assertTrue(os.path.exists(model_path), "预测模型未保存。")
        
        # 加载模型并测试预测
        model = joblib.load(model_path)
        self.assertIsInstance(model, RandomForestRegressor, "模型类型错误。")
    
    def tearDown(self):
        # 清理生成的模型
        model_path = os.path.join('models', 'demand_forecast_model.pkl')
        if os.path.exists(model_path):
            os.remove(model_path)

if __name__ == '__main__':
    unittest.main()