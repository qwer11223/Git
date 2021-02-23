import psutil
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

print('read data...')
data = pd.read_csv(
    'C:/Users/Administrator/Desktop/ml_data/day05资料/2.code/data/FBlocation/train.csv')

print('split data...')
partial_data = data.query('x>2.0 & x<2.5 & y>2.0 & y<2.5')

time = pd.DatetimeIndex(pd.to_datetime(partial_data.time, unit='s'))

partial_data['day'] = time.day
partial_data['hour'] = time.hour
partial_data['weekday'] = time.weekday

place_count = partial_data.groupby('place_id').count()
place_count = place_count[place_count['row_id'] > 3]

partial_data = partial_data[partial_data['place_id'].isin(place_count.index)]

x = partial_data[["x", "y", "accuracy", "day", "hour", "weekday"]]  # 特征值
y = partial_data['place_id']  # 目标值

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=2)

print('train model...')
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

cpu_count = psutil.cpu_count()
print('cpu_count: ',cpu_count,'\n')

estimator = GridSearchCV(KNeighborsClassifier(), param_grid={
                         'n_neighbors': [3, 5, 7, 9]}, cv=5, n_jobs=cpu_count-1)
estimator.fit(x_train, y_train)

score = estimator.score(x_test, y_test)
print("预测的准确率为:\n", score)

y_predict = estimator.predict(x_test)
print("预测值为:\n", y_predict)
print("预测值和真实值的对比情况:\n", y_predict == y_test)

print("在交叉验证中验证的最好结果:\n", estimator.best_score_)
print("最好的参数模型:\n", estimator.best_estimator_)
print("每次交叉验证后的验证集准确率结果和训练集准确率结果:\n", estimator.cv_results_)

input()
