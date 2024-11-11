import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def load_data(file_path):
    """
    从CSV文件加载数据。
    """
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """
    预处理数据：处理缺失值，进行特征工程和标准化。
    """
    # 处理缺失值
    df.fillna(method='ffill', inplace=True)
    
    # 处理日期
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    
    # 特征选择
    features = ['sales', 'units_sold']
    
    # 标准化
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    
    return df

def save_processed_data(df, file_path):
    """
    将处理后的数据保存为CSV文件。
    """
    df.to_csv(file_path, index=False)

def main():
    raw_data_path = os.path.join('data', 'raw_sales_data.csv')
    processed_data_path = os.path.join('data', 'processed_sales_data.csv')
    
    # 加载数据
    raw_data = load_data(raw_data_path)
    print("原始数据加载完成。")
    
    # 预处理数据
    processed_data = preprocess_data(raw_data)
    print("数据预处理完成。")
    
    # 保存处理后的数据
    save_processed_data(processed_data, processed_data_path)
    print(f"处理后的数据已保存到 {processed_data_path}")

if __name__ == "__main__":
    main()