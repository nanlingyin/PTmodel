import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib
import os

def plot_forecast(df, model):
    """
    使用训练好的模型进行销售预测并生成可视化图表。
    """
    last_month = df['month'].max()
    last_year = df['year'].max()
    
    # 计算下一个月和年份
    future_month = last_month + 1
    future_year = last_year
    if future_month > 12:
        future_month = 1
        future_year += 1
    
    # 创建未来数据
    future_data = pd.DataFrame({
        'month': [future_month],
        'year': [future_year],
        'units_sold': [df['units_sold'].mean()]
    })
    
    # 进行预测
    forecast = model.predict(future_data)[0]
    print(f"预测的下个月销售额: {forecast:.2f}")
    
    # 可视化预测结果
    plt.figure(figsize=(8,4))
    sns.barplot(x=['Forecast'], y=[forecast], palette='viridis')
    plt.title('Next Month Sales Forecast')
    plt.ylabel('Sales')
    plt.tight_layout()
    
    # 保存图表
    result_dir = os.path.join('results')
    os.makedirs(result_dir, exist_ok=True)
    forecast_plot_path = os.path.join(result_dir, 'sales_forecast.png')
    plt.savefig(forecast_plot_path)
    plt.show()
    print(f"销售预测图已保存到 {forecast_plot_path}")

def main():
    processed_data_path = os.path.join('data', 'processed_sales_data.csv')
    model_path = os.path.join('models', 'demand_forecast_model.pkl')
    
    # 加载处理后的数据
    df = pd.read_csv(processed_data_path)
    print("处理后的数据加载完成。")
    
    # 加载训练好的模型
    model = joblib.load(model_path)
    print("预测模型加载完成。")
    
    # 生成预测可视化
    plot_forecast(df, model)
    print("销售预测可视化完成。")

if __name__ == "__main__":
    main()