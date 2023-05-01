import os
import random
import shutil

n = 2690
dataset = r'C:\Users\MGeorge\Downloads\archive\COVID-19_Radiography_Dataset'
new = r'C:\Users\MGeorge\Downloads\test2'

for path, dirs, files in os.walk(dataset):
    for dir in dirs:
        images = os.listdir(os.path.join(dataset, dir))
        for im in random.sample(images, len(images) - 2690):
            shutil.move(os.path.join(dataset, dir, im), os.path.join(new, dir, im))
