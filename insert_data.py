
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
    return render_template("index.html")


# In[ ]:

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




# In[ ]:



