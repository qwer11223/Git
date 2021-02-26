#通过求和降低维度

import tensorflow as tf

t1 = tf.constant([0,1,2,3],tf.float32)

print(tf.reduce_sum(t1))