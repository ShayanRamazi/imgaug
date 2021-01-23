import imageio
import numpy as np
import imgaug as ia
from imgaug.augmentables.segmaps import SegmentationMapsOnImage
from PIL import Image
import imgaug.augmenters as iaa
import cv2
import os
import random

#read all image in folder
def load_images_from_folder(folder):
    images = []
    nameOfFile=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
            nameOfFile.append(filename)
    return images,nameOfFile

#save mask and image in des folder
def saveImage(image,mask,des):
    cells = [
        image,
        mask
    ]
    grid_image = ia.draw_grid(cells, cols=2)
    imageio.imwrite(des, grid_image)

#Agment and Save Image in Des folder
def randomImageAugment(imageFolder,maskFolder,des):
    #read image
    images,name=load_images_from_folder(imageFolder)
    masks, _ = load_images_from_folder(maskFolder)
    rand=random.randint(1,4)
    if rand==1:
        aug = iaa.Fliplr(1)
    elif rand==2:
        aug = iaa.Rot90(1)
    elif rand==3:
        aug = iaa.Cutout(fill_mode="constant", cval=255)   
    else:
        aug = iaa.Rot90(2)
    for i in range(images.__len__()):
        print(i)
        print(name[i])
        images_aug = aug(image=images[i])
        masks_aug = aug(image= masks[i])
        saveImage(images_aug,masks_aug, des + name[i])



randomImageAugment("C:/Users/shayanr/Desktop/imgaug/mamo/Whole Image","C:/Users/shayanr/Desktop/imgaug/mamo/RoI","C:/Users/shayanr/Desktop/imgaug/mamo/Des/")
