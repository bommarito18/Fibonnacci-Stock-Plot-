#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Libraries
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import numpy as np
plt.style.use('seaborn-pastel')


# In[23]:


stock = input("Enter Ticker: ")


# In[24]:


#OHLC Moving Average Data
stock = web.DataReader(stock, data_source='yahoo', start='2015-01-01')

stock = stock.dropna()
stock


# In[25]:


#Calculate the max and min close price
maximum_price = stock['Close'].max()
minimum_price = stock['Close'].min()
difference = maximum_price - minimum_price #Get the difference        
first_level = maximum_price - difference * 0.236   
second_level = maximum_price - difference * 0.382  
third_level = maximum_price - difference * 0.5     
fourth_level = maximum_price - difference * 0.618 


# In[26]:


#Print the price at each level
print("Level Percentage\t", "Price ($)")
print("00.0%\t\t", maximum_price)
print("23.6%\t\t", first_level)
print("38.2%\t\t", second_level)
print("50.0%\t\t", third_level)
print("61.8%\t\t", fourth_level)
print("100.0%\t\t", minimum_price)


# In[27]:


new_stock = stock
plt.figure(figsize=(16,8))
plt.title('Fibonnacci Retracement Plot')
plt.plot(new_stock.index, new_stock['Close'])
plt.axhline(maximum_price, linestyle='--', alpha=0.5, color = 'red')
plt.axhline(first_level, linestyle='--', alpha=0.5, color = 'orange')
plt.axhline(second_level, linestyle='--', alpha=0.5, color = 'yellow')
plt.axhline(third_level, linestyle='--', alpha=0.5, color = 'green')
plt.axhline(fourth_level, linestyle='--', alpha=0.5, color = 'blue')
plt.axhline(minimum_price, linestyle='--', alpha=0.5, color = 'purple')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price in USD',fontsize=18)
plt.show()


# In[28]:


#Create another plot of the Fibonacci levels along with the close price with the levels filled in by color
new_stock = stock
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(1,1,1)
plt.title('Fibonnacci Plot')
plt.plot(new_stock.index, new_stock['Close'], color='black')
plt.axhline(maximum_price, linestyle='--', alpha=0.5, color = 'red')
ax.fill_between(new_stock.index, maximum_price, first_level, color = 'red')
plt.axhline(first_level, linestyle='--', alpha=0.5, color = 'orange')
ax.fill_between(new_stock.index, first_level, second_level, color = 'orange')
plt.axhline(second_level, linestyle='--', alpha=0.5, color = 'yellow')
ax.fill_between(new_stock.index, second_level, third_level, color = 'yellow')
plt.axhline(third_level, linestyle='--', alpha=0.5, color = 'green')
ax.fill_between(new_stock.index, third_level, fourth_level, color = 'green')
plt.axhline(fourth_level, linestyle='--', alpha=0.5, color = 'blue')
ax.fill_between(new_stock.index, fourth_level, minimum_price, color = 'blue')
plt.axhline(minimum_price, linestyle='--', alpha=0.5, color = 'purple')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price ($)',fontsize=18)
plt.show()


# In[ ]:




