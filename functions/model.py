
import os
import numpy as np
import glob
import json
import importlib
import csv
import operator
import pandas as pd

from tensorflow import keras
from keras import backend as K
from keras.models import Model
from keras.layers import Dropout, Dense
from keras.optimizers import Adam

def earth_movers_distance(y_true, y_pred):
    cdf_true = K.cumsum(y_true, axis=-1)
    cdf_pred = K.cumsum(y_pred, axis=-1)
    emd = K.sqrt(K.mean(K.square(cdf_true - cdf_pred), axis=-1))
    return K.mean(emd)

##################################################################

class MyModel:
    def __init__(self, base_model_name, n_classes=10, learning_rate=0.001, dropout_rate=0, loss=earth_movers_distance,
                 decay=0, weights='imagenet'):
        self.n_classes = n_classes
        self.base_model_name = base_model_name
        self.learning_rate = learning_rate
        self.dropout_rate = dropout_rate
        self.loss = loss
        self.decay = decay
        self.weights = weights
        self._get_base_module()

    def _get_base_module(self):
        # import Keras base model module
        if self.base_model_name == 'InceptionV3':
            self.base_module = importlib.import_module('keras.applications.inception_v3')
        elif self.base_model_name == 'InceptionResNetV2':
            self.base_module = importlib.import_module('keras.applications.inception_resnet_v2')
        else:
            self.base_module = importlib.import_module('keras.applications.'+self.base_model_name.lower())

    def build(self):
        # get base model class
        BaseCnn = getattr(self.base_module, self.base_model_name)

        # load pre-trained model
        self.base_model = BaseCnn(input_shape=(224, 224, 3), weights=self.weights, include_top=False, pooling='avg')

        # add dropout and dense layer
        x = Dropout(self.dropout_rate)(self.base_model.output)
        x = Dense(units=self.n_classes, activation='softmax')(x)

        self.my_model = Model(self.base_model.inputs, x)

    def compile(self):
        self.my_model.compile(optimizer=Adam(lr=self.learning_rate, decay=self.decay), loss=self.loss)

    def preprocessing_function(self):
        return self.base_module.preprocess_input


#################################################################

def load_image(img_file, target_size):
    x = np.asarray(keras.preprocessing.image.load_img(img_file, target_size=target_size))
    x = np.expand_dims(x, axis=0)
    return x

def normalize_labels(labels):
    labels_np = np.array(labels)
    return labels_np / labels_np.sum()

def calc_mean_score(score_dist):
    score_dist = normalize_labels(score_dist)
    return (score_dist*np.arange(1, 11)).sum()

def predict(model, image):
    return model.predict(image)