from check_website import checkWebsites;
from search_movie import search_movie;

movie_name = input("Enter the movies/webseries name ")

# Now we will search in sites one by one and fetch movie page
working_sites_list=checkWebsites()

for i in working_sites_list:
    search_movie(i, movie_name=movie_name)