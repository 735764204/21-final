import scipy.io
import numpy as np
import os
from PIL import Image
import shutil

######## imagelabels ############

imagelabels_path='imagelabels.mat'
labels = scipy.io.loadmat(imagelabels_path)
labels = np.array(labels['labels'][0])-1

########  flower dataset: train test valid id ########
setid_path='setid.mat'
setid = scipy.io.loadmat(setid_path)

validation = np.array(setid['valid'][0]) - 1
np.random.shuffle(validation)

train = np.array(setid['trnid'][0]) - 1
np.random.shuffle(train)

test=np.array(setid['tstid'][0]) -1
np.random.shuffle(test)
######## flower data path  ########
flower_dir = list()

######## flower data dirs  ########
for img in os.listdir("jpg"):
    
    ######## flower data ########
    flower_dir.append(os.path.join("jpg", img))

######## flower data dirs sort ########
flower_dir.sort()

#print(flower_dir)

#####flower data train#######
des_folder_train="prepare_pic\\train"
for tid in train:
    ######## open image and get label ########
    img=Image.open(flower_dir[tid])
    #print(flower_dir[tid])
    ######## resize img #######
    img = img.resize((256, 256),Image.ANTIALIAS)
    lable=labels[tid]
    #print(lable)
    
    path=flower_dir[tid]
    #print("path:",path)
    
    base_path=os.path.basename(path)
    #print("base_path:",base_path) 
    ######
    classes="c"+str(lable)
    class_path=os.path.join(des_folder_train,classes)

    if not os.path.exists(class_path):
        os.makedirs(class_path) 
    
    #print("class_path:",class_path) 
    despath=os.path.join(class_path,base_path)
    #print("despath:",despath)
    img.save(despath)


#####flower data validation #######   
des_folder_validation="prepare_pic\\validation"

for tid in validation:
    ######## open image and get label ########
    img=Image.open(flower_dir[tid])
    #print(flower_dir[tid])
    img = img.resize((256, 256),Image.ANTIALIAS)
    lable=labels[tid]
    #print(lable)
    path=flower_dir[tid]
    print("path:",path)
    base_path=os.path.basename(path)
    print("base_path:",base_path) 
    classes="c"+str(lable)
    class_path=os.path.join(des_folder_validation,classes)
    if not os.path.exists(class_path):

        os.makedirs(class_path) 
    print("class_path:",class_path) 
    despath=os.path.join(class_path,base_path)
    print("despath:",despath)
    img.save(despath)


#####flower data test #######     
des_folder_test="prepare_pic\\test"
for tid in test:
    ######## open image and get label ########
    img=Image.open(flower_dir[tid])
    #print(flower_dir[tid])
    img = img.resize((256, 256),Image.ANTIALIAS)
    lable=labels[tid]
    #print(lable)
    path=flower_dir[tid]
    print("path:",path)
    base_path=os.path.basename(path)
    print("base_path:",base_path) 
    classes="c"+str(lable)
    class_path=os.path.join(des_folder_test,classes)
    if not os.path.exists(class_path):
        os.makedirs(class_path) 
    print("class_path:",class_path) 
    despath=os.path.join(class_path,base_path)
    print("despath:",despath)
    img.save(despath)
