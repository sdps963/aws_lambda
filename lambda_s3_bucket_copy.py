import boto3
import urllib
# This function copies all the files in a S3 bucket to another bucket
def lambda_handler(event, context):
    event_record = event['Records'][0]
    s3_download_bucket = event_record['s3']['bucket']['name']
    s3_destination_bucket = 'source-9696'
    s3_destination_key = event_record['s3']['object']['key']
    
    s3_resource = boto3.resource('s3')
    for srcobj in s3_resource.Bucket(s3_download_bucket).objects.all():
        
        source_file = {
            'Bucket': event_record['s3']['bucket']['name'],
            'Key':srcobj.key
        }
    

        s3_resource.meta.client.copy(source_file, s3_destination_bucket, srcobj.key)
  
