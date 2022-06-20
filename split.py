import numpy as np
import os
import random

#set directories
directory = str(r'E:\images\car\images')
target_directory = str(r'E:\images\car\testing')
data_set_percent_size = float(0.07)

#print(os.listdir(directory))

# list all files in dir that are an image
files = [f for f in os.listdir(directory) if f.endswith('.png')]

#print(files)

# select a percent of the files randomly 
random_files = random.sample(files, int(len(files)*data_set_percent_size))
#random_files = np.random.choice(files, int(len(files)*data_set_percent_size))

#print(random_files)

# move the randomly selected images by renaming directory 

for random_file_name in random_files:      
    #print(directory+'/'+random_file_name)
    #print(target_directory+'/'+random_file_name)
    os.rename(directory+'/'+random_file_name, target_directory+'/'+random_file_name)
    continue

# move the relevant labels for the randomly selected images

for image_labels in random_files:
    # strip extension and add .txt to find corellating label file then rename directory. 
    os.rename(directory+'/'+(os.path.splitext(image_labels)[0]+'.xml'), target_directory+'/'+(os.path.splitext(image_labels)[0]+'.xml'))

    continue