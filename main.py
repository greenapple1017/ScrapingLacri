import requests
from bs4 import BeautifulSoup
url = 'https://orbi.kr/search?type=imin&q=2'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.post-list')
    titles = ul.select('li > div > p > a')
    with open("post.txt", 'w') as f:
        for title in titles:
            f.write(title.get_text())
else:
    print(response.status_code)