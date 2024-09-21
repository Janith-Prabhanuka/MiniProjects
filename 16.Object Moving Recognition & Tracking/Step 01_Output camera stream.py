#Moving Objects Detection

import  cv2
import  time
import  imutils

vs = cv2.VideoCapture(0) 

while True:
    _,img=vs.read()
    cv2.imshow("Video Stream",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
vs.release()
cv2.destroyAllWindows()



      
                
     
