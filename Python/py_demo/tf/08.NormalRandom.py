# 随机数生成 -- 正态分布

import tensorflow as tf
import matplotlib.pyplot as plt
import math
import numpy as np

# mean:随机数平均值
# stddev:随机数标准差

meanSelf = 10
stddevSelf = 0.3

#-----------------------
dataT = tf.random.normal([400],mean=meanSelf,stddev=stddevSelf)

dataNd = dataT.numpy()

plt.hist(dataNd,bins=80)

plt.show()


# #截取正态分布两边
# dataT = tf.random.truncated_normal([400],mean=meanSelf,stddev=stddevSelf)

# dataNd = dataT.numpy()

# plt.hist(dataNd,bins=80)

# plt.show()