from sklearn.neighbors import KNeighborsClassifier

# 1. 构造数据
x = [[1],[2],[10],[20]]
y = [0,0,1,1]

# 2. 训练模型
estimator = KNeighborsClassifier(n_neighbors=1)

estimator.fit(x,y)

# 3. 数据预测
print(estimator.predict([[100]]))