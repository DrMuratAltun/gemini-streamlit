#!/usr/bin/env python
# coding: utf-8

# ### Google Gemini

# ![image.png](attachment:image.png)

# In[1]:


#pip install google-generativeai


# In[3]:


import streamlit as st
import google.generativeai as genai
genai.configure(api_key='AIzaSyDnBVZRrktkc-gOzW-5gQqNGxDIrBUD5bI')


# In[4]:


st.title=('Chat with Me')
model=genai.GenerativeModel('gemini-1.5-pro-latest')
chat=model.start_chat(history=[])


# In[5]:


soru=st.text_input('You:')
if st.button('sor'):
    response=chat.send_message(soru)
    st.write(response.text)
    st.write(chat.history)


# In[ ]:




