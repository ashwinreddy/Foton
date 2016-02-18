import cv2
import numpy as np
import os
# X = []
# y = []
# yes, no = os.listdir('examples/yes'), os.listdir('examples/no')
# for example in yes:
#     X.append(np.resize(cv2.imread('examples/yes/' + example), (40,40)).flatten())
#     y.append(1)
#
# for example in no:
#     X.append(np.resize(cv2.imread('examples/no/' + example), (40,40)).flatten())
#     y.append(0)
#
# print "Dataset loaded"
# data = list(zip(X,y))
import random
# random.shuffle(data)
# X, y = zip(*data)
# X = np.array(X)
# y = np.array(y)
# print "Dataset shuffled"
import skflow
# classifier = skflow.TensorFlowDNNClassifier(hidden_units=[10,10,10], n_classes=2)
# classifier.fit(X,y)
# classifier.save('./mymodel/')
from sklearn import metrics
# print metrics.accuracy_score(y, classifier.predict(X))
classifier = skflow.TensorFlowEstimator.restore('./mymodel/')
cap = cv2.VideoCapture(0)
while "pigs" != "fly":
    _, frame = cap.read()
    grayscaled = np.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (40,40)).flatten()
    cv2.imshow('latest image', frame)
    print classifier.predict(np.array([grayscaled]))
