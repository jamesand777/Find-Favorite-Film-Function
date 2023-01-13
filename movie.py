import random
import requests
from bs4 import BeautifulSoup

url = 'https://films.criterionchannel.com/'
url2 = 'https://www.imdb.com/chart/top'

def get_year(movie_tag):
    moviesplit = movie_tag.text.split()
    year = moviesplit[-1] # last item 
    return year




def main():
    response = requests.get(url2)
    html = response.text

#   soup = BeautifulSoup(response.text, 'lxml') # faster

    soup = BeautifulSoup(html, 'html.parser')
    # movietags = soup.select('td.criterion-channel__td criterion-channel__td--title')


    # print(soup.prettify())


    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

 
    years = [get_year(tag) for tag in movietags]
    actors_list =[tag['title'] for tag in inner_movietags] # access attribute 'title'
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value'

    n_movies = len(titles)

    idx = 0
    for tag in movietags:
         print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')
         idx += 1
         if idx == 10:
            break



"""
Random Selection


    while(True):
        idx = random.randrange(0, n_movies)
        
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

        user_input = input('Do you want another movie (y/[n])? ')
        if user_input != 'y':
            break

"""



if __name__ == '__main__':
    main()

