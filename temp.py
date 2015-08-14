# read ds18b20 sensor.
# you can change the pin for "1-wire"
#
# edit "sudo nano /boot/config.txt" and add this line to the bottom of the file
# dtoverlay=w1-gpio,gpiopin=26
#
# Test your sensor:
# sudo modprobe w1-gpio
# sudo modprobe w1-therm
#
# list the divices
# ls /sys/bus/w1/devices/
# acess the device read:
# cat /sys/bus/w1/devices/28-000004c0002b/w1_slave
# 
#!/usr/bin/python
def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline()
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc== 'YES':
      line = f.readline()
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()
    
    return int(mytemp[1])
    
  except:
    return 99999
    
if __name__ == '__main__':
  id = '28-000004c0002b'
  print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))
  
  id = '28-000004bf7965'
  print "Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))
