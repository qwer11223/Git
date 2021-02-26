# 张量的转置
import tensorflow as tf

#构建二维张量
x = tf.constant([[1, 2, 3], [4, 5, 6]])

#转置张量
xt = tf.transpose(x,perm=[1,0])
# perm ： 
# - [1,0] : 实际转置 
# - [0,1] ：不转置

print(x)
print(xt)

#---------------------------------------------------

#构建三维张量
x = tf.constant(
    [
        [[2,5],[3,4],[8,2]],
        [[6,1],[1,2],[5,4]]
    ]
)

#绕2轴旋转转置
xt = tf.transpose(x,perm=[1,0,2])


print(x)
print(xt)