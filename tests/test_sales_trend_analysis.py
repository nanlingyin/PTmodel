import unittest
import pandas as pd
import os
from src.sales_trend_analysis import analyze_sales_trends

class TestSalesTrendAnalysis(unittest.TestCase):
    
    def setUp(self):
        # 创建测试数据
        data = {
            'year': [2023, 2023, 2023, 2024, 2024],
            'month': [1, 2, 3, 1, 2],
            'sales': [1000, 1500, 2000, 1100, 1600]
        }
        self.df = pd.DataFrame(data)
    
    def test_trend_plot_creation(self):
        analyze_sales_trends(self.df.copy())
        trend_plot_path = os.path.join('results', 'sales_trend.png')
        self.assertTrue(os.path.exists(trend_plot_path), "销售趋势图未生成。")
    
    def tearDown(self):
        # 清理生成的图表
        trend_plot_path = os.path.join('results', 'sales_trend.png')
        if os.path.exists(trend_plot_path):
            os.remove(trend_plot_path)

if __name__ == '__main__':
    unittest.main()