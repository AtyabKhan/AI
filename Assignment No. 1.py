#!/usr/bin/env python
# coding: utf-8

# In[34]:


name="atyab"
para="python, is a good programming language! Programming in python is very easy" 


# In[8]:


#capitalize function
test = para.capitalize()

print (test)


# In[12]:


#casefold function
test = para.casefold()

print(test)


# In[13]:


#center function
test = name.center(50)

print(test)


# In[21]:


#count function
oper = para.count("python")

print(oper)


# In[24]:


#encode function
oper = name.encode()

print(oper)


# In[27]:


#endswith function
oper = para.endswith("y")

print(oper)


# In[32]:


#expand tabs function
newtext="P\ty\tt\th\to\tn"
oper =  newtext.expandtabs(10)
print(oper)


# In[39]:


#find function
oper = para.find("good")

print(oper)


# In[49]:


#format function
pricetext = "You can get this software solution for only {price:.2f} dollars!"
print(pricetext.format(price = 950))


# In[44]:


oper = para.index("good")

print(oper)


# In[51]:


oper = name.isalnum()

print(oper)


# In[52]:


numberstring="9513574826"
oper = numberstring.isdecimal()

print(oper)


# In[54]:


oper = numberstring.isdigit()

print(oper)


# In[56]:


oper = name.isidentifier()

print(oper)


# In[57]:


oper = name.islower()

print(oper)


# In[59]:


oper = numberstring.isnumeric()

print(oper)


# In[61]:


oper = name.isprintable()

print(oper)


# In[63]:


oper = para.isspace()

print(oper)


# In[64]:


oper = para.istitle()

print(oper)


# In[65]:


oper = name.isupper()

print(oper)


# In[70]:


newtuple=("Hamza","Mansoor","Arsalan")
oper = "< >".join(newtuple)

print(oper)


# In[75]:


oper = name.ljust(3)

print(oper, "is my name.")


# In[76]:


textupper="HELLO"
oper = textupper.lower()

print(oper)


# In[77]:


sub="computer"
oper = sub.lstrip()

print("of all subjects", oper, "is my favorite")


# In[88]:


oper = para.partition("good")

print(oper)


# In[80]:


oper = sub.replace("computer", "english")

print(oper)


# In[81]:


oper = para.rfind("python")

print(oper)


# In[82]:


oper = para.rindex("python")

print(oper)


# In[84]:



oper = sub.rjust(0)

print(oper, "is my favorite subject.")


# In[86]:


oper = para.rpartition("good")

print(oper)


# In[90]:


separated="Hamza, Mansoor, Arsalan"
oper = separated.rsplit(", ")

print(oper)


# In[92]:


oper = sub.rstrip()

print("of all subjects", oper, "is my favorite")


# In[93]:


oper = para.split()

print(oper)


# In[94]:


separate_lines="python, is a good programming language! \nProgramming in python is very easy"
oper = separate_lines.splitlines()

print(oper)


# In[95]:


oper = para.startswith("python")

print(oper)


# In[96]:


oper = sub.strip()

print("of all Subjects", oper, "is my favorite")


# In[97]:


oper = name.swapcase()

print(oper)


# In[98]:


oper = name.title()

print(oper)


# In[99]:


oper = para.upper()

print(oper)


# In[103]:


oper = numberstring.zfill(15)

print(oper)

