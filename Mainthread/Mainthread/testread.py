import RPi.GPIO as gp
import os

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
        camera = Fh.readline(10)
        print ("Read is:%s " % camera)
#       print(len(camera))
        Fh.close()
        
        while( camera[0] == "1"):
            gp.output(7, False)
            gp.output(11, False)
            gp.output(12, True)
            capture(1)
            Fh = open('control_file.txt', 'r') 
            camera = Fh.readline(10)
            print ("Read is:%s " % camera)
            #print(len(camera))
            Fh.close()

        while( camera[0] == "3" ):
            print('camera 2')
            gp.output(7, True)
            gp.output(11, False)
            gp.output(12, True)
            capture(2)
        
        while(camera[0] == "2"):
            print('camera 2')
            gp.output(7, False)
            gp.output(11, True)
            gp.output(12, False)
            capture(3)

            #gp.output(7, True)
            #gp.output(11, True)
            #gp.output(12, False)
            #capture(4)

def capture(cam):
    cmd = "raspistill -o capture_.jpg " 
    os.system(cmd)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)

