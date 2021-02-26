# 随机数生成 -- 均匀分布

import tensorflow as tf
import matplotlib.pyplot as plt

#构建一个包含40个元素的一维张量，从0 - 255 均匀随机分布
x = tf.random.uniform([40],minval=0,maxval=255)

xnd = x.numpy()

plt.hist(xnd,bins=40) # bins: 柱数 40

plt.show()
