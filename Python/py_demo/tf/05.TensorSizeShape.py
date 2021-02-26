import tensorflow as tf

# 4维张量
t = tf.constant(
    [
        [
            [[1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4]]
        ],
        [
            [[1, 2, 3, 4], [1, 2, 3, 4]],
            [[1, 2, 3, 4], [1, 2, 3, 4]]
        ]
    ], tf.float32)
print(t)

#张量尺寸(返回的尺寸也是一个张量)
shape = tf.shape(t)

#打印尺寸张量类型
print(type(shape))

print(shape)

#转化为ndarray
infoArray = shape.numpy()

print(infoArray)

print(infoArray[-1])

#------------------------
#通过成员方法获取张量尺寸
size1 = t.get_shape()

print(type(size1))
print(size1)

infoList = size1.as_list()

print(infoList)