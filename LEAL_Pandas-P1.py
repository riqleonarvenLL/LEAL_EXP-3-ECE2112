#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  # Import the pandas library
# Load the CSV file into a  named 'cars'
cars = pd.read_csv("cars.csv")
# Concatenate the first 5 and last 5 rows
p1 = pd.concat([cars.head(), cars.tail()])
# Display the result
print(p1)


# In[ ]:




