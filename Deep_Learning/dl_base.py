import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))  # 将两个数组按垂直方向叠加
print(c)

# ---------------------------

x, y = np.mgrid[1:3:1, 2:4:0.5] #生成等差数组
grid=np.c_[x.ravel(),y.ravel()]
# np.c[] 配对数组
# x.ravel() 将x变为一维数组
print('x:',x)
print('y:',y)
print('grid:',grid)