from djitellopy import Tello
import cv2
import numpy as np
import time
import datetime
import os
import argparse


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='** = required')
parser.add_argument('-d', '--distance', type=int, default=3,
    help='use -d to change the distance of the drone. Range 0-6')
parser.add_argument('-sx', '--saftey_x', type=int, default=100,
    help='use -sx to change the saftey bound on the x axis . Range 0-480')
parser.add_argument('-sy', '--saftey_y', type=int, default=55,
    help='use -sy to change the saftey bound on the y axis . Range 0-360')
parser.add_argument('-os', '--override_speed', type=int, default=1,
    help='use -os to change override speed. Range 0-3')
parser.add_argument('-ss', "--save_session", action='store_true',
    help='add the -ss flag to save your session as an image sequence in the Sessions folder')
parser.add_argument('-D', "--debug", action='store_true',
    help='add the -D flag to enable debug mode. Everything works the same, but no commands will be sent to the drone')

args = parser.parse_args()

# Speed of the drone is preset in this
S = 20
S2 = 5
UDOffset = 150

# bound box sizes
faceSizes = [1026, 684, 456, 304, 202, 136, 90]

acc = [500,250,250,150,110,70,50]

# Frames per second of the pygame
FPS = 25
dimensions = (960, 720)

# 
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# If we are to save our sessions, we need to make sure the proper directories exist
if args.save_session:
    ddir = "Sessions"

    if not os.path.isdir(ddir):
        os.mkdir(ddir)

    ddir = "Sessions/Session {}".format(str(datetime.datetime.now()).replace(':','-').replace('.','_'))
    os.mkdir(ddir)

class FrontEnd(object):
    
    def __init__(self):
        # Init Tello object that interacts with the Tello drone
        self.tello = Tello()

        # Drone velocities between -100~100
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 20

        self.send_rc_control = False

    def run(self):

        if not self.tello.connect():
            print("Tello not connected")
            return

        if not self.tello.set_speed(self.speed):
            print("Not set speed to lowest possible")
            return

        if not self.tello.streamoff():
            print("Could not stop video stream")
            return

        if not self.tello.streamon():
            print("Could not start video stream")
            return

        frame_read = self.tello.get_frame_read()

        should_stop = False
        imgCount = 0
        OVERRIDE = False
        oSpeed = args.override_speed
        tDistance = args.distance
        self.tello.get_battery()
        

        szX = args.saftey_x

        
        szY = args.saftey_y
        
        if args.debug:
            print("DEBUG MODE ENABLED!")

        while not should_stop:
            self.update()

            if frame_read.stopped:
                frame_read.stop()
                break

            theTime = str(datetime.datetime.now()).replace(':','-').replace('.','_')

            frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
            frameRet = frame_read.frame

            vid = self.tello.get_video_capture()

            if args.save_session:
                cv2.imwrite("{}/tellocap{}.jpg".format(ddir,imgCount),frameRet)
            
            frame = np.rot90(frame)
            imgCount+=1

            time.sleep(1 / FPS)

            
            k = cv2.waitKey(20)

            
            if k == ord('0'):
                if not OVERRIDE:
                    print("Distance = 0")
                    tDistance = 0

            # Press 1 to set distance to 1
            if k == ord('1'):
                if OVERRIDE:
                    oSpeed = 1
                else:
                    print("Distance = 1")
                    tDistance = 1

            
            if k == ord('2'):
                if OVERRIDE:
                    oSpeed = 2
                else:
                    print("Distance = 2")
                    tDistance = 2
                    
            
            if k == ord('3'):
                if OVERRIDE:
                    oSpeed = 3
                else:
                    print("Distance = 3")
                    tDistance = 3
            
            
            if k == ord('4'):
                if not OVERRIDE:
                    print("Distance = 4")
                    tDistance = 4
                    
            
            if k == ord('5'):
                if not OVERRIDE:
                    print("Distance = 5")
                    tDistance = 5
                    
            
            if k == ord('6'):
                if not OVERRIDE:
                    print("Distance = 6")
                    tDistance = 6

            # Press T to take off
            if k == ord('t'):
                if not args.debug:
                    print("Taking Off")
                    self.tello.takeoff()
                    self.tello.get_battery()
                    self.tello.move_up(60)
                self.send_rc_control = True

            # Press L to land
            if k == ord('l'):
                if not args.debug:
                    print("Landing")
                    self.tello.land()
                self.send_rc_control = False

            # Backspace for controls override
            if k == 8:
                if not OVERRIDE:
                    OVERRIDE = True
                    print("OVERRIDE ENABLED")
                else:
                    OVERRIDE = False
                    print("OVERRIDE DISABLED")

            if OVERRIDE:
                # S & W to fly forward & back
                if k == ord('w'):
                    self.for_back_velocity = int(S * oSpeed)
                elif k == ord('s'):
                    self.for_back_velocity = -int(S * oSpeed)
                else:
                    self.for_back_velocity = 0

                # a & d to pan left & right
                if k == ord('d'):
                    self.yaw_velocity = int(S * oSpeed)
                elif k == ord('a'):
                    self.yaw_velocity = -int(S * oSpeed)
                else:
                    self.yaw_velocity = 0

                # Q & E to fly up & down
                if k == ord('e'):
                    self.up_down_velocity = int(S * oSpeed)
                elif k == ord('q'):
                    self.up_down_velocity = -int(S * oSpeed)
                else:
                    self.up_down_velocity = 0

                # c & z to fly left & right
                if k == ord('c'):
                    self.left_right_velocity = int(S * oSpeed)
                elif k == ord('z'):
                    self.left_right_velocity = -int(S * oSpeed)
                else:
                    self.left_right_velocity = 0

            # Quit the program
            if k == 27:
                should_stop = True
                break

            gray  = cv2.cvtColor(frameRet, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=2)

            # Target size
            tSize = faceSizes[tDistance]

            # center dimensions
            cWidth = int(dimensions[0]/2)
            cHeight = int(dimensions[1]/2)

            noFaces = len(faces) == 0

            # Main Algorithm
            if self.send_rc_control and not OVERRIDE:
                for (x, y, w, h) in faces:

                     
                    roi_gray = gray[y:y+h, x:x+w] 
                    roi_color = frameRet[y:y+h, x:x+w]

                    # Face Box properties
                    fbCol = (255, 0, 0) 
                    fbStroke = 2
                    
                    
                    end_cord_x = x + w
                    end_cord_y = y + h
                    end_size = w*2

                    # target coordinates
                    targ_cord_x = int((end_cord_x + x)/2)
                    targ_cord_y = int((end_cord_y + y)/2) + UDOffset

                    # Calculating vector from your face to the center of the screen
                    vTrue = np.array((cWidth,cHeight,tSize))
                    vTarget = np.array((targ_cord_x,targ_cord_y,end_size))
                    vDistance = vTrue-vTarget

                     
                    if not args.debug:
                        
                        if vDistance[0] < -szX:
                            self.yaw_velocity = S
                            
                        elif vDistance[0] > szX:
                            self.yaw_velocity = -S
                            
                        else:
                            self.yaw_velocity = 0
                        
                        
                        if vDistance[1] > szY:
                            self.up_down_velocity = S
                        elif vDistance[1] < -szY:
                            self.up_down_velocity = -S
                        else:
                            self.up_down_velocity = 0

                        F = 0
                        if abs(vDistance[2]) > acc[tDistance]:
                            F = S

                        
                        if vDistance[2] > 0:
                            self.for_back_velocity = S + F
                        elif vDistance[2] < 0:
                            self.for_back_velocity = -S - F
                        else:
                            self.for_back_velocity = 0

                    # face bounding box
                    cv2.rectangle(frameRet, (x, y), (end_cord_x, end_cord_y), fbCol, fbStroke)

                    # target as a circle
                    cv2.circle(frameRet, (targ_cord_x, targ_cord_y), 10, (0,255,0), 2)

                    # safety zone
                    cv2.rectangle(frameRet, (targ_cord_x - szX, targ_cord_y - szY), (targ_cord_x + szX, targ_cord_y + szY), (0,255,0), fbStroke)

                    # estimated drone vector position in relation to face bounding box
                    cv2.putText(frameRet,str(vDistance),(0,64),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

                # if there are no faces detected, don't do anything
                if noFaces:
                    self.yaw_velocity = 0
                    self.up_down_velocity = 0
                    self.for_back_velocity = 0
                    print("NO TARGET")
                
            
            cv2.circle(frameRet, (cWidth, cHeight), 10, (0,0,255), 2)

            dCol = lerp(np.array((0,0,255)),np.array((255,255,255)),tDistance+1/7)

            if OVERRIDE:
                show = "OVERRIDE: {}".format(oSpeed)
                dCol = (255,255,255)
            else:
                show = "Distance: {}".format(str(tDistance))

            # distance choosen
            cv2.putText(frameRet,show,(32,664),cv2.FONT_HERSHEY_SIMPLEX,1,dCol,2)

            # resulting frame
            cv2.imshow(f'Tello Tracking...',frameRet)

        # print the battery percentage
        self.tello.get_battery()

        # release the capture window
        cv2.destroyAllWindows()
        
        
        self.tello.end()


    def battery(self):
        return self.tello.get_battery()[:2]

    def update(self):
        
        if self.send_rc_control:
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity, self.up_down_velocity,
                                       self.yaw_velocity)

def lerp(a,b,c):
    return a + c*(b-a)

def main():
    frontend = FrontEnd()

    # run frontend
    frontend.run()


if __name__ == '__main__':
    main()
