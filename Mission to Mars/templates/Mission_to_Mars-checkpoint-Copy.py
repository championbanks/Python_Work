#!/usr/bin/env python
# coding: utf-8

# <h2>Life Expectancy Data</h2>
# <p>Estimated life expectancy data is acquired from the CDC website using API requests.
# The API is of type SODA (Socrata Open Data API).</p>
# 
# <h3>CDC Description</h3>
# <p>This dataset includes estimates of U.S. life expectancy at birth by state 
# and census tract for the period 2010-2015. Estimates were produced for 65,662 census tracts, 
# covering the District of Columbia (D.C.) and all states, excluding Maine and Wisconsin, 
# representing 88.7% of all U.S. census tracts (see notes). 
# These estimates are the result of the collaborative project, 
# “U.S. Small-area Life Expectancy Estimates Project (USALEEP),” 
# between the National Center for Health Statistics (NCHS), the National Association for 
# Public Health Statistics and Information Systems (NAPHSIS), 
# and the Robert Wood Johnson Foundation (RWJF).</p> 

# In[516]:


import requests
import json
from splinter import Browser
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from flask import Flask, render_template


# In[435]:


driver = webdriver.Chrome("chromedriver")
driver.get("https://mars.nasa.gov/news/8522/nasas-curiosity-rover-finds-an-ancient-oasis-on-mars")
driver.get("https://mars.nasa.gov/msl/mission-updates/sols-2564-2566-the-early-rover-gets-the-frost/?mu=sols-2564-2566-the-early-rover-gets-the-frost")


# In[288]:


content = driver.page_source
soup = bs(content)


# In[289]:


news_title=[]
news_p =[]


# In[290]:


page = requests.get("https://mars.nasa.gov/news/8522/nasas-curiosity-rover-finds-an-ancient-oasis-on-mars")
page2 = requests.get("https://mars.nasa.gov/msl/mission-updates/sols-2564-2566-the-early-rover-gets-the-frost/?mu=sols-2564-2566-the-early-rover-gets-the-frost")


# In[291]:


page.status_code
#page.content
page2.status_code
#page2.content


# In[292]:


soup = bs(page.content, 'html.parser')
soup2 = bs(page2.content, 'html.parser')
print(soup2.prettify())


# In[293]:


list(soup.children)
list(soup2.children)
[type(item) for item in list(soup.children)]
[type(item) for item in list(soup2.children)]


# In[294]:


soup = bs(page.content, 'html.parser')
news_title  = soup.find_all('title')
soup.find_all('title')[0].get_text()

soup2 = bs(page2.content, 'html.parser')
news_title2  = soup2.find_all('title')
soup2.find('title').get_text()
# print(title)

news_title = soup.title.text
news_Paragraph = soup.body.p.text

news_title = soup2.title.text
news_paragraph = soup2.body.p.text


# In[295]:


get_ipython().system('which chromedriver')


# In[366]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

#driver = webdriver.Chrome("chromedriver")
#driver.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
#Img = requests.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[383]:


# Iterate through all pages
for x in range(50):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup3 = bs(html, 'html.parser')
    soup3.content
print(soup3.prettify())    


# In[420]:


featured_image_url = []
img = soup3.find_all('img')
for i in img:
    if (i['alt']) == "Lyot Crater Dunes":
        featured_image_url.append(i['src'])
        print(i['alt'])
featured_image_url 
#print(img['scr'])    


# In[429]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[446]:


for x in range(50):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup4 = bs(html, 'html.parser')
    soup4.content
print(soup3.prettify())


# In[456]:


mars_weather = soup4.find_all("p")[5].get_text()
mars_weather 
#mars_weather  = soup4.body.find_all('p')[5].get_text()
#mars_weather 


# In[457]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[458]:


for x in range(50):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup5 = bs(html, 'html.parser')
    soup5.content
print(soup3.prettify())


# In[462]:


soup4.find_all('a')


# In[507]:


hemisphere_image_urls = []
links = soup5.find_all('img', class_="thumb" )
for i in links:
        hemisphere_image_urls.append(f"Title : {(i['alt'])}")
        hemisphere_image_urls.append(f"Url : {(i['src'])}")

hemisphere_image_urls
#print(img['scr']) 


# In[ ]:


get_ipython().system(' ')

