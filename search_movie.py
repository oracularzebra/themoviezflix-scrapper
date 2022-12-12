from bs4 import BeautifulSoup;
import requests;
from movie_page import find_download_links;

def search_movie(url, movie_name):

    request_page_code = requests.get(url).text
    soup = BeautifulSoup(request_page_code, 'lxml')
    

    try:    
        search_form = soup.find('form')
        search_form_input_tag = search_form.find('input') 
        search_tag_id = search_form_input_tag.attrs['name']
        
        search_url = url+"?"+search_tag_id+"="+movie_name.replace(" ", "+")
        sendSearchRequest(search_url, moviename=movie_name)

    except:
        print("Please check the website", url)
    
    
    # find the id of input tag and search in website as /?[tag]=[movie name]

    # movie_request = requests.get(url, params={})

def sendSearchRequest(url, moviename):

    request = requests.get(url).text
    soup = BeautifulSoup(request, 'lxml')

    try:
        all_articles = soup.findAll('article')
        
        #finding the a tags titles attribute matching our movie name
        a_tags = []
        index = 0; 
        for article in all_articles:
            a_tag = article.find('a')
            title = a_tag.attrs['title']

            if(title.lower().__contains__(moviename.lower())):
                a_tags.append(a_tag)
                print(index, title)
                index += 1
        
            
        # print(a_tags[3].attrs['href'])
        if(len(a_tags) > 0):

            a_tags_index = input("Enter the index of movie you want to select ")

            # print(a_tags[int(a_tags_index)]['href'])
            try:
                find_download_links(a_tags[int(a_tags_index)]['href'])
            except:
                print("find_download_links function error")
           
        else:
            print("Movie not found")
        # print(hrefs_with_movie_name)
        # for article in all_articles:
            
            
    except:
        print("ERROR")