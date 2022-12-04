import requests
from bs4 import BeautifulSoup

url='https://nodejs.org/en/download/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
nodejs_version =str(soup.p)
strong_begin = nodejs_version.find("<strong>")
strong_end = nodejs_version.find("</strong>")
print("Latest NodeJS Version: ", nodejs_version[(strong_begin+8):strong_end])
