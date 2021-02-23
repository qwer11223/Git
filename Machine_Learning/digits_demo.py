import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.metrics import classification_report

digits = load_digits()
true_images = list(zip(digits.images, digits.target))

for index, (image, label) in enumerate(true_images[:4]):
    plt.subplot(2, 4, index+1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: %i' % label)

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

x_train, x_test, y_train, y_test = (
    data[:n_samples//2], data[n_samples//2:], digits.target[:n_samples//2], digits.target[n_samples//2:])

estimator = SVC(gamma=0.001)
estimator.fit(x_train, y_train)

y_pre = estimator.predict(x_test)
print('report:', classification_report(y_test, y_pre))


pre_images = list(zip(digits.images[n_samples//2:], y_pre,y_test))
for index, (image, pre,res) in enumerate(pre_images[:4]):
    plt.subplot(2, 4, index+5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('res:%i / pre: %i' % (res,pre))

plt.show()
