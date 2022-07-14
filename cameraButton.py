import time
import picamera
import serial

import boto3

s3 = boto3.resource('s3')

import RPi.GPIO as GPIO

import smtplib
#from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def gpio_callback(self):
	capture_image()
	time.sleep(0.3)
	print('Captured')
	upload_image()
	time.sleep(2)
	send_email()
	

GPIO.add_event_detect(4, GPIO.FALLING, callback=gpio_callback, bouncetime=3000)


def capture_image():
	with picamera.PiCamera() as camera:
		camera.resolution = (640, 480)
		camera.start_preview()
		camera.capture('sample.jpeg')
		camera.stop_preview()
		camera.close()
		return
		
				
def upload_image():
	file = open('sample.jpeg','rb')
	object = s3.Object('ritwik-faces','sample.jpeg')
	ret = object.put(Body=file,
			Metadata={'FullName':'Guest'}
			)
	print(ret)
	return


def send_email(): 
    fromaddr = "ritwiknigam06@gmail.com"
    toaddr = "ritwiknigam06@gmail.com"
     
    msg = MIMEMultipart()
     
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "New Guest"
     
    body = "A new guest is waiting at your front door. Photo of the guest is attached."
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "sample.jpeg"
    attachment = open("/home/ritwik/Project/sample.jpeg", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "lhdvgfvyltjhrzpg")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
	

while True:
	time.sleep(2)
