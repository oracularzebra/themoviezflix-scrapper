from bs4 import BeautifulSoup;
import requests;
import json;

def checkWebsites():    

        websites = ['https://themoviezflix.co.in']
        request = requests.get(websites[0])
        if(request.ok):
            print('themoviezflix.co.in', "is live !")

        return websites