from utils import *

import cv2
w=360
h=240
pid = [0.5,0.5,]
pError = 0
startCounter = 1 # to test for no flight put 1 and For Flight put as 0


myDrone = initializeTello()



while True:
    
    #Flight
    if startCounter == 0:
        #myDrone.takeoff()
        startCounter = 1
        
    
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        myDrone.land()
        break