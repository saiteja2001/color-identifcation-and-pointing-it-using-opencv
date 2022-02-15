import cv2
import numpy as np
lower = np.array([25, 114, 121])
upper=np.array([71, 255, 210])
cam = cv2.VideoCapture("video_3.mp4")
output = cv2.VideoWriter("output3.mp4",cv2.VideoWriter_fourcc(*'mp4v'),15,(700,500))
while cam.isOpened():
    _,frame = cam.read()
    if _ == True:

        img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        img = cv2.inRange(img,lower,upper)
        contours = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = contours[0]
        try:
            for i in cnts:
                # cv2.drawContours(frame,[i],-1,(0,0,255),3)
                M=cv2.moments(np.array(i))
                if M['m00']>0:
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    cv2.circle(frame,(cx,cy),2,(0,0,255),2)
        except:
            print("error")
        frame = cv2.resize(frame, (700, 500))
        cv2.imshow("video",frame)
        output.write(frame)
        key = cv2.waitKey(1)&0xFF
        if key == ord('q'):
            break
    else:
        break
cam.release()
output.release()
cv2.destroyAllWindows()

