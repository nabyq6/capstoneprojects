import RPi.GPIO as gp
import pygame
'''
import cv
import picamera.array
import PiRGBArray
import PiCamera
'''
import os
import time

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

def main():
    while 1:
        Fh = open('control_file.txt', 'r') 
        camera = Fh.readline(15)
        print ("Read is:%s " % camera)
        Fh.close()

        if( camera[0] == "1"):
            print('main camera')
            gp.output(7, False)
            gp.output(11, False)
            gp.output(12, True)
            capture(camera)
          
        if( camera[0] == "3" ):
            print('camera 2')
            gp.output(7, True)
            gp.output(11, False)
            gp.output(12, True)
            capture(2)
        
        if(camera[0] == "2"):
            print('camera 3')
            gp.output(7, False)
            gp.output(11, True)
            gp.output(12, False)
            capture(3)
           
            #gp.output(7, True)
            #gp.output(11, True)
            #gp.output(12, False)


def capture(cam):
    new_cam = cam

    while cam == new_cam: 
        cmd = "raspistill -o capture_.jpg " 
        os.system(cmd)
        Fh = open('control_file.txt', 'r') 
        new_cam = Fh.readline(10)
        Fh.close()
        print("audio is outputing")
        pygame.mixer.init()
        print ("Read is:%s " % cam)
        if( cam[0] == "1"):
            print("hit")
            pygame.mixer.music.load("you-got-it-1.wav")
#        if(cam == 2):
#            pygame.mixer.music.load("test.m4a")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
'''
camera = PiCamera();
camera.resolution = (640 ,480)
camera.framerate = 32
rawCapture = PiRGBArray( camera, size=(640, 480))
time.sleep(.1)
for frame in camera.capture_continous( rawCapture, format = "bgr", use_video_port = True):
    
    image = frame.array
    
    cv2.imshow("Frame", image)
    key = cv2.waitkey(1) & 0xFF
    rawCapture.truncate(0)
    
    if key == ord("q"):
        break;
    
'''

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
