from keras.datasets import mnist
import os
import numpy as np
import scipy.misc

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

if not os.path.exists("test_images"):
    os.makedirs("test_images")

for i in range(len(test_images)):
    img = np.array(test_images[i]).reshape((28, 28))
    label = test_labels[i]
    scipy.misc.imsave("test_images/%s_%s.png" % (label, i), img)
