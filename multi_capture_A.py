import RPi.GPIO as gp
import os
import pipes

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
 while( 1 )
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    capture(1)

    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    capture(2)

    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    capture(3)

    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    capture(4)

def capture(cam):
    t = pipes.Template()
    t.append('tr a-z A-Z')
    f = t.open("Camera_Switch", 'r')
    str = f.read()
    if( str < 1)
    break
    else 
    print "camera = 4 ", str



if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
