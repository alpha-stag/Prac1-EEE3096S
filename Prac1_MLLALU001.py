#!/usr/bin/python3
"""
Python Practical Template
Names: Aluwani Malalamabi
Student Number: MLLALU001
Prac: Prac1
Date: <dd/mm/yyyy>
"""

# import Relevant Librares
import time
import RPi.GPIO as GPIO

from itertools import product

#setup the GPIO pins to outputs and inputs and set the board numbering type (BCM/BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)

#create a list of 3 LED pins
chlist = (17,27,22)


count = 0

#create an ndarray from itertools library
mylist = list(product([0,1],repeat=3))


def main():
    global count
    time.sleep(1)
    global chlist
    
    print(chlist)
    print(count)

#count upwards
def upcount(channel):
    global mylist
    global count
    
    #time.sleep(2)
    if (count==7):
        count=0
    else:
        count+=1
        
    GPIO.output(chlist,mylist[count])
#count downwards
def downcount(channel):
    global mylist
    global count
    

    #time.sleep(2)
    if (count==0):
        count=7
    else:
        count-=1
    
    GPIO.output(chlist,mylist[count])
#interupts   
GPIO.add_event_detect(23,GPIO.FALLING,callback=upcount,bouncetime=500)
GPIO.add_event_detect(24,GPIO.FALLING,callback=downcount,bouncetime=500)


if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e)
