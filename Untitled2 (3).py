#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  # Load the pandas library
cars = pd.read_csv("cars.csv")  # Read the cars.csv file
# Show the first 5 rows of only the odd-numbered columns (0, 2, 4, ...)
odd_columns = cars.iloc[:, ::2]  # Get every second column starting from the first
print(odd_columns.head())  # Show the first 5 rows


# In[2]:


#part b the Model is 'Mazda RX4'
mazda_rx4 = cars.loc[cars['Model'] == 'Mazda RX4']
print(mazda_rx4)


# In[3]:


#part c the model is 'Camaro Z28'
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]


# In[4]:


#part d
# set a tuple of specific car models to filter
models = ('Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic')
# filter rows where 'Model' is one of the models in the tuple, and select relevant columns
cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]


# In[ ]:




