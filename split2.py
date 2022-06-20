import numpy as np
import os
import random

#set directories
directory = str(r'E:\images\car\images')
target_directory = str(r'E:\images\car\testing')
data_set_percent_size = float(0.07)

#select any image extension
files = [f for f in os.listdir(directory) if f.endswith('.png')]


random_files = random.sample(files, int(len(files)*data_set_percent_size))
for random_file_name in random_files:      
    os.rename(directory+'/'+random_file_name, target_directory+'/'+random_file_name)
    continue

#change it to any annotation file format
for image_labels in random_files:   
    os.rename(directory+'/'+(os.path.splitext(image_labels)[0]+'.xml'), target_directory+'/'+(os.path.splitext(image_labels)[0]+'.xml'))

    continue
