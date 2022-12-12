from bs4 import BeautifulSoup;
import requests;
from download_links_page import follow_the_link;

def find_download_links(url):
    
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    
    if(request.ok):

        try:
            #there are two tags with movie heading 
            #p tag and h tag
            #I'll find the one with the inner html as 'Download Links'
            #If the above one was not found I'll look for p tag and find its sibling
            all_p_tags = soup.findAll('p',{'style':'color:#008080'})
            all_h4_tags = soup.findAll('h4',{'style':'color:#008080'})

            #We need to find non empty sibling of p tag
            try:
                index = 0
                for p in all_p_tags:
                    print(index, p.text)
                    index += 1
                
                p_tag_index = int(input("Enter the index "))
                p_sibling = all_p_tags[p_tag_index].next_sibling
                #Now we will visit the download page 

                #We need to find all the a tags which are child of p_sibling
                #a contains the link in href attribute and span contains the name of website
                a_p_sibling = p_sibling.findAll('a')
                id=0
                for website in a_p_sibling:
                    print(id, website.find('span').text, website.attrs['href'])
                    id += 1
                
                id = int(input("Enter the id "))
                follow_the_link(a_p_sibling[id].attrs['href'])
            except:
                index = 0 
                for h4 in all_h4_tags:
                    print(index, h4.text)
                    index += 1

                h4_tag_index = int(input("Enter the index "))
                h4_sibling = all_h4_tags[h4_tag_index].next_sibling.next_sibling
                a_h4_sibling = h4_sibling.findAll('a')
                id = 0
                for website in a_h4_sibling:
                    print(id, website.text, website.attrs['href'])
                    id += 1
                id = int(input("Enter the id "))
                follow_the_link(a_h4_sibling[id].attrs['href'])

        except:
            print("ERROR- MOVIE PAGE")