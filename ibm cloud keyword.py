# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:36:39 2022

@author: wendy
"""

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions,EntitiesOptions, KeywordsOptions

authenticator = IAMAuthenticator('lyXSQXrOfaO5V7ptjCsgYkoxzdl4cRCnp36yLZe_meCl')
service = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
service.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com')
response = service.analyze(
    text='Clicoh is a startup born in Cordoba, Argentina in 2018 that provides fulfillment and logistics solutions through innovation and technology for digital companies in Latam',
    features=Features(categories=CategoriesOptions(limit=3))).get_result()
    

print(json.dumps(response, indent=2))


    

