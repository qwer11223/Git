import tensorflow as tf

x = tf.constant(
    [
        [[2,5],[3,4],[8,2]],
        [[6,1],[1,2],[5,4]]
    ]
)

t = tf.reshape(x,[4,1,-1]) #-1代表最后一个维度自动计算
tt = tf.reshape(x,[4,-1])

print(t)
print(tt)

#除了reshape还可用expand_dims增加维度
ttt = tf.expand_dims(x,axis=1)
print(ttt)

#除了reshape还可用squeeze减少维度
sq = tf.ones([1,2,3,1,4])
print(sq.shape)
print(tf.squeeze(sq,axis=3).shape)