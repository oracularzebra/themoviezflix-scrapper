import requests;
from bs4 import BeautifulSoup;

def follow_the_link(url):

    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')

    #For webseries websites has h3 tags with Episode number as heading
    #For movies we have span tags Which represent the website name
    #If page contains Episode keyword we will treat it as a webseries page

    if(soup.text.__contains__('Episode')):
        print("Webseries")
        
        try:
            all_h3_tags = soup.findAll('h3', {'style':'color:#008080'})
            # print(all_h3_tags)
            all_a_tags_in_h3 = []
            for a in all_h3_tags:
                print(a.find('a').text, a.find('a').attrs['href'])
                all_a_tags_in_h3.append(a.find('a').attrs['href'])
        except:
            print("Last url where error occured is(webseries)", url)

    else:
        print("Movie")
        
        try:
            p_tag = soup.find('p', {'style':'color:#008080'})
            
            p_tag_spans = p_tag.findNextSiblings('span')
            
            for a in p_tag_spans:
                print(a.find('a').text, a.find('a').attrs['href'])
            
        except:
            print("Last url where error occured(movie)", url)
    