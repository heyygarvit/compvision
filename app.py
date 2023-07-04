import webopencv as wcv
import cv2

app = wcv.WebApplication()

@app.transform('Hello', default = TRUE)
def hello(image , frame):
  cv2.putText (
  image, 
  'Hello World!'
  (100, 100), 
  cv2.FONT_HERSHEY_SIMPLEX, 
  1, 
  (255, 0, 0) 
  )
  return image
  

app.run()