import requests
from bs4 import BeautifulSoup

nodejs_url='https://nodejs.org/en/download/'
strapi_url='https://strapi.io/changelog'

print("Updated: yesterday")

# NodeJS
response = requests.get(nodejs_url)
soup = BeautifulSoup(response.text, 'html.parser')
nodejs_version =str(soup.p)
strong_begin = nodejs_version.find("<strong>")
strong_end = nodejs_version.find("</strong>")
print("Latest NodeJS Version: ", nodejs_version[(strong_begin+8):strong_end])

#Strapi
response = requests.get(strapi_url)
soup = BeautifulSoup(response.text, 'html.parser')

strapi_version = str(soup.h3)
strapi_begin = strapi_version.find("S")
strapi_end = strapi_version.find("-")

strapi_date = str(soup.find("span", {"class": "typography_Label__1knAy"}))
strapi_date_begin = strapi_date.find(">")
strapi_date_end = strapi_date.find("</")

print("Latest Strapi Version: %s (%s)" % (strapi_version[strapi_begin:strapi_end] , strapi_date[(strapi_date_begin+1):strapi_date_end]))
