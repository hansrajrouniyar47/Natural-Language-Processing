#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download()


# In[ ]:


import nltk
nltk.download()


# In[1]:


import nltk
ntlk.download()


# In[2]:


import nltk
nltk.download()


# In[3]:


# task 2- import brown corpus and access data


# # Task 2- import brown corpus and access data

# In[5]:


from nltk.corpus import brown
#brown.categories()
brown.words(categories='adventure')[:10]


# In[6]:


brown.categories()


# # Task 3 - Import inaugural corpus and access data

# In[7]:


from nltk.corpus import inaugural
inaugural.fileids()


# In[8]:


inaugural.words(fileids='2013-Obama.txt')[:50]


# ## homework: import webtext corpus and access data
# ## homework: frequency distribution of words in a text

# In[12]:


textsample1='Gautam Buddha was the founder of the Buddhism religion. He was born in the ruling house of Kapilvastu, at Lumbini located at the foothills of Nepal in 566 B.C'

fd=nltk.FreqDist(textsample1.split())
fd


# # Task 6 Conditional frequency distribution of words in a text

# In[14]:


from nltk.probability import ConditionalFreqDist
cfd=ConditionalFreqDist((len(word),word) for word in textsample1.split())
cfd[4]


# In[15]:


cfd[10]


# In[16]:


cfd[8]


# In[19]:


cfd[6]
cfd[3]


# # homework to determine frequency distribution and conditional frequency distribution of the President inaugural address

# In[25]:


sampletext2=inaugural.words(fileids='2013-Obama.txt')
fd1=nltk.FreqDist(inaugural.words(fileids='2013-Obama.txt'))
fd1


# In[ ]:


from nltk.probability import ConditionalFreqDist
cfc=ConditionalFreqDist((len(word),word) for word in sampletext2)
cfc[5]


# In[4]:


cfc[3]


# In[8]:


from nltk.probability import ConditionalFreqDist

cfd=ConditionalFreqDist((len(word),word)for word in inaugural.words(fileids= '2013-Obama.txt'))


# In[ ]:





# In[9]:


from nltk.probability import ConditionalFreqDist

cfd=ConditionalFreqDist((len(word),word)for word in inaugural.words(fileids= '2013-Obama.txt'))


# In[ ]:




