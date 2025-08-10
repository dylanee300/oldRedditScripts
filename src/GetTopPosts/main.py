# Sends req to reddit to then get the first amount of posts you want.
# You can set the amount of posts to see if you want on line 15. 
# Change the limit to the number you want to see.

import requests
from bs4 import BeautifulSoup

url = 'https://old.reddit.com/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

posts = soup.find_all('div', class_='thing', limit=10) #if you want set the amount of posts you wanna see here.

for post in posts:
    title = post.find('a', class_='title').text
    print(title)