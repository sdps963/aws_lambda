 

#Lambda Function 

from __future__ import print_function 
import json 
import urllib
import boto3 
import os 

print('Loading function') 

s3 = boto3.resource('s3') 

def lambda_handler(event, context): 

    #print("Received event: " + json.dumps(event, indent=2)) 
    #Get the object from the event and show its content type 

    bucket = event['Records'][0]['s3']['bucket']['name'] 
    print("source bucket name: "+bucket) 

    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))  
    print("key name: "+key) 

    dest_bucket = s3.Bucket(os.environ['Buckt']) 
    print("destination bucket name: "+dest_bucket.name) 

    try: 

        copy_source = {  

            'Bucket': bucket, 

            'Key': key 

        } 

        dest_obj = dest_bucket.Object('appcache/'+key) 

        dest_obj.copy(copy_source) 

        print("File copied successfully") 

    except Exception as e: 

        print(e) 
