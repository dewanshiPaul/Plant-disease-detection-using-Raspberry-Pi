from mail import email_alert_temp_humid
import Adafruit_DHT as dht
from time import sleep
import urllib.request as urllib2

apiKey = '' #to be set
apiUrl = '' #to be set
link = '' #to be set
pin = 23 #to be set if required

x, y, u, v = 10, 20, 30, 40 #need to configure later

try:
    while True:
        print('Reading data....\n')
        humidity, temperature = dht.read(dht.DHT11, pin)
        if humidity is None or temperature is None:
            print('Sensor is not working\n')
        else:
            print("Temperature: ",temperature," Humidity: ",humidity)
            #send data to cloud
            conn = urllib2.urlopen(apiUrl+'&field1=%s&field2=%s'%(temperature,humidity))
            print(conn.read)
            if(humidity > x or temperature > y or humidity < u or temperature < v):
                subject = 'ALERT!!! Your plants will get affected'
                body = '''
                    Hi user, \n
                         \t This is an email alert is to let you know that your 
                    plants are getting affected because of imbalance in either temperature or humidity. \n
                    To know, analyse via given link
                ''' + link
                to = "" #set
                email_alert_temp_humid(subject,body,to)
        sleep(10)
except KeyboardInterrupt:
    print("End")
    pass
