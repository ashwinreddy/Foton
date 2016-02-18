import numpy as np
from time import time
import cv2
cap = cv2.VideoCapture(0)
def procImage(im, Type):
    if Type == 'y':
        path = './examples/yes/{}.jpg'.format(str(time()))
    elif Type == 'n':
        path = './examples/no/{}.jpg'.format(str(time()))
    cv2.imwrite(path, im)


while 1:
    _, frame = cap.read()
    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('latest image',frame)
    k = cv2.waitKey(33)
    example_Type = None
    if k == ord('y'):
        procImage(grayscaled, 'y')
    elif k == ord('n'):
        procImage(grayscaled, 'n')
