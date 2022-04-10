# -*- coding: utf-8 -*-
"""rectangles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1btYhBrOfepyapkM483EgSH_EtoWFQL_d
"""

import tensorflow as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import sklearn
import seaborn as sns
import sklearn.metrics as metrics

from tensorflow.keras import callbacks
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D,Input
from keras.utils.vis_utils import plot_model

# path_test="/content/drive/MyDrive/Colab Notebooks/test"
path_train="/content/drive/MyDrive/Colab Notebooks/test"

train_data = tf.keras.preprocessing.image_dataset_from_directory(
    path_train,
    validation_split=0.2,
    image_size=(128,128),
    batch_size=32,
    subset='training',
    seed=1000)

val_data = tf.keras.preprocessing.image_dataset_from_directory(
    path_train,
    validation_split=0.2,
    image_size=(128,128),
    batch_size=8,
    subset='validation',
    seed=1000
    )

train_data = train_data.map(lambda x, y: (tf.divide(x, 255), y))
val_data = val_data.map(lambda x, y: (tf.divide(x, 255), y))

class_name=["classic", "rotated"]

cnn=Sequential()
cnn.add(Conv2D(32,(3,3), activation='relu', input_shape=(128,128,3)))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Conv2D(16,(3,3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Conv2D(128,(3,3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Flatten())
cnn.add(Dense(128,activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(32,activation='relu'))
cnn.add(Dropout(0.3))
cnn.add(Dense(16,activation='relu'))
cnn.add(Dense(1,activation='sigmoid'))
cnn.summary()

cnn.compile(optimizer = 'adam' , loss = "poisson", metrics=["accuracy"])

early_stopping = callbacks.EarlyStopping(monitor ="val_loss", 
                                         mode ="min", patience = 5)

history = cnn.fit(train_data, validation_data = val_data, epochs = 30,callbacks = [early_stopping])

accuracy_train = history.history['accuracy']
accuracy_val = history.history['val_accuracy']
plt.grid(True)
plt.plot(accuracy_train, 'g', label='Training accuracy')
plt.plot(accuracy_val, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()



cmap=metrics.confusion_matrix(val_data,train_data)
plt.figure(figsize=(4,4),dpi=150)
hm=sns.heatmap(data=cmap,annot=True,fmt='g')
