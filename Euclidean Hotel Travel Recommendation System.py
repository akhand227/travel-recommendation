#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[1]:


import pandas as pd
from pandas import read_csv
from math import sqrt
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean,cosine


# # Loading the dataset

# Overall rating for several hotels by various tourists.

# In[2]:


hotel_ratings = pd.read_csv('dset - Sheet1.csv',index_col=0)
hotel_ratings
ratings = pd.read_csv('dset - Sheet1.csv',index_col=0)
ratings = pd.DataFrame(ratings)
ratings


# This dataset provides us with every traveller's overall rating of the following hotels.  

# ## Aim

# 1. Find similar travellers based on user recommendations. 
# 2. Provide the user with hotel recommendations from travelers most similar to user.
# 3. Similarity between user and other travellers is calculated based on common user reviews (Eucledian distance function).

# ## Exploring the dataset

# Finding null values

# In[3]:


hotel_ratings.isna().sum(), sum(hotel_ratings.isna().sum())


# This provides us with missing values from each column. In total 87 missing values

# Null values in the dataset is supposed to be interpreted as 0.

# In[4]:


hotel_ratings.info()


# No need for data type conversion as all values are float.

# Replacing null values with zero

# In[5]:


hotel_ratings=hotel_ratings.fillna(0)


# Now there are no null values. 

# In[6]:


hotel_ratings.isna().sum(), sum(hotel_ratings.isna().sum())


# Let's take a look at the hotels

# In[7]:


hotel_ratings.columns


# # Recommendation System

# Essentially we want to recommend new hotels based on eucledian distance of one traveller from another. To be precise we’ll look at a measure of the dissimilarity or distance between hotels, as well as a direct measurement of similarity. We shall then see how such measures can be used to suggest items in recommender systems.

# In[8]:


def distance(p1,p2):
  distance = euclidean(p1,p2)
  return distance


# In[9]:


hotel_names = list(hotel_ratings.columns)
hotel_names


# In[10]:


customer_names = list(hotel_ratings.index)
customer_names


# In[14]:


hotel = hotel_ratings.fillna(0)
hotel


# In[17]:


def similar_to(traveller):
  person = hotel.loc[traveller]
  closest_distance=float('inf')
  closest_person=''
  for other_person in hotel.itertuples():
    if other_person.Index==traveller:
      continue
    distance_to_other_person = distance(person,hotel.loc[other_person.Index])
    if distance_to_other_person < closest_distance:
      closest_distance = distance_to_other_person
      closest_person = other_person.Index
  return closest_person, closest_distance


# Now that we have a most similar function, we can find the distsnce between two users. For instance:

# In[20]:


similar_to('Stevie Herbert')


# We can further check manually if Stevie is the most similar person to Sana Orozco (in terms of assigning travel ratings).

# Both of them have assigned similar rating to similar hotels. This can be due to a common element both of them value within hotels. 

# Now that we have the most similar person (Sana) to the assigned user (Stevie). We can find their travel suggestions. 

# In[41]:


print(ratings.at['Sana Orozco','Ascott Limited']),
print(ratings.at['Sana Orozco','Jinjiang International']),
print(ratings.at['Sana Orozco','Hilton Worldwide']),
print(ratings.at['Sana Orozco','Tokyo Inn']),
print(ratings.at['Sana Orozco','Banyan Tree Holdings']),
print(ratings.at['Sana Orozco','Huazhu Hotels Group']),
print(ratings.at['Sana Orozco','Shangri-La Hotels and Resorts']),
print(ratings.at['Sana Orozco','Heritage Hotels'])


# Based on this, Stevie being most similar to Sana Orozco should try staying at Ascott Limited. 
