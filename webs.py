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
nodejs_lts_begin = nodejs_lts_version.find(":")
nodejs_lts_end = nodejs_lts_version.find("(")
print("NodeJS (LTS):" , nodejs_lts_version[(nodejs_lts_begin+2):nodejs_lts_end])
# NodeJS - LATEST
response = requests.get(nodejs_latest_url)
soup = BeautifulSoup(response.text, 'html.parser')
nodejs_latest = soup.tbody
nodejs_latest_version = nodejs_latest.tr.td.getText()
nodejs_latest_version_begin = nodejs_latest_version.find(".js")
nodejs_latest_version_end = nodejs_latest_version.find("(")
nodejs_latest_date = nodejs_latest.tr.time.getText()
print("NodeJS (LATEST CURRENT): %s (%s)" % (nodejs_latest_version[(nodejs_latest_version_begin+4):], nodejs_latest_date))
#Strapi
response = requests.get(strapi_url)
soup = BeautifulSoup(response.text, 'html.parser')

strapi_version = str(soup.h3)
strapi_begin = strapi_version.find("v")
strapi_end = strapi_version.find("-")

strapi_date = str(soup.find("span", {"class": "typography_Label__1knAy"}))
strapi_date_begin = strapi_date.find(">")
strapi_date_end = strapi_date.find("</")

print("Strapi: %s (%s)" % (strapi_version[strapi_begin:strapi_end] , strapi_date[(strapi_date_begin+1):strapi_date_end]))
# NextJS
response = requests.get(nextjs_url)
soup = BeautifulSoup(response.text, 'html.parser')
nextjs = soup.find("h3", {"class":"f2 fw7 preview_postTitle__1DQfX"}).getText()
nextjs_begin = nextjs.find(".js")
nextjs_end = nextjs.find("(")
nextjs_date = soup.find("p", {"class": "f5"}).getText()
nextjs_date_begin = nextjs_date.find(",")
nextjs_date_end = nextjs_date.find("ago")
print("NextJS:" , nextjs[(nextjs_begin+3):], "(%s)" % nextjs_date[(nextjs_date_begin+2):(nextjs_date_end-3)])
