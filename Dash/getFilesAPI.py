# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:11:00 2019

@author: saidu
"""

import requests
import json


def getDocNames(parameters):
    api_Url = "https://**************"
    response = requests.post(api_Url,params= parameters )
    data = response.json()
    docList = []
    for key,value in data.items():
        docList.append(value)
        
    return docList