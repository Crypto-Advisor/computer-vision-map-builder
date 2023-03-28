import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

##############################################
############# 1. Load the data ###############
##############################################

# read the image dataset
data = tf.keras.utils.image_dataset_from_directory('data')
# create a data iterator
data_iterator = data.as_numpy_iterator()
# get the next batch
batch = data_iterator.next()


##############################################
########## 2. Determine class index ##########
##############################################

#1 == blocked 
#0 == free
# check which class is blocked / free
# fig, ax = plt.subplots(ncols=4, figsize=(20,20))
# for idx, image in enumerate(batch[0][:4]):
#     ax[idx].imshow((image * 255).astype(np.uint8))
#     ax[idx].set_title(batch[1][idx])
    
# plt.savefig('images.png')


##############################################
############# 3. Preprocess data #############
##############################################

