import requests
from bs4 import BeautifulSoup
import re
import datetime
def scrap(name):
    request_result=requests.get("https://en.wikipedia.org/wiki/"+name)
    soup=BeautifulSoup(request_result.text,"html.parser")
    text = soup.get_text()
    pattern='born (\w*) (\d{2}), (\d{4})'
    ot=re.findall(pattern,text)
    birth_date_str = f"{ot[0][0]} {ot[0][1]}, {ot[0][2]}"
    birth_date = datetime.datetime.strptime(birth_date_str, "%B %d, %Y")
    current_date = datetime.datetime.now()
    difference = current_date - birth_date
    days_passed = difference.days
    return(days_passed,ot)
name=input("Enter a celibrity name")
print(scrap(name))
