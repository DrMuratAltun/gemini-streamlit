#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyDnBVZRrktkc-gOzW-5gQqNGxDIrBUD5bI')

st.title('Chat with Me')
model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

soru = st.text_input('You:')

if st.button('sor'):
    response = chat.send_message(soru)
    st.write(response.text)
    st.write(chat.history)

if st.button('Yeni Sohbet'):
    chat = model.start_chat(history=chat.history)

