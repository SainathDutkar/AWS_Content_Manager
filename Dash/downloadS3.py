# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:53:57 2019

@author: saidu
"""

import logging
import boto3
from botocore.exceptions import ClientError
import botocore

def download_S3_file(bucket,objectKey):
    
    
    access_key_id="**************"
    secret_access_key= "******************"
    
    s3 = boto3.resource('s3',region_name='us-east-1',aws_access_key_id=access_key_id,
         aws_secret_access_key= secret_access_key)
        
    try:
        dwnFile = str(objectKey+'.txt')
        s3.Bucket(bucket).download_file(objectKey, dwnFile)
                
            
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            print('Done')
    return True

