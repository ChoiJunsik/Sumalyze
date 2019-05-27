from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib.request
from urllib import parse

def image_crowling(request, word):
    tmp = 'https://ko.wikipedia.org/wiki/' + parse.quote(word)
    
    html = urllib.request.urlopen(tmp)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    img = soup.find("a","image")
    img = img.find("img")
    
    img_src = img.get("src")
    img_url = 'https:' + img_src

    #urllib.request.urlretrieve(img_url, "./img/" + '당근')
    # return render(request, 'sumalyze/image_crowling.html', {
    #     'url' : img_url,
    # })
    return img_src