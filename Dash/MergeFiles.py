# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:53:57 2019

@author: saidu
"""

import logging
import boto3
from botocore.exceptions import ClientError
import botocore
import requests


def merge_S3_files(doc1,doc2):
    parameter = {"Doc1":doc1, "Doc2":doc2}
    print(parameter)
    api_merge_url = "https://rad11l79rd.execute-api.us-east-1.amazonaws.com/default/MergeFiles"
    result = requests.post(api_merge_url,params=parameter)
    MergeResult = result.json()
    return MergeResult
