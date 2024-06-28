#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import google.generativeai as genai
genai.configure(api_key='AIzaSyDnBVZRrktkc-gOzW-5gQqNGxDIrBUD5bI')

st.title('Analyze Image with Google Gemini')
model = genai.GenerativeModel('gemini-pro-vision')
from PIL import Image

# Kullanıcıların jpg, jpeg veya png türünde resimler yüklemesine izin veren bir dosya yükleme widget'ı oluşturur
resim = st.file_uploader("Bir resim seç", type=(['jpg', 'jpeg', 'png']))

if resim is not None:
    img = Image.open(resim)
    st.image(img)
soru = st.text_input('Soru')
if st.button('soru sor'):
    response = Image1_generate_content([soru, img], stream=True)
    response.resolve()
    st.write(response.text)


# In[ ]:




