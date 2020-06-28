"""
A utility program in order to split the data into the required form to train the model.
"""

import argparse
import shutil
import os

parser = argparse.ArgumentParser(description='A utility program in order to split the data into the required form to train the model.')

parser.add_argument('location', type=str, help='The folder containing the images, the images should already be split into cats/dogs')
parser.add_argument('-N', type=int, dest='amount', help='The size of the validation data')

args = parser.parse_args()

path = os.path

os.makedirs('images/train/cats/')
os.makedirs('images/train/dogs/')
os.makedirs('images/validation/cats/')
os.makedirs('images/validation/dogs/')

images = os.listdir(args.location)

# split all of the names into two lists
cats = []
dogs = []
for image in images:
    if 'cat' in image:
        cats.append(image)
    else:
        dogs.append(image)

# cats
for i in range(0, args.amount):
    shutil.move(args.location + cats[0], os.getcwd() + '/images/validation/cats/')
    del cats[0]

# dogs
for i in range(0, args.amount):
    shutil.move(args.location + dogs[0], os.getcwd() + '/images/validation/dogs/')
    del dogs[0]

# move the rest into the appropriate dir in images/train
while len(cats) > 0:
    shutil.move(args.location + cats[0], os.getcwd() + '/images/train/cats/')
    del cats[0]

while len(dogs) > 0:
    shutil.move(args.location + dogs[0], os.getcwd() + '/images/train/dogs/')
    del dogs[0]
