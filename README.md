Drones are becoming more and more popular these days. However the size is the main factor while flying the drone. As smaller drones don’t have the sensors and processing power to fly autonomously. Hence to make the drones more intelligent , we are incorporating them with Computer Vision. The  Computer Vision is the interesting part because drone is learning the position of person in realtime as it changes and adjusts itself in three dimensions.

This is a consumer drone integrated with Artificial Intelligence and Computer vision to make him track the face and follow it without using any sensors other than Camera. As the camera cannot have the sense of depth; hence we we have used  the Computer Vision which incorporates the facial recognition functionality. Also our algorithm tracks the face and makes the drone fly autonomously without any need of pilot. The basic principal behind this algorithm is re-enforcement learning; where the  program adapts to learn the live location of the object we are tracking and takes appropriate decision upon it. Like if the face goes left then the drone turns Left. In this way we can also adjust the distance between the drone and the person closer and far. This feature is achieved by the variable face size of a person from camera. The perspective changes the size of the face. Like if the drone is near to the face, then the face size appears bigger through the camera and if the drone is far from the face then the face size appears smaller through the camera. 
	Now the Tracking function achieved by maintaining the face to be position at the centre of the screen. Then fixed size of the face is provide which can be the z axis and also gave the safe zone distance. To safely fly the drone without crashing into the person. The drone follows the person easily and efficiently.
  
Tested with Python 3.6, but it also may be compatabile with other versions.


## Install
```
$ pip install -r requirements.txt
```

## Usage
```
  -h, --help            ** = required
  -d DISTANCE, --distance DISTANCE
                        use -d to change the distance of the drone. Range 0-6
                        (default: 3)
  -sx SAFTEY_X, --saftey_x SAFTEY_X
                        use -sx to change the saftey bound on the x axis .
                        Range 0-480 (default: 100)
  -sy SAFTEY_Y, --saftey_y SAFTEY_Y
                        use -sy to change the saftey bound on the y axis .
                        Range 0-360 (default: 55)
  -os OVERRIDE_SPEED, --override_speed OVERRIDE_SPEED
                        use -os to change override speed. Range 0-3 (default:
                        1)
  -ss, --save_session   add the -ss flag to save your session as an image
                        sequence in the Sessions folder (default: False)
  -D, --debug           add the -D flag to enable debug mode. Everything works
                        the same, but no commands will be sent to the drone
                        (default: False)
```

## Controls
- Esc: Quit Application
- T: Takeoff
- L: To Land

##### AI Mode
- 0: Set Drone distance to 0
- 1: Set Drone distance to 1
- 2: Set Drone distance to 2
- 3: Set Drone distance to 3
- 4: Set Drone distance to 4
- 5: Set Drone distance to 5
- 6: Set Drone distance to 6

##### Override Mode
- Backspace: Enable / Disable Override mode
- W/S: Fly Forward/Back
- A/D: Pan Left/Right
- Q/E: Fly Up/Down
- Z/C: Fly Left/Right
- 1: Set Drone speed to 1
- 2: Set Drone speed to 2
- 3: Set Drone speed to 3


## Roadmap
- Figure out a way to save images at a frame rate from 24-60, or at least 12 fps
- Display current battery power on screen
- Add a movement gradient dependent on distance from subject
- Add more to the facial recog to be able to tell when the drone needs to fly left or right
- Use pose estimation for input commands
- Add a function where the drone will ignore all faces except the one you specify
- ~~Fix key pressing spam~~

# Credits
This script has been adapted from Damià Fuentes Escoté's [TelloSDKPy](https://github.com/damiafuentes/DJITelloPy) script, please check it out if you want to learn more about that.


#### Backend Thanks
- **Damià Fuentes Escoté** 
