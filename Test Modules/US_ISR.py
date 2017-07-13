import mraa
import time
import math

def Subida():
    while echo.read()==1:
        pulse_start=time.time()
        print "01"
    if echo.read()==0:
        pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*speed/2
        distance=round(distance,2)
        print "Distance",distance,"cm"
            

#def Descida():
#    pulse_end=time.time()
#    pulse_duration=pulse_end-pulse_start
#    print "02"
    

trig = mraa.Gpio(32)
echo = mraa.Gpio(27)

trig.dir(mraa.DIR_OUT)
echo.dir(mraa.DIR_IN)
echo.isr(mraa.EDGE_BOTH, Subida, echo)
#echo.isr(mraa.EDGE_FALLING, Descida, echo)

D = 10
speed = 34029
print "Begin"
timeout=time.time()+D


while True:
    trig.write(0)
    time.sleep(0.5)
    trig.write(1)
    time.sleep(0.00002)
    trig.write(0)
    
                            
    
        
    
    
    time.sleep(0.5)
