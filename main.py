import requests
from bs4 import BeautifulSoup

url = "https://seekingalpha.com/article/4406922-wesfarmers-limited-wfaff-ceo-rob-scott-on-half-year-2021-results" \
      "-earnings-call-transcript "

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:85.0) Gecko/20100101 Firefox/85.0."
}
resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    print('Status Connected')
else:
    print('Link ERROR')

soup = BeautifulSoup(resp.text, features='html.parser')
print(f'Isi Content \n{resp.text}')
print(f'\nScraping Data Dari Web : {url}')
print(f'\nTile Web : \n{soup.title.string}')
print(f'\nContent Web : \n{soup.contents}')

with open('file.txt', 'w+') as file:
    file.write(resp.text)
    file.close()
