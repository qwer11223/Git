#张量区域访问
#使用slice 或 [] 索引

import tensorflow as tf

# 一维张量索引

t1 = tf.constant([1,2,3,4,5,6,7,8],tf.float32)

#取出从1位置开始，长度为3的区域
ta = tf.slice(t1,[1],[3])
tb = t1[1:4]

print(t1)
print(ta)
print(tb)

# 多维张量索引
t5 = tf.ones([2,4,28,28,3])
print(t5.shape)

print(t5[1,:,:,:,0:3].shape)
print(t5[1,...,0:3].shape)

