#!/usr/bin/env python

"""Import an image and show its inside border"""

import cv2

def showBorder(fileName):
	#try to load all channels including alpha
	img_orig = cv2.imread(fileName,-1);
	#to check whether it's alpha-channel enabled (4 channels)
	if(img_orig.shape[2] < 4) :
		#print debug infor out...
		print 'Not Alpha image, nothing to do!';
		return None;

	img_clone = img_orig.copy();
	img_thres = img_clone[:,:,3:]; #only alpha channel considered and reshape to shallower structure
	img_thres = img_thres.reshape(img_thres.shape[0],img_thres.shape[1]);
	cv2.imshow('threshold',img_thres);  #debug info: to show threshold image

	#cont,hier = cv2.findContours(img_thres, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1);
	#very most outsider contour
	cont,hier = cv2.findContours(img_thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
	#cont,hier = cv2.findContours(img_thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE);
	cv2.drawContours(img_orig, cont, -1, (255,255,128), thickness=2);
	cv2.imshow('final',img_orig);
	cv2.waitKey();