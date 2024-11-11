import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sales_trends(df):
    monthly_sales = df.groupby(['year', 'month'])['sales'].sum().reset_index()
    plt.figure(figsize=(12,6))
    sns.lineplot(data=monthly_sales, x='month', y='sales', hue='year', marker='o')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.legend(title='Year')
    plt.savefig('../results/sales_trend.png')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/processed_sales_data.csv')
    analyze_sales_trends(df)