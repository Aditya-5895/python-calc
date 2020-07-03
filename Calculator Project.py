#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
run=True
prev=0
def domath():
    global run 
    global prev
    if prev==0:
        eq=input("Enter your equation")
    else:
        eq=input(str(prev))
    if eq=='quit':
        run=False
        print("Good bye Human.")
    else:
        eq=re.sub('[a-zA-Z,:" "]','',eq)
        if prev==0:
            prev=eval(eq)
        else:
            prev=eval(str(prev)+eq)
while run:
    domath()


# In[ ]:




