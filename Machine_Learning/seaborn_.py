import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
# print(iris)

#把数据转化为dataframe格式

iris_d = pd.DataFrame(iris.data,columns=iris.feature_names)
iris_d["target"] = iris.target
# print(iris_d)


def iris_plot(data,col1,col2):
    sns.lmplot(x=col1,y=col2,data=data,hue='target',fit_reg=0)
    plt.show()

iris_plot(iris_d,'sepal width (cm)','petal length (cm)')