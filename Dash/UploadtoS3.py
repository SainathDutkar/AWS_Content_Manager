# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:47:56 2019
@author: sainath.dutkar
"""

import logging
import boto3
from botocore.exceptions import ClientError


def upload_file(file_name, bucket, object_name,DocSeq,
                DocType,Venue,Year,DocPrv,PrvReason,DocCode,DocDes,Mime,CourtDiv,ItemType):
    
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
        
    # Upload the file
    access_key_id="******************"
    secret_access_key= "*********************"
        
    # Upload the file
    s3_client = boto3.client('s3',aws_access_key_id=access_key_id,
         aws_secret_access_key= secret_access_key)
    try:
     
        response = s3_client.upload_file(file_name, bucket, object_name,ExtraArgs={'Metadata':
            {'Docket_Seq_Number': DocSeq,
             'Docket_Type_Code': DocType,
             'Docket_Venue_ID':Venue,
             'Docket_Court_Year':Year,
             'Document_Privacy_Code':DocPrv,
             'Document_Privacy_reason':PrvReason,
             'Document_Code':DocCode,
             'Document_Description':DocDes,
             'Document_Mime_Type':Mime,
             'EFILING_COURT_DIV':CourtDiv,
             'Item_Type':ItemType
             }})
    except ClientError as e:
        logging.error(e)
        return False
    return True

