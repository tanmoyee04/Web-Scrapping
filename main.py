'''scrapping a website can be done by two ways:
1. by using APIs
2. by using some tools like bs4(beautifulsoup)'''

# Step-1: importing the libraries

import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

# Step-2: get the HTML

r = requests.get(url) #to get the content of url
htmlcontent = r.content
#print(htmlcontent)

# Step-2: Parse the HTML

soup = BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())

# Step-3: HTML tree traversal

# Commonly used types of object in bs4:
#print(type(title)) # 1. Tag
#print(type(title.string)) # 2. NavigableString
#print(type(soup)) # 3. BeautifulSoup
# 4. Comment
#markup = "<p><!--This is a comment--!></p>"
#soup2 = BeautifulSoup(markup)
#print(type(soup2.p.string))

#Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

#print(soup.find('p')) #get the first para
#print(soup.find('p')['class']) #get the classes in parra

# Find all the elements with class lead
#print(soup.find_all("p",class_="lead"))

# Get the text from tags/soup
#print(soup.find('p').get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
#print(anchors)

all_links = set()
# Get all the links on the page
'''for link in anchors:
    if link.get('href')!='#':
        linktext = "https://www.codewithharry.com"+link.get('href')
        all_links.add(link)
        print(linktext)'''

navbarSupportedContent = soup.find(id='navbarSupportedContent')
# .contents - A tags childern are available as a list
# .children - A tags childern are available as a list

#for item in navbarSupportedContent.strings:
#    print(item)

#for item in navbarSupportedContent.stripped_strings:
#    print(item)

#print(navbarSupportedContent.parent.prettify())
#print(navbarSupportedContent.parents) #creates a generator. i.e we can iterate over

#for item in navbarSupportedContent.parents:
#    print(item.name)
#print(navbarSupportedContent.next_sibling)

#print(navbarSupportedContent.previous_sibling.prettify())

#ele = soup.select('#loginModal') #ID of the loginModal class '#' for ID and '.' for class
#print(ele)

ele = soup.select('.modal-footer')
print(ele)