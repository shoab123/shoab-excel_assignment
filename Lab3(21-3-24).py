#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 13800
# 2000*6: 12000
#     500*3:1500
#     100*3:300
    
print("hello")


# In[ ]:





# In[22]:


ch=input("Enter a character:")
if(ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    print("It's a alphabet")
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o'or ch=='u')or(ch=='A' or ch=='E' or ch=='I' or ch=='O'or ch=='U'):
        print("It's a vowel")
    else:
        print("It's not a vowel")
else:
    print("It's not alphabet!")


# In[24]:


# Ternary operator

# Q1>
num=int(input("Enter a number:"))
result="Even"if num%2==0 else "Odd"
print(result)


# In[27]:


#Q2
salary=float(input("Enter salary:"))
exp=int(input("Enter expeience:"))
rs= salary*20/100 if exp>=15 else salary*10/100
print(rs)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




