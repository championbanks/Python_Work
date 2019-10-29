from bs4 import BeautifulSoup

import requests as req

import pandas as pd

import re





class ScrapeSpace:

    ''' object used to scrape certain sites '''

    def __init__(self, *args, **kwargs):

        self.urls = kwargs

        self.collection = {}



    def config_bs(self, url):

        return BeautifulSoup(url, 'lxml')



    def pull_url(self, url, insert):

        return url.format(insert)



    def scrape(self):

        try:

            if 'https://mars.nasa.gov/' in self.urls['url1']:

                url1 = req.get(self.urls['url1']).text

                soup = self.config_bs(url1)

                news_title = soup.select_one('.content_title').get_text(strip=True)

                news_p = soup.select_one('.rollover_description_inner').get_text(strip=True)

                self.collection['news_title'] = news_title

                self.collection['news_p'] = news_p



            if 'https://www.jpl.nasa.gov/' in self.urls['url2']:

                url2 = req.get(self.urls['url2']).text

                soup = self.config_bs(url2)

                image_url = soup.select_one('.carousel_item')['style']

                strip = re.findall("url\('(.*?)'\)", image_url)[0]

                featured_image_url = f'https://www.jpl.nasa.gov{strip}'

                self.collection['featured_image_url'] = featured_image_url



            if 'https://twitter.com/' in self.urls['url3']:

                url3 = req.get(self.urls['url3']).text

                soup = self.config_bs(url3)

                tweets = soup.find_all("p", class_="tweet-text")

                for tweet in tweets:

                    if tweet.text.partition(' ')[0] == 'Sol':

                        mars_weather = tweet.text

                        break

                self.collection['mars_weather'] = mars_weather



            if 'http://space-facts.com/' in self.urls['url4']:

                url4 = self.urls['url4']

                df = pd.read_html(url4, attrs={'id': 'tablepress-mars'})[0]

                df = df.set_index(0).rename(columns={1: "value"})

                del df.index.name

                mars_facts = df.to_html(justify='left')

                self.collection['mars_facts'] = mars_facts



            if 'https://astrogeology.usgs.gov/' in self.urls['url5']:

                url5 = req.get(self.urls['url5']).text

                img_url = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/{}_enhanced.tif/full.jpg"

                soup = self.config_bs(url5)

                title = soup.find_all('h3')

                first_img = self.pull_url(img_url, title[0].text.split(' ')[0].lower())

                second_img = self.pull_url(img_url, title[1].text.split(' ')[0].lower())

                third_img = self.pull_url(img_url, title[2].text.split(' ')[0].lower() + "_" + title[2].text.split(' ')[1].lower())

                fourth_img = self.pull_url(img_url, title[3].text.split(' ')[0].lower() + "_" + title[3].text.split(' ')[1].lower())

                hemisphere_image_urls = [

                    {'title': title[0].text, 'img_url': first_img},

                    {'title': title[1].text, 'img_url': second_img},

                    {'title': title[2].text, 'img_url': third_img},

                    {'title': title[3].text, 'img_url': fourth_img}

                ]

                self.collection['hemisphere_image_urls'] = hemisphere_image_urls



            return self.collection

        except TimeoutError:

            self.collection['error'] = 'Sorry, but the scraper is currently pinging the F out.'

            return self.collection