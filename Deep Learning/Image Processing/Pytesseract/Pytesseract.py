#!/usr/bin/env python
# coding: utf-8

# # Pytesseract 
# 
# -------Use cases------
# 
# 1.Retrieving information from vendor bills-Date, invoice #, amount
# 
# 2.For scanning image and convert text to another language
# 
# 3.scan image and use as narator
# 
# Nowadays people use Google API instead of Pytesseract
# 
# -------Drawback--------
# 
# Eventhough it takes care of capital / small letter and somewhat blur, we need to use white background
# 
# In some cases i saw different laungauge instead of English in the output. In some way if we cam make pytesseract to understand that we need only English, then may be accuracy would be increased
# 
# Also processing like lemetizzation can help in increasing the accuracy

# Thing to be noted:-
# 1. If the image is not clear enough, apply different filters to the image using openCv before applying pytesseract E.g.
#    if the image is tilted, try to rotate it.
# 2. Go to https://github.com/UB-Mannheim/tesseract/wiki to install tesseract
# 3. Install openCV               !pip install opencv-python 
# 4. Install Pytesseract          !pip install pytesseract

# In[6]:


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\bjoseph\AppData\Local\Tesseract-OCR\tesseract.exe"


# In[7]:


import cv2                                  #helps in reading the image
img = cv2.imread('Desktop/test_image.png')
cv2.imshow('test image', img)               #diplay the image

#The function waits for specified milliseconds for any keyboard event. 
#If you press any key in that time, the program continues. 
#If 0 is passed, it waits indefinitely for a key stroke.
cv2.waitKey(0)                             
cv2.destroyAllWindows()


# In[8]:


text = pytesseract.image_to_string(img)
print(text)


# References
# 
# https://opencv-python-tutroals.readthedocs.io/en/latest/index.html
# 
# Krish Naik Channel - https://www.youtube.com/watch?v=JW3SLBOx_xc
# 
# https://stackoverflow.com/

# In[ ]:




