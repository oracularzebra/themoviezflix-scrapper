from bs4 import BeautifulSoup;
import requests;
import json;

sites_file = open('sites.json', encoding='utf-8').read()
sites_obj = json.loads(sites_file)
#sites['sites'][0]['id']  //Here we are getting site id
def checkWebsites():    
    
    working_sites = []
    for i in sites_obj['sites']:
        request = requests.get(i['url'])
        if(request.ok):
            print(i['url'], "is live !")
            working_sites.append(i['url'])
        
    return working_sites