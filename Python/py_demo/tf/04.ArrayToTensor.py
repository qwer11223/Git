import tensorflow as tf
import numpy as np

array = np.array([[1,2,3],[1,2,3]],np.float32)

t = tf.convert_to_tensor(array,tf.float32)

print(t)