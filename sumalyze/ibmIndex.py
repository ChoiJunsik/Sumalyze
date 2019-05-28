from __future__ import print_function
import json
import config
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions,CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey= config.ibm_api_key,
    url='https://gateway-tok.watsonplatform.net/natural-language-understanding/api')

def ibmIndex(text,summaries):

    response1 = natural_language_understanding.analyze(
        text=text,
        features=Features(keywords=KeywordsOptions(limit = 2))).get_result()

    jData = json.loads(json.dumps(response1, indent=2, ensure_ascii=False))  #keyword 추출

    keywords = []
    indexList = []
    for i in jData['keywords']:
        keywords.append(i['text'])

    for c in summaries:
        if (keywords[0] in c) and (keywords[1] in c):
            return c
        elif (keywords[0] in c):
            return c
        elif (keywords[1] in c):
            return c    
