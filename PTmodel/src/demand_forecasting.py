import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def prepare_features(df):
    X = df[['month', 'year', 'units_sold']]
    y = df['sales']
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, '../models/demand_forecast_model.pkl')
    print(f"Model trained with R^2 score: {model.score(X_test, y_test):.2f}")

if __name__ == "__main__":
    df = pd.read_csv('../data/processed_sales_data.csv')
    X, y = prepare_features(df)
    train_model(X, y)