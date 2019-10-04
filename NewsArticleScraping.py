#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[49]:


import json
import requests
file='''
{   
    "url":"fgds",
    "images":[],
    "caption":[],
    "content":"fbd",

    "author":"jatin",
    "title":"The epic war",
    "date":"dfs",
    "category":"sports"
}
'''
url="https://timesofindia.indiatimes.com/sports/cricket/south-africa-in-india/gavaskar-not-happy-with-team-indias-treatment-of-ashwin/articleshow/71440635.cms"
data=requests.get(url)
text=json.loads(file)
from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')
text["url"]=url
for i in soup.find_all('img'):
    text["images"].append(i.get('src'))
    text["caption"].append(i.get('title'))

text["content"]=soup.get_text()

for i in soup.find_all('span',itemprop="author"):
    text["author"]=i.get_text()

text["date"]=soup.time['datetime']
for i in soup.find_all('div',class_="Normal"):
    text["content"]=i.get_text()
    
print(json.dumps(text,indent=2))


    


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook
