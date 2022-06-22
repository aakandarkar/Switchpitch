#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 09:21:45 2022

@author: evelynwang
"""

import os
import pandas as pd
import numpy as np
from google.cloud import language_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/evelynwang/Desktop/switchpitch/google-cloud/lustrous-acumen-352417-a17f95240219.json"

#diffbot output files
df=pd.read_csv('/Users/evelynwang/Desktop/switchpitch/50startups/raw_data.csv')
df0=df.iloc[:,[1,2,3]]
#df.iloc[1,1]
df0['description'].replace({'NULL': None, 'Nan': None,'NaN': None,'nan': None})
df0=df0.dropna()
df0.reset_index(drop=True, inplace=True)

df0['google_keywords']=''
df0.to_csv('/Users/evelynwang/Desktop/switchpitch/50startups/cleaned_data.csv')

#############################
#Entity analysis:
#############################
for i in range(0,df0.shape[0]):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": df0['description'][i], "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_entities(request = {'document': document, 
                                                  'encoding_type': encoding_type})
    entity_list=[]
    # Loop through entitites returned from the API
    # Entities are returned in the order (highest to lowest) of their salience scores
    for entity in response.entities:
        entity_list.append(entity.name)
    df0['google_keywords'][i]= entity_list
df0.to_csv('/Users/evelynwang/Desktop/switchpitch/50startups/google_data.csv')
