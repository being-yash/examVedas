# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd 
 
# Make requests from webpage
url = 'https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/'
result = requests.get(url) 
 
# Creating soap object
soup = BeautifulSoup(result.text,'lxml') 

more = soup.find("ul", {"class": "more-section"})
sec_links = ['https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/',]
links = more.find_all('a', href=True)
for a in links:
  ref = a['href']
  sec_links.append(ref)

print(sec_links)
got_q = []
page_links = ['https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=2','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=3','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=4','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=5','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=6','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=7','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=8','https://www.examveda.com/arithmetic-ability/practice-mcq-question-on-number-system/?section=9']

for page in sec_links:

  url2 = page
  result2 = requests.get(url2) 
   
  # Creating soap object
  soup2 = BeautifulSoup(result2.text,'lxml') 

  pagination = soup2.find("div", {"class": "pagination"})
  links = pagination.find_all('a', href=True)
  for b in links:
    ref2 = b['href']
    page_links.append(ref2)
  page_links = page_links[:-1]

  for page in page_links:
    url3 = page
    result3 = requests.get(url3) 
     
    # Creating soap object
    soup3 = BeautifulSoup(result3.text,'lxml') 

    questions = soup3.find_all("div", {"class": "question-main"})

    inners = soup3.find_all("div", {"class": "question-inner"})

    
    for i,j in zip(questions,inners):
      k= i.get_text()
      l = '\n'
      m = j.get_text()
      final_q = k+l+m
      the_q = []    
      the_q.append(final_q)
      got_q.append(the_q)

#print(got_q)
#print(len(got_q))
with open('numberSystemQuestions.txt', 'w', encoding="utf-8") as f:
     for sublist in got_q:
          line = "{}\n".format(sublist[0])
          f.write(line)