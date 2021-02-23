import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report

# 1.获取数据
names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
         'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
         'Normal Nucleoli', 'Mitoses', 'Class']

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
                   names=names)

data = data.replace(to_replace='?', value=np.NaN).dropna()

# 2. 确定特征值,目标值
x = data.iloc[:, 1:-1]
y = data["Class"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=2, train_size=0.2)

# 3.特征工程(标准化)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4.机器学习(逻辑回归)
estimator = LogisticRegression()
estimator.fit(x_train, y_train)

# 5.模型评估
y_pre = estimator.predict(x_test)
print('准确率:\n',estimator.score(x_test, y_test))

print('分类评估报告:\n')
print(classification_report(y_test, y_pre,
                            labels=(2, 4), target_names=('良性', '恶性')))

print('AUC指标:\n')
y_test = np.where(y_test > 3, 1, 0)
print(roc_auc_score(y_test,y_pre))
