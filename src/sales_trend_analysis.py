import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_sales_trends(df):
    """
    分析销售趋势并生成图表。
    """
    monthly_sales = df.groupby(['year', 'month'])['sales'].sum().reset_index()
    plt.figure(figsize=(12,6))
    sns.lineplot(data=monthly_sales, x='month', y='sales', hue='year', marker='o')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.legend(title='Year')
    plt.tight_layout()
    
    # 保存图表
    result_dir = os.path.join('results')
    os.makedirs(result_dir, exist_ok=True)
    trend_plot_path = os.path.join(result_dir, 'sales_trend.png')
    plt.savefig(trend_plot_path)
    plt.show()
    print(f"销售趋势图已保存到 {trend_plot_path}")

def main():
    processed_data_path = os.path.join('data', 'processed_sales_data.csv')
    
    # 加载处理后的数据
    df = pd.read_csv(processed_data_path)
    print("处理后的数据加载完成。")
    
    # 分析销售趋势
    analyze_sales_trends(df)
    print("销售趋势分析完成。")

if __name__ == "__main__":
    main()