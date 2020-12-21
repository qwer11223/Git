import tensorflow as tf
import numpy as np

print('创建一个[2,3,4]，元素值都为0的张量')
t1 = tf.zeros([2, 3, 4], tf.float32)
print(t1)
print('-----------------------------------')

print('创建一个[2,3,4]，元素值都为1的张量')
t2 = tf.ones([2, 3, 4], tf.float32)
print(t2)
print('-----------------------------------')

print('创建一个[2,3,4]，元素值都为5的张量')
t3 = tf.fill([2,3,4],9.0)
print(t3)
print('-----------------------------------')

print('创建一个尺寸和给定张量相同，元素值都为0的张量')
t4 = tf.ones_like(t3)
print(t4)
t5 = tf.ones(t3.shape)
print(t5)
print('-----------------------------------')