import cv2 #importing computer vision library
import numpy as np

a=np.zeros([10,10],dtype='uint8')
b=np.ones([10,10],dtype='uint8')*255#creating array of zeroes
print(a,b)#printing the matrix
cv2.imshow('white Wallpaper',b)
cv2.imshow('Black Wallpaper',a)#showing the image in new window
cv2.waitKey(0)#time for delay
cv2.destroyAllWindows()#closing the window


#0-black
#1-related to black
#255 white
