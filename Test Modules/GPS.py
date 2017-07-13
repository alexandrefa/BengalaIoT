import os
import serial
import pynmea2

def startGPS():
    os.system('sudo systemctl start qdsp-start.service')
    os.system('sudo systemctl start gnss-gpsd.service')
    os.system('sudo systemctl start qmi-gps-proxy.service')
    os.system('sudo systemctl restart gpsd')


def main():
    startGPS()
    gps = serial.Serial('/dev/ttyGPS0')
 
    while True:
        data = gps.readline()
        i = data.find('$GPGGA')
        if (i>0):
		msg = pynmea2.parse(data[i:])
		print 'Latitude: ' + str(msg.latitude)
		print 'Longitude: ' + str(msg.longitude)
		print ' '
		print ' '

if __name__ == '__main__':
    try:
        main()
    except FatalError as e:
        print '\nA fatal error occurred: %s' % e
        gps.close()
        sys.exit(2)
    except KeyboardInterrupt:
        print '\nExit'
        gps.close()
