#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Import the modules needed
from PIL import Image
import os

# Folder Path
# replace this path with the path to your folder containing the images
path = "/Users/jovan/Desktop/images/" 

# Getting list of image paths (path to each image in the folder)
image_path = os.listdir(path)
  
images = []
for x in image_path:
    images.append(path + x)

# Loop for each image
for x in images:
    # loophole to not allow .DS_Store files to pass on macOS 
    if x != '/Users/jovan/Desktop/images/.DS_Store': 
        # set the base width you want
        basewidth = 1920
        img = Image.open(x)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.LANCZOS)
        img.save(x)

print('The images have been succesfully resized.')


# In[ ]:




