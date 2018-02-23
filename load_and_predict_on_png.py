import keras
from keras.datasets import mnist
from keras.models import load_model
from keras.utils import to_categorical
import numpy as np
import scipy.misc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path')
args = parser.parse_args()

img = scipy.misc.imread(args.path)
img_reshape = img.reshape((1, 28 * 28)).astype('float32') / 255

network = load_model('my_model.h5')

print "Predicted probabilities : %s" % network.predict(img_reshape)
print "Predicted class : %s" % network.predict_classes(img_reshape)[0]


