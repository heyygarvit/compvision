from tkinter import NO
import cv2
from cv2 import imwrite
from cv2 import rectangle





def swap_faces(image, detector):
    rec = detector.detectMultiScale(   
        image,
        scaleFactor = 1.3
    )

    for rectangle1,rectangle2  in zip(rec[::2],rec[1::2]):
        mask1 = get_face_selector(rectangle1)
        mask2 = get_face_selector(rectangle2)
        face1 = image[mask1]
        face2 = image[mask2]
        resized1 = resize_to_fit(face1, face2)
        resized2 = resize_to_fit(face2, face1)
        image[mask1] = apply(resized2, face1)
        image[mask2] = apply(resized1, face2)


        # x, y, w , h = rectangle
     #rectangle(image to draw on , top left corner , bottom right , color(rgb) , border line width)
        # cv2.rectangle(image , (x,y), (x+w, y+h), (0,255,0), 2)

def get_face_selector(rec):
    x, y, w , h = rec
    return (slice(y, y+h), slice(x,x+w))


def resize_to_fit(face1, face2):
    face1_h , face1_w, _ = face1.shape
    face2_h , face2_w, _ = face2.shape
    factor = min(face2_h/face1_h , face2_w/face1_w)
    return  cv2.resize(face1 , None ,fx = factor, fy= factor  )


def apply(resized1 , face2):
    resized1_h, resized1_w, _ = resized1.shape
    face2[:resized1_h, : resized1_w] = resized1
    return face2



detector = cv2.CascadeClassifier("parameters.xml")



image = cv2.imread("kids.png")
swap_faces(image, detector)







cv2=imwrite("out.jpg" , image)