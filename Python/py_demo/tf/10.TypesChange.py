#张量类型转换

import tensorflow as tf

#构建一个数值型二维张量
t = tf.constant([[0,2,0],[0,0,1]],tf.float32)

#将数值型张量抓换为布尔型张量
b = tf.cast(t,tf.bool)
tt = tf.cast(b,tf.float32)

print(t)
print(b)
print(tt)