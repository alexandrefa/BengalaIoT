import mraa
import time

x = mraa.Gpio(27)


x.dir(mraa.DIR_OUT)



while True:
	x.write(1)
	time.sleep(0.1)
	x.write(0)
	time.sleep(0.1)
      
