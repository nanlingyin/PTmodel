# 零售经营数据分析与市场需求预测系统

## 项目简介
本项目旨在为零售企业提供销售趋势分析和市场需求预测的解决方案，帮助企业做出数据驱动的决策。

## 功能模块
- 数据采集与预处理
- 销售趋势分析
- 市场需求预测
- 可视化展示
- API接口

## 安装与配置

1. 克隆项目仓库：
    ```bash
    git clone https://github.com/your-repo/retail_data_analysis.git
    ```

2. 进入项目目录：
    ```bash
    cd retail_data_analysis
    ```

3. 创建并激活虚拟环境：
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

4. 安装依赖库：
    ```bash
    pip install -r requirements.txt
    ```

## 使用指南

1. **数据预处理**
    ```bash
    python src/data_preprocessing.py
    ```

2. **销售趋势分析**
    ```bash
    python src/sales_trend_analysis.py
    ```

3. **市场需求预测**
    ```bash
    python src/demand_forecasting.py
    ```

4. **生成预测可视化**
    ```bash
    python src/visualization.py
    ```

5. **启动API服务**
    ```bash
    python src/api.py
    ```

## API使用示例

发送POST请求到 `http://localhost:5000/predict`，包含JSON数据：
```json
{
  "month": 11,
  "year": 2024,
  "units_sold": 500
}
```

返回预测结果：
```json
{
  "predicted_sales": 15000.75
}
```

## 测试

在`tests/`目录下，运行各模块的测试用例：
```bash
pytest tests/
```

## 贡献

欢迎提交Issue或Pull Request，共同完善项目。

