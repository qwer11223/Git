import tensorflow as tf

temp = tf.constant(
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

array = temp.numpy()

print(array)
