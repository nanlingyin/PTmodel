
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def prepare_features(df):
    """
    准备特征和目标变量。
    """
    X = df[['month', 'year', 'units_sold']]
    y = df['sales']
    return X, y

def train_model(X, y):
    """
    训练随机森林回归模型并保存。
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 评估模型
    r2 = model.score(X_test, y_test)
    print(f"模型训练完成，R²得分: {r2:.2f}")
    
    # 保存模型
    models_dir = os.path.join('models')
    os.makedirs(models_dir, exist_ok=True)
    model_path = os.path.join(models_dir, 'demand_forecast_model.pkl')
    joblib.dump(model, model_path)
    print(f"预测模型已保存到 {model_path}")

def main():
    processed_data_path = os.path.join('data', 'processed_sales_data.csv')
    
    # 加载处理后的数据
    df = pd.read_csv(processed_data_path)
    print("处理后的数据加载完成。")
    
    # 准备特征和目标变量
    X, y = prepare_features(df)
    print("特征和目标变量准备完成。")
    
    # 训练模型
    train_model(X, y)
    print("市场需求预测模型训练完成。")

if __name__ == "__main__":
    main()
