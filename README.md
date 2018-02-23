# Simple Keras example on MNIST : Train, Save and Load

Simple example of scripts for training a simple neural network on mnist, save the network on disk and load it to predict on images, using Keras

## Train a Neural Network and save it to disk
The following script will train a simple neural network on the MNIST dataset and save it as a `.h5` file.

If the MNIST dataset is not on your computer, the script will download it before training.

```
>>> python train_and_save.py
```

## Load and predict on MNIST
The following script will load the previously saved model and apply predictions on the test set of the MNIST dataset.

```
>>> python load_and_predict_on_mnist.py
```

## Create test images
The following script will save all test images from MNIST as `.png` files.

```
>>> python create_test_images.py
```

## Load and predict from image on disk
The following script takes a MNIST test `.png` image path, loads the previously saved model and apply prediction on the image.

```
>>> python load_and_predict_on_png.py --path test_images/0_2378.png
```
