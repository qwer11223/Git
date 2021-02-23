"""
线性回归：
波士顿房价预测
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.metrics import mean_squared_error  #均方误差
import joblib


def linear_model1():
    """
    正规方程
    sklearn.linear_model.LinearRegression()
    """
    # 1.获取数据
    boston = load_boston()

    # 2.分割数据
    x_train, x_test, y_train, y_test = train_test_split(
        boston.data, boston.target, test_size=0.2)

    # 3.特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4.机器学习-线型回归
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)

    print('模型的偏置：', estimator.intercept_)
    print('模型的系数：', estimator.coef_)

    # 5.模型评估
    # 5.1预测值
    y_pre = estimator.predict(x_test)
    print('预测值是：\n', y_pre)

    # 5.2均方误差
    ret = mean_squared_error(y_test, y_pre)
    print('均方误差：\n', ret)


def linear_model2():
    """
    梯度下降法
    sklearn.linear_model.SGDRegressor(）
    """
    # 1.获取数据
    boston = load_boston()

    # 2.分割数据
    x_train, x_test, y_train, y_test = train_test_split(
        boston.data, boston.target, test_size=0.2, random_state=2)

    # 3.特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # # 4.机器学习-线型回归
    # estimator = SGDRegressor()
    # estimator.fit(x_train, y_train)

    # joblib.dump(estimator, 'boston.pkl')  # 保存模型
    estimator = joblib.load('boston.pkl') #加载模型

    print('模型的偏置：', estimator.intercept_)
    print('模型的系数：', estimator.coef_)

    # 5.模型评估
    # 5.1预测值
    y_pre = estimator.predict(x_test)
    print('预测值是：\n', y_pre)

    # 5.2均方误差
    ret = mean_squared_error(y_test, y_pre)
    print('均方误差：\n', ret)


# linear_model1()
linear_model2()
