from djitellopy import Tello

tello = Tello()

tello.connect()

print(tello.get_battery())
'''
tello.takeoff()
#tello.move_up(60)

#tello.move_forward(200)
#tello.move_right(200)
#tello.move_back(200)
#tello.move_left(200)
#25 -25 0 25 -75 0 20
tello.curve_xyz_speed(25, 25, 0, 25, -75, 0, 50)
#tello.curve_xyz_speed(25, 25, 0, 25, -75, 0, 30)
tello.land()
'''

tello.takeoff()
tello.move_up(100)
for i in range(0,2):
    tello.move_forward(300)
    tello.move_right(300)
    tello.move_back(300)
    tello.move_left(300)
    
tello.land()
