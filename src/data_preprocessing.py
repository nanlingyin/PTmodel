import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    # 处理缺失值
    df.fillna(method='ffill', inplace=True)
    
    # 特征工程
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    
    # 标准化
    scaler = StandardScaler()
    numeric_features = ['sales', 'units_sold']
    df[numeric_features] = scaler.fit_transform(df[numeric_features])
    
    return df

def save_processed_data(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    raw_data = load_data('../data/raw_sales_data.csv')
    processed_data = preprocess_data(raw_data)
    save_processed_data(processed_data, '../data/processed_sales_data.csv')