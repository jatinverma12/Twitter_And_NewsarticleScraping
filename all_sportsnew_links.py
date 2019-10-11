#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[1]:


def Ancestors (a,k,url):
    try:
        if a[1:7]=="sports":
            k.append(url+a)
    except TypeError:
        print("Not your fault")
    return k
import json
import requests
from bs4 import BeautifulSoup as s
url="https://www.bhaskar.com/sports/72"
data=requests.get(url)

file='''
{   
    "urls":[]
}
'''

soup=s(data.text,'html.parser')
b=[]
for i in soup.find_all('a'):
    b=Ancestors(i.get('href'),b,url)
text=json.loads(file)

for i in b:
    text['urls'].append(i)



with open("all_sportsnews_urls.json",'w') as f:
    json.dump(text,f,indent=2)


# In[ ]:


pip install bs4


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
