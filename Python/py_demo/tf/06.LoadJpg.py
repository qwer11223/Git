import tensorflow as tf
import matplotlib.pyplot as plt

#读取图像文件
img = tf.io.read_file("./img/tf_logo.jpeg")

#将图像解码为张量
img_tensor = tf.image.decode_image(img)

print(img_tensor)
print('-------------------------------')

#将张量转换为numpy数组
img_ndarray = img_tensor.numpy()

print(img_ndarray)

plt.imshow(img_ndarray)
plt.show()