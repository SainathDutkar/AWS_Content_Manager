# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:53:51 2019

@author: sainath.dutkar
"""
import boto3
from boto3.dynamodb.conditions import Key, Attr



access_key_id="******"
secret_access_key= "*******"

dynamodb = boto3.resource('dynamodb',region_name='us-east-1',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)
table = dynamodb.Table('CMPOC')

response = table.query(
    KeyConditionExpression=Key('DocketNumber').eq('ATLCR1930005')
)
items = response['Items']

for x in items:
    print(x['document_code'])

#print(items)