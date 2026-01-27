
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.training-support.net/webelements/tables")
webpage_content = response.content


soup = BeautifulSoup(webpage_content, "html.parser")


table = soup.find('table')


for tr in table.find_all('tr'):   
    cells = tr.find_all('td')      
    row = [i.text for i in cells] 
    print(row)                    