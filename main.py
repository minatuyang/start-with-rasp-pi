# -*- coding: utf-8 -*-
from facepp_v import facepp_video
from facepp_p import facepp_picture
from hog_v import hog_video
from hog_p import hog_picture
from acc_v import acc_video

print 'please enter the model'
print '1 for ACCweight'
print '2 for HOG'
print '3 for face++ API'
model=raw_input('enter the number:')

print 'please enter the source way'
print '1 for picture'
print '2 for video'
print '3 for camera'
source=raw_input('enter the number:')

if source=='1' and model=='3':
    facepp_picture()
if source=='2' and model=='3':
    facepp_video()
if source=='3' and model=='3':
    print 'face++ with camera not ready'
    
if source=='1' and model=='2':
    hog_picture()
if source=='2' and model=='2':
    hog_video()
if source=='3' and model=='2':
    print 'not ready'

if source=='1' and model=='1':
    print 'Analysing picture with ACCweight is unnecessary'
if source=='2' and model=='1':
    acc_video()#参数需要调整
if source=='3' and model=='1':
    print 'not ready'
    
