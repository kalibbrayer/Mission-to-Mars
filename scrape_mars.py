from splinter import Browser
from bs4 import BeautifulSoup

def scrape():
    
   executable_path = {'executable_path': 'chromedriver'}

   browser = Browser('chrome', **executable_path, headless=False)
    
   scrapeData = {}
   
   url = "https://mars.nasa.gov/news/?page=0&per_page=15&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

   browser.visit(url)

   html = browser.html
   
   soup = BeautifulSoup(html, 'html.parser')

   content = soup.find('div', class_='article_teaser_body').get_text()

   title = soup.find('div', class_='content_title').get_text()

   scrapeData["latest_news_title"] = title
   
   scrapeData["latest_news_content"] = content

   url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

   browser.visit(url)

   html = browser.html
   
   soup = BeautifulSoup(html, 'html.parser')

   feature_image = "https://www.jpl.nasa.gov" + soup.find('a', class_='button fancybox')['data-fancybox-href']
   
   scrapeData["feature_image"] = feature_image
   
   url = "https://twitter.com/marswxreport?lang=en"

   browser.visit(url)

   html = browser.html
   
   soup = BeautifulSoup(html, 'html.parser')

   mars_weather = soup.find(class_='js-tweet-text-container').find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
   
   scrapeData["mars_weather"] = mars_weather
   
   url = "https://space-facts.com/mars/"

   browser.visit(url)

   html = browser.html

   soup = BeautifulSoup(html, 'html.parser')

   table = soup.find(id="tablepress-mars")

   import pandas as pd 

   df = pd.read_html(str(table))

   df = df[0]

   mars_facts = pd.Series(df[1].values, index = df[0]).to_dict() 
   
   scrapeData["mars_facts"] = mars_facts
   
   url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

   browser.visit(url)

   html = browser.html
   
   soup = BeautifulSoup(html, 'html.parser')

   mars_links = []

   img_links = soup.select("div.description")

   for i in img_links:
       url = "https://astrogeology.usgs.gov" + i.find("a",class_="itemLink")["href"]
       mars_links.append(url)

   mars_images = {}

   for link in mars_links:
       browser.visit(link)
       html = browser.html
       soup = BeautifulSoup(html, 'html.parser')
       img_url = "https://astrogeology.usgs.gov" + soup.find(class_="wide-image")["src"]
       hemisphere_title = browser.title.split("|")[0][:-1]
       mars_images[hemisphere_title] = img_url 
       
   scrapeData["mars_images"] = mars_images
   
   return scrapeData

