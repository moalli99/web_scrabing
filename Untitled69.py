#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
from bs4 import BeautifulSoup


# In[17]:


url="https://books.toscrape.com/"


# In[18]:


r=requests.get(url)


# In[19]:


data_content=r.content


# In[20]:


soup=BeautifulSoup(data_content,"lxml")


# In[41]:


book_shop = soup.find_all('article, class_='product_pod')


# In[45]:


len(book_shop)


# In[88]:


rating=book_shop[2].find("p", class_="star-rating").find_all("i", calss_="icon-star")
print(len(rating))


# In[107]:


for book in book_shop:
    rating=book.find("p")["class"][1]
    book_name=book.find("h3").text   
    book_price=book.find('div',class_="product_price").find('p',class_="price_color").text.strip()
    print(f"book rating is: {rating}\nand name is:{book_name}\nand its price{book_price}\n*************")


# In[54]:





# In[ ]:




