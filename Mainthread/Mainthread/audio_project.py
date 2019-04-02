import pygame
import time

def main():
    old_camera = 0
    while 1:
       Fh = open('control_file.txt', 'r') 
       camera = Fh.readline(10)
#       print ("Read is:%s " % camera)
       Fh.close()
       if(camera != old_camera):
           print("capture hit")
           capture(camera)
       
       old_camera = camera;
       time.sleep(1);
       
       
def capture(cam):
    print("audio is outputing")
    pygame.mixer.init()
    pygame.mixer.music.load("you-got-it-1.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


if __name__ == "__main__":
    main()