# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:00:59 2019

@author: sainath.dutkar
"""

import logging
import boto3
from botocore.exceptions import ClientError




s3 = boto3.client('s3')

with open('testing','wb') as f:
    s3.download_fileobj('njcpoc', 'Example2', f)



print(S3file)