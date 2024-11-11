import unittest
import pandas as pd
from src.data_preprocessing import preprocess_data
from sklearn.preprocessing import StandardScaler

class TestDataPreprocessing(unittest.TestCase):
    
    def setUp(self):
        # 创建测试数据
        data = {
            'date': ['2023-01-15', '2023-02-15', '2023-03-15', None],
            'sales': [1000, 1500, None, 2000],
            'units_sold': [50, 75, 100, None]
        }
        self.df = pd.DataFrame(data)
    
    def test_missing_values_filled(self):
        processed_df = preprocess_data(self.df.copy())
        self.assertFalse(processed_df.isnull().values.any(), "缺失值未被正确填充。")
    
    def test_date_parsing(self):
        processed_df = preprocess_data(self.df.copy())
        self.assertIn('month', processed_df.columns, "月份特征未提取。")
        self.assertIn('year', processed_df.columns, "年份特征未提取。")
        self.assertEqual(processed_df.loc[0, 'month'], 1, "月份提取错误。")
        self.assertEqual(processed_df.loc[0, 'year'], 2023, "年份提取错误。")
    
    def test_feature_standardization(self):
        processed_df = preprocess_data(self.df.copy())
        scaler = StandardScaler()
        original_features = self.df[['sales', 'units_sold']].fillna(method='ffill')
        scaler.fit(original_features)
        scaled_features = scaler.transform(original_features)
        self.assertAlmostEqual(processed_df.loc[0, 'sales'], scaled_features[0][0], places=5, msg="销售额标准化错误。")
        self.assertAlmostEqual(processed_df.loc[0, 'units_sold'], scaled_features[0][1], places=5, msg="销售量标准化错误。")

if __name__ == '__main__':
    unittest.main()