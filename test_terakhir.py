
from os import getcwd

import tensorflow as tf
import tensorflow_datasets as tfds
# EXERCISE: encoding the labels using your own function for one-hot encoding

def my_one_hot(feature, label):
    # Encode the labels to one-hot using tf.one_hot with depth equal to total
    # number of classes here which are rock, paper and scissors

    one_hot = tf.one_hot(label, 3)
    return feature, one_hot


# TESTING THE FUNCTION
_, one_hot = my_one_hot(["a", "b", "c", "a"], [1, 2, 3, 1])


# EXERCISE: Loading the rock, paper and scissors train and test dataset using tfds.load.

# Use data_dir=filepath as the dataset is already downloaded for you

filePath = f"{getcwd()}/data"

train_data = tfds.load("rock_paper_scissors:3.*.*", data_dir=filePath, split='train[:100%]')
val_data = tfds.load("rock_paper_scissors:3.*.*", data_dir=filePath, split='test[:100%]')

# Testing train_data and val_data if loaded correctly

train_data_len = len(list(train_data))
val_data_len = len(list(val_data))




train_data = train_data.map(map)
val_data = val_data.map()

print(type(train_data))