# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:47:56 2019

@author: sainath.dutkar
"""

import logging
import boto3
from botocore.exceptions import ClientError


def download_S3_file(file_name, bucket, object_name):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    

    # Upload the file
    s3_client = boto3.client('s3' )
    try:
        s3_client.download_file(bucket,object_name,file_name)
        
    except ClientError as e:
        logging.error(e)
        return False
    return True



flag = download_S3_file("downloadedDoc.txt","njcpoc","Doc1")

print(flag)