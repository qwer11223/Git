from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1.获取数据
iris = load_iris()

# 2.数据基本处理
# 划分 训练集、测试集
# x: 特征值  y: 目标值
x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=2)  #分割数据集

# 3.特征工程 - 特征预处理
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)   #标准化数据
x_test = transfer.transform(x_test)

# 4.机器学习 - KNN
## 4.1实例化一个估计器
estimator = KNeighborsClassifier()

## 4.2 模型调优 -- 交叉验证，模型调优
param_grid = {'n_neighbors': [1, 3, 5, 7]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5)
# estimator 选择训练模型
# param_grid 需要传递的超参数
# cv 几折交叉验证

## 4.3 模型训练
estimator.fit(x_train, y_train)

# 5.模型评估
## 5.1 预测结果输出
y_pre = estimator.predict(x_test)
print('预测值为：\n', y_pre)
print('预测值与真实值对比：\n', y_pre == y_test)

## 5.2 准确率计算
score = estimator.score(x_test, y_test)
print('准确率为：\n', score)

## 5.3 查看交叉验证，网格搜索的一些属性
print('在交叉验证中,得到最好结果：\n',estimator.best_score_)
print('在交叉验证中,得到最好模型：\n',estimator.best_estimator_)
print('在交叉验证中,得到模型结果是：\n',estimator.cv_results_)