
# coding: utf-8

# In[1]:

import pymongo


# In[2]:

from scrape_mars import *


# In[4]:

from flask import Flask, render_template 


# In[9]:

from flask.ext.pymongo import PyMongo


# In[10]:

app = Flask(__name__)


# In[11]:

app.config["MONGO_DBNAME"] = "mars_data"


# In[12]:

app.config["MONGO_URI"] = "mongodb://user:password@ds151558.mlab.com:51558/mars_data"


# In[14]:

mongo = PyMongo(app)


# In[ ]:

@app.route("/scrape")
def add(): 
    mars_data = mongo.db.mars_data
    mars_data.insert(scrape()) 
    return "scrapeData"

@app.route("/")
def index(): 
    mars_data = mongo.db.mars_data
    return render_template("index.html", news_title = mars_data.find_one({},{"latest_news_title":1})["latest_news_title"], current_weather = mars_data.find_one({},{"mars_weather":1})["mars_weather"], image_link1= mars_data.find_one({},{"mars_images":1})["mars_images"]["Cerberus Hemisphere Enhanced"], image_link2= mars_data.find_one({},{"mars_images":1})["mars_images"]["Schiaparelli Hemisphere Enhanced"], image_link3= mars_data.find_one({},{"mars_images":1})["mars_images"]["Syrtis Major Hemisphere Enhanced"], image_link4= mars_data.find_one({},{"mars_images":1})["mars_images"]["Valles Marineris Hemisphere Enhanced"], feature_image= mars_data.find_one({},{"feature_image":1})["feature_image"], news_content = mars_data.find_one({},{"latest_news_content":1})["latest_news_content"], mars_facts = mars_data.find_one({},{"mars_facts":1})["mars_facts"])


# In[ ]:

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=9999, debug=True)


# In[ ]:




# In[ ]:



