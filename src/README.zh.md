## 虚拟货币价格预测
[English](./README.md) | 简体中文
### 项目简介
本项目是一个基于深度学习的虚拟货币价格预测项目，通过爬取公开数据信息，获得了关于比特币的市场，新闻，美国互联网巨头公司的股票及市值，在数据清洗（异常值剔除，缺失值填补）后，采用了多个预测模型对比特币价格进行预测，最终得到了较为准确的预测结果。
### 项目数据来源
- 比特币价格数据：[https://www.coindesk.com/price/bitcoin](https://www.coindesk.com/price/bitcoin)
- 比特币新闻数据：[https://www.coindesk.com/news](https://www.coindesk.com/news)
- 市场情绪数据：[FearGreedIndex](https://api.alternative.me/fng/?limit=2000&date_format=us)

- 美国互联网巨头公司的股票及市值：[https://finance.yahoo.com/quote/GOOG/history?p=GOOG](https://finance.yahoo.com/quote/GOOG/history?p=GOOG)
- okx交易平台数据 ：[https://www.okex.com/](https://www.okex.com/)
### 项目结构
项目分为数据获取以及模型预测两部分
- 数据获取
    位于[`datasets`](./datasets/dataGain.py)文件夹下
    - 数据爬取
    - 数据清洗
    - 保存数据
        - [BTC价格及市场数据](./datasets/demodata.csv)
- 模型预测
    位于`simplemodel`文件夹下
    - 通过关联分析，提取数据集中的有效信息，再利用MLP 线性模型进行预测[代码](mlp.ipynb) 
    ![res](images/image.png)
    - 采用卷积神经网络利用市场，新闻情绪等数据进行预测([代码](longtermprediction.ipynb))
    ![resConv](images/image2.png)
### TODO
- [x] 数据爬取
- [x] 数据清洗
- [x] LSTM对纯历史价格进行预测
- [x] 通过关联分析，提取数据集中的有效信息，再利用MLP 线性模型进行预测
- [x] 采用卷积神经网络利用市场，新闻情绪等数据进行预测
- [ ] 采用LSTM对市场，新闻情绪等数据进行预测
- [ ] 高频数据预测
- [ ] 交易策略，以回报率为指标


阐述解决的任务，任务的挑战，问题的难点，遇到的问题以及技术路线和解决方案（实现细节）。
