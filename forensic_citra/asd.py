from numpy import genfromtxt
import matplotlib
from matplotlib import pyplot
from matplotlib.image import imread

my_data = genfromtxt('chall.txt', delimiter=',')
matplotlib.image.imsave('out.png', my_data)
image_1 = imread('out.png')
# plot raw pixel data
pyplot.imshow(image_1)
# show image
pyplot.show()