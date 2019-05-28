from __future__ import print_function
import json
import config
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions,CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey= config.ibm_api_key,
    url='https://gateway-tok.watsonplatform.net/natural-language-understanding/api')

def ibmContent(text):

    response1 = natural_language_understanding.analyze(
        text=text,
        features=Features(keywords=KeywordsOptions(limit = 10))).get_result()

    jData = json.loads(json.dumps(response1, indent=2, ensure_ascii=False))  #keyword 추출

    response2 = natural_language_understanding.analyze(
        text=text,
        features=Features(categories=CategoriesOptions(limit=3))).get_result()

    jData2 = json.loads(json.dumps(response2, indent=2, ensure_ascii=False)) #카테고리 추출

    keywords = ''
    relevance = ''
    categories = ''

    for i in jData['keywords']:
        keywords += i['text']
        keywords += '#'

    for i in jData['keywords']:
        relevance += str(i['relevance'])
        relevance += '#'

    for i in jData2['categories']:
        categories += i['label']
        categories += '#'

    return keywords, relevance, categories
