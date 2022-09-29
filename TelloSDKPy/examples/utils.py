from djitellopy import Tello
import cv2
import numpy as np


def initializeTello():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0 
    myDrone.left_right_velocity = 0 
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0 
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone,w=1440,h=900):
    # GET THE IMGAE FROM TELLO
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w, h))
    print("THIS IS THE IMAGE")
    return img

'''
def findFace(img):
    hand_cascade = cv2.CascadeClassifier('hand.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)
    contour = hands
    contour = np.array(contour)
    
    
    if count==0:

        if len(contour)==2:
            cv2.putText(img=frame, text='Your engine started', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if count>0:

        if len(contour)>=2:
            cv2.putText(img=frame, text='You can take your car on long drive', org=(int(100 / 2 - 20),int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(255, 0, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==1:
            cv2.putText(img=frame, text='You can speed upto 80km/h', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 255, 0))
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour)==0:
            cv2.putText(img=frame, text='Brake is applied slowly', org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1,
                        color=(0, 0, 255))


    count+=1
    
'''