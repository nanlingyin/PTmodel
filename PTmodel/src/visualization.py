import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_forecast(df, model):
    last_month = df['month'].max()
    last_year = df['year'].max()
    
    future_months = last_month + 1
    future_year = last_year
    if future_months > 12:
        future_months = 1
        future_year += 1
    
    future_data = pd.DataFrame({
        'month': [future_months],
        'year': [future_year],
        'units_sold': [df['units_sold'].mean()]
    })
    
    forecast = model.predict(future_data)
    plt.figure(figsize=(8,4))
    sns.barplot(x=['Forecast'], y=forecast)
    plt.title('Next Month Sales Forecast')
    plt.ylabel('Sales')
    plt.savefig('../results/sales_forecast.png')
    plt.show()

if __name__ == "__main__":
    import joblib
    df = pd.read_csv('../data/processed_sales_data.csv')
    model = joblib.load('../models/demand_forecast_model.pkl')
    plot_forecast(df, model)