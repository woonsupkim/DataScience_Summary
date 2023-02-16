#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math
import turtle as t


# In[2]:


X=[]
E=[]
for n in range (0,50):
    E.append(random.gauss(0,math.sqrt(400)))
    X.append(random.uniform(-200,200))

Y=list(map(lambda a,b:10+0.5*a + b, X, E))


# In[3]:


def Expectation(m):
    total=0
    l=len(m)
    for k in range (0,l):
        total+=m[k]*(1/l)

    return total


# In[4]:


Ybar=Expectation(Y)
Xbar=Expectation(X)


# In[5]:


xdifference=list(map(lambda a: a - Xbar,X))


# In[6]:


x_minus_y=list(map(lambda a,b: a*b, xdifference,Y ))


# In[7]:


xdifference_squared=list(map(lambda a: a**2,xdifference))


# In[8]:


b1_hat= sum(x_minus_y)/sum(xdifference_squared)


# In[9]:


b0_hat=Ybar - b1_hat*Xbar


# In[10]:


y_fitted=list(map(lambda a: b0_hat+b1_hat*a,X))


# In[11]:


tss=list(map(lambda a:(a - Ybar)**2,Y))


# In[12]:


rss=list(map(lambda a:(a-Ybar)**2,y_fitted))


# In[13]:


r_squared=sum(rss)/sum(tss)


# In[14]:


coordinates=list(zip(X,Y,y_fitted))
coordinates=sorted(coordinates, key=lambda x_min: x_min[0])


# In[ ]:


t.Screen()
t.screensize(750,750)

t.color('black')
t.penup(); t.goto(-400, 0); t.pendown(), t.forward(800), t.stamp()
t.penup(); t.seth(90); t.goto(0, -400); t.pendown(), t.forward(800), t.stamp()


t.shape('circle')
t.color('blue')
t.turtlesize(0.25,0.25,1)
for n in range(0,50):
    t.penup(); t.goto(coordinates[n][0],coordinates[n][1]); t.pendown(); t.stamp()
    

t.color('red')
t.pensize(2.5)
t.penup()
for n in range(0,50):
     t.goto(coordinates[n][0],coordinates[n][2]); t.pendown();

t.penup()
t.color('blue')
t.goto(5,300)
t.write('truth: Yᵢ = 10 + 0.5 xᵢ + eᵢ')
t.goto(5,285)
t.write(f'fitted: \u0176 = {b0_hat:.5f} + {b1_hat:.5f} X')
t.goto(5,270)
t.write(f'R² = {r_squared:.5f}')

    
    
t.hideturtle()
t.done()


# In[ ]:




