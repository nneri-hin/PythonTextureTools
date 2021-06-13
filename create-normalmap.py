#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from sys import argv  as a
import datetime
import locale   
import numpy as np
import cv2



def NormalMap(temp,param):
    (w,h) = temp.shape
    print(np.average(temp))
    temp_r =  np.zeros((w,h),dtype=np.float)
    temp_g =  np.zeros((w,h),dtype=np.float)
    temp_b =  np.zeros((w,h),dtype=np.float)
    #temp_r[0:w-1,0:h  ] =  temp[1:w,0:h] / 255.0
    #temp_r[w-1  ,0:h  ] =  temp[0  ,0:h] / 255.0
    #temp_g[0:w  ,0:h-1] =  temp[0:w,1:h] / 255.0
    #temp_g[0:w  ,  h-1] =  temp[0:w,0  ] / 255.0
    #temp_b[:,:] = temp[:,:]  / 255.0
    temp_r[:,:] = np.roll(temp,-1,axis=1) / 255.0
    temp_g[:,:] = np.roll(temp,1,axis=0) / 255.0
    temp_b[:,:] = temp[:,:] / 255.0
    r = temp_b  - temp_r
    g = temp_b  - temp_g
    b = np.ones((w,h),dtype=np.float) * param
    x = np.abs(r) + np.abs(g) + np.abs(b )
    result = np.zeros((w,h,3),dtype=np.float)
    result[:,:,2] = r / x 
    result[:,:,1] = g / x
    result[:,:,0] = b / x
    result2 = np.array(result * 127.5 + 127.5,dtype=np.uint8)
    return result2

if __name__ == '__main__':
    org = cv2.imread(a[1],cv2.IMREAD_UNCHANGED)
    print(org.shape)
    gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
    #normal = NormalMap(org[:,:,0],0.1)
    normal = NormalMap(gray,0.2)
    cv2.imwrite(a[2],normal)

