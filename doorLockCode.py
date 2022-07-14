import boto3
import botocore
from decimal import Decimal
import json
import urllib
BUCKET = "ritwik-faces"
KEY = "image.jpeg"
IMAGE_ID = KEY
COLLECTION = "face_collection"
dynamodb = boto3.client('dynamodb', "us-west-1")
s3 = boto3.client('s3')

def update_index(tableName,faceId, fullName):
    response = dynamodb.put_item(
    TableName=tableName,
    Item={'RekognitionId': {'S': faceId},'FullName': {'S': fullName}}
    )

def index_faces(bucket, key, collection_id, image_id=None, attributes=(), region="us-west-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.index_faces(
    Image={
    "S3Object": {
                                "Bucket": bucket,
                                "Name": key,
                        }
                },
                CollectionId=collection_id,
                ExternalImageId="ritwik",
            DetectionAttributes=attributes,
    )
    #print(response)\
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                faceId = response['FaceRecords'][0]['Face']['FaceId']
                #print(faceId)
                ret = s3.head_object(Bucket=bucket,Key=key)
                personFullName = ret['Metadata']['fullname']
                update_index('face_collection',faceId,personFullName)
    return response['FaceRecords']

def guest_search(bucket, key, collection_id, image_id=None, attributes=(), region="us-west-1"):
    rekognition = boto3.client("rekognition", region)
    try:
        response = rekognition.search_faces_by_image(
        Image={
        "S3Object": {
                                    "Bucket": bucket,
                                    "Name": key,
                            }
                    },
                    CollectionId=collection_id
        )
        k=0
        #print(response)
        ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
        if len(response['FaceMatches']) == 0:
            print('new guest is at door')
            k=1
        else:
            for match in response['FaceMatches']:
                #print(match['Face']['FullName'],match['Face']['Confidence'])
                face = dynamodb.get_item(
                    TableName='face_collection',
                    Key={'RekognitionId':{'S':match['Face']['FaceId']}})
                #print(face)
                if 'Item' in face:
                    guest = face['Item']['FullName']['S']
                    print("Person at the door:",guest)
                    if (guest=='Ritwik Nigam'):
                        ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
                        ser.reset_input_buffer()
                        time.sleep(2)
                        ser.write(b"open\n")
                        #print("Test1")
                        time.sleep(5)
                        #print("Test2")
                        ser.write(b"close\n")
                        k = 1
                    break
        if k==1 or k == 2:
            send_email()
        if k == 1:
            ser.write(b"red\n")
        #print(response)
        return
    except botocore.exceptions.ClientError as e:
        print('No Face Found')



import time
import picamera
import serial


s31 = boto3.resource('s3')

import RPi.GPIO as GPIO

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
count=0
previn=1


def gpio_callback():
        capture_image()
        time.sleep(0.3)
        print('Captured')
        upload_image()
        time.sleep(2)
        guest_search(BUCKET, KEY, COLLECTION, IMAGE_ID)
        return

def but(Pin4):
    global previn
    global count
    inp=GPIO.input(Pin4)
    #print(not previn,inp)
    if ((not previn) and inp):
        count = count + 1
        #print ("BUtton pressed")
        gpio_callback()
        #print (count)
    previn = inp
    time.sleep(0.05)

#GPIO.add_event_detect(4, GPIO.FALLING, callback=gpio_callback, bouncetime=3000)


def capture_image():

        with picamera.PiCamera() as camera:
                camera.resolution = (640, 480)
                camera.start_preview()
                camera.capture('image.jpeg')
                camera.stop_preview()
                camera.close()
                return


def upload_image(FullName="Guest"):
        file = open('image.jpeg','rb')
        object = s31.Object('ritwik-faces','image.jpeg')
        ret = object.put(Body=file,Metadata={'FullName':FullName})
        #print(ret)
        return
def send_email():
    fromaddr = "ritwiknigam06@gmail.com"
    toaddr = "ritwiknigam06@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "New Guest"
    #for record in index_faces(BUCKET, KEY, COLLECTION, IMAGE_ID):
        #face = record['Face']
    body = "A new guest is waiting at your front door. Photo of the guest is attached\n"
    #body+=str(face['Confidence'])+str(face['FaceId'])

    msg.attach(MIMEText(body, 'plain'))
    #print(face)
    filename = "image.jpeg"
    attachment = open("/home/ritwik/image.jpeg", "rb")
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

try:
    while(True):
        but(4)
except KeyboardInterrupt:
    GPIO.cleanup()

