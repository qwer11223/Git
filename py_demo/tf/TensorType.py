import tensorflow as tf

# 0维张量
t = tf.constant(3, tf.float32)
print(t)

# 1维张量
t = tf.constant([1, 2, 3, 4], tf.float32)
print(t)

# 2维张量
t = tf.constant(
    [
        [1, 2, 3, 4], [1, 2, 3, 4]
    ], tf.float32)
print(t)

# 3维张量
t = tf.constant(
    [
        [
            [1, 2, 3, 4], [1, 2, 3, 4]
        ],
        [
            [1, 2, 3, 4], [1, 2, 3, 4]
        ]
    ], tf.float32)
print(t)

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
