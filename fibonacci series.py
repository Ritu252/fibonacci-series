#!/usr/bin/env python
# coding: utf-8

# In[22]:


#taking the input integer till where fibonacci seriex is required
n = int(input("enter the number:"))
a = 0
b = 1
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    print(a)
    print(b)
    i = 0
    while i<n-2:    #two of the fibonacci number already have been printed so the while loop is running till n-2
        c = a+b
        a = b
        b = c
        print(c)
        i += 1
    


# In[ ]:




