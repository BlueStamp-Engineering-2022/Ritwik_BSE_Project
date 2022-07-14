import boto3
s3 = boto3.resource('s3')
# Get list of objects for indexing
images=[('ritwik1.jpeg','Ritwik Nigam'),
       ('ritwik2.jpeg','Ritwik Nigam'),
       ('ritwik3.jpeg','Ritwik Nigam'),
       ('ritwik4.jpeg','Ritwik Nigam'),
       ('ritwik5.jpeg','Ritwik Nigam')
      ]
# Iterate through list to upload objects to S3   
for image in images:
   file = open(image[0],'rb')
   object = s3.Object('ritwik-faces',image[0])
   ret = object.put(Body=file,
                   Metadata={'FullName':image[1]}
                   )
   #print(image[0])
   #print(image[1])
