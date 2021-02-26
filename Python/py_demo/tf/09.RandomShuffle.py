import tensorflow as tf

print('生成0-9的偶数序列作为张量的元素')
seq = tf.range(0, 10, delta=2, dtype=tf.int32)
print(seq)
print('随机打乱')
seqShuffle = tf.random.shuffle(seq)
print(seqShuffle)

a = tf.reshape(tf.range(1, 101, delta=1, dtype=tf.int32), [10, 10])
print(a)

#获取序列
ag = tf.gather(a,indices=[1,2,3,8],axis=0)
print(ag)

#多维度联合自由点选元素
bg = tf.gather_nd(a,indices=[[0],[2]])
print(bg)

#通过掩码获取元素
bg = tf.boolean_mask(a,mask=[1,0,1,0,1,1,1,1,1,1])
print(bg)