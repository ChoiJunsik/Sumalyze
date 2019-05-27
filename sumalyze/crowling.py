from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib.request
from urllib import parse

def image_crowling(request, word):
    tmp = 'https://ko.wikipedia.org/wiki/' + parse.quote(word)
    
    try:
        html = urllib.request.urlopen(tmp)
        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        img = soup.find("a","image")
        img = img.find("img")

        img_src = img.get("src")
        img_url = 'https:' + img_src

        return img_src

    except Exception as e:
        return None