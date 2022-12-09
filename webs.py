import requests
from bs4 import BeautifulSoup

nodejs_lts_url = 'https://nodejs.org/en/download/'
nodejs_latest_url = 'https://nodejs.org/en/download/releases/'
strapi_url = 'https://strapi.io/changelog'
nextjs_url = 'https://nextjs.org/blog'


# NodeJS - LTS
response = requests.get(nodejs_lts_url)
soup = BeautifulSoup(response.text, 'html.parser')
nodejs_lts_version = soup.p.getText()
print("NodeJS: " , nodejs_lts_version)
# NodeJS - LATEST
response = requests.get(nodejs_latest_url)
soup = BeautifulSoup(response.text, 'html.parser')
nodejs_latest_version = soup.tbody
print("NodeJS (LATEST CURRENT): ", nodejs_latest_version.tr.td.getText(), "(", nodejs_latest_version.tr.time.getText(), ")")

#Strapi
response = requests.get(strapi_url)
soup = BeautifulSoup(response.text, 'html.parser')

strapi_version = str(soup.h3)
strapi_begin = strapi_version.find("S")
strapi_end = strapi_version.find("-")

strapi_date = str(soup.find("span", {"class": "typography_Label__1knAy"}))
strapi_date_begin = strapi_date.find(">")
strapi_date_end = strapi_date.find("</")

print("Strapi: %s (%s)" % (strapi_version[strapi_begin:strapi_end] , strapi_date[(strapi_date_begin+1):strapi_date_end]))

# NextJS
response = requests.get(nextjs_url)
soup = BeautifulSoup(response.text, 'html.parser')
nextjs_version = soup.find("h3", {"class": "preview_postTitle_1DQfX"})
nextjs_version_date = soup.p.getText()
print(nextjs_version)
print(nextjs_version_date)
