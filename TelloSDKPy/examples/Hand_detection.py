from utils import *
import cv2
import numpy as np


myDrone = initializeTello()
count = 0

while True:
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (960, 720))
    #print("THIS IS THE IMAGE")
    hand_cascade = cv2.CascadeClassifier('hand.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.2, 2)
    contour = hands
    contour = np.array(contour)
    
    if count==0:

        if len(contour)==2:
            cv2.putText(img=myFrame, text='Start', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            #for (x, y, w, h) in hands:
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if count>0:

        if len(contour)>=2:
            cv2.putText(img=myFrame, text='Start', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(255, 0, 0))
            #for (x, y, w, h) in hands:
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==1:
            cv2.putText(img=myFrame, text='Gonn', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(myFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==0:
            cv2.putText(img=myFrame, text='Brake', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 0, 255))


    count+=1

   
    # DISPLAY IMAGE
    cv2.imshow("MyResult",  img)
    

 
    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) and 0xFF == ord('q'): # replace the 'and' with '&amp;' 
        myDrone.land()
        break