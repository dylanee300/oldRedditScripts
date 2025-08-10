import requests
from bs4 import BeautifulSoup

url = 'https://old.reddit.com/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

first_post = soup.find('div', class_='thing')

author = first_post.find('a', class_='author')

if author:
    print("top author:", author.text)
else:
    print("author not found :(")
