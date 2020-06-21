import cv2
import numpy as np
b=np.ones([640,640],dtype='uint8')*255
i=80
while i<=640:
    j=80
    while j<=640:
        b[i-80:i,j:j+80]=0
        b[i:i+80,j-80:j]=0
        j=j+160
    i=i+160
cv2.imshow('Checkerboard 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
