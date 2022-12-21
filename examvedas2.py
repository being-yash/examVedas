# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd 
 
# Make requests from webpage
url = 'https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-average/'
result = requests.get(url) 
 
# Creating soap object
soup = BeautifulSoup(result.text,'lxml') 

pagination = soup.find("div", {"class": "pagination"})
page_links = ['https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-average/']
links = pagination.find_all('a', href=True)
for a in links:
  ref = a['href']
  page_links.append(ref)
page_links = page_links[:-1]
print(page_links)
got_q = []
for page in page_links:

  url2 = page
  result = requests.get(url2) 
   
  # Creating soap object
  soup2 = BeautifulSoup(result.text,'lxml') 

  questions = soup2.find_all("div", {"class": "question-main"})

  inners = soup2.find_all("div", {"class": "question-inner"})

  
  for i,j in zip(questions,inners):
    k= i.get_text()
    l = 'the Answers'
    m = j.get_text()
    final_q = k+l+m
    the_q = []    
    the_q.append(final_q)
    got_q.append(the_q)

print(got_q)


