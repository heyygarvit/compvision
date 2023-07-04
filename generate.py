import numpy as np
import cv2



#numeric represent of image

image = np.array([
    [0,0,0],
    [0,255,0],
    [0,0,0],
    [0,255,0],
    [0,0,0]
], dtype=np.uint8)  #dtype required by cv2 to successfully save image as array


#resize image


cv2.resize(image,
(90,150), 
interpolation=cv2.INTER_NEAREST) 

cv2.imwrite('8.png' , image)  #(path , image to save)
