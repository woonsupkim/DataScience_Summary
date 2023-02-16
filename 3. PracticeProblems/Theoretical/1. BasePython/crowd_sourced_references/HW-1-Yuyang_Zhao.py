#!/usr/bin/env python
# coding: utf-8

# ### ACTU PS5841 Data Science in Finance & Insurance

# ### Yuyang Zhao | Jan 20, 2022

# In terminal, run this file with command 'python SLR.py'

# In[1]:


# import libraries
import random
import turtle as t
import csv


# In[2]:


#generate a training set of 50 observations
n = 50
x = []
y = []

for i in range(n):
    x.append(random.uniform(-200, 200))
    ε = random.gauss(0, 20) #normal dist with mean 0 and var 400
    y.append(10 + 0.5*x[i] + ε)

#print(x)
#print(y)


# In[3]:


#method of least squares, estimate parameters
numer = 0
denom = 0

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

for i in range(n):
    numer += (x[i] - mean_x) * (y[i] - mean_y)
    denom += (x[i] - mean_x) ** 2

β1 = numer / denom
β0 = mean_y - (β1 * mean_x)

print("coefficients are \u03B2\u2080 =", β0, "\u03B2\u2081 =", β1)


# In[4]:


#fitted y
y_hat = []
for i in range(n):
    y_hat.append(β0 + β1 * x[i])
    
#print(y_hat)


# In[5]:


#the coefficient of determination R2

RSS = [] #sum squared regression 
TSS = [] #total sum of squares

for i in range(n):
    RSS.append((y_hat[i] - mean_y) ** 2)
    TSS.append((y[i] - mean_y) ** 2)

R2 = sum(RSS)/sum(TSS)
print("R\u00B2 =", R2)


# In[6]:


#for validation purposes, open a csv file and change the directory

data_list = [['x', 'y', 'y_hat']]
for i in range(n):
    data_list.append([x[i], y[i], y_hat[i]])

data_list.append(['', '', ''])

data_list.append(['intercept', 'slope', 'r_squared'])
data_list.append(['=INTERCEPT(C2:C51, A2:A51)', '=SLOPE(C2:C51, A2:A51)', '=RSQ(C2:C51, B2:B51)'])

with open('validation.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_list)

#now open the csv file and scroll down to bottom to check parameters


# In[ ]:


#Sort x first so that the turtle travels in one direction
sort = sorted((i, j) for i, j in zip(x, y))
sort_x, sort_y = zip(*sort)

#Use turtle graphics to present a scatter plot of the training set

BASEPYONLY = True
t.Screen()

# draw axis
t.color('black')
t.penup(); t.goto(-300, 0); t.pendown(), t.forward(600), t.stamp()
t.penup(); t.seth(90); t.goto(0, -300); t.pendown(), t.forward(600), t.stamp()

# common turtle attributes
t.resizemode('user') 
t.turtlesize(0.3,0.3,1) 
t.shape('circle')

#draw the random 50 observations
t.color('blue','') #pen color, fill color 
for _ in range(n):
    t.penup(); t.goto(sort_x[_], sort_y[_]); t.stamp()

# draw fitted line
t.color('red')
t.width(3)
t.penup(); t.goto(min(x), min(y_hat)); t.pendown(), t.goto(max(x), max(y_hat))

#annotate
t.color('')
t.goto(10, 200)
t.color('blue')
t.turtlesize(0.05,0.05,1) 
t.write("truth: Y\u1D62 = 10 + 0.5 x\u1D62 + \u03B5\u1D62", move=False, font=('Arial', 18, 'italic'))
t.color('')
t.goto(10, 180)
t.color('blue')
t.write("fitted: \u0177 = {} + {} x".format(round(β0,5), round(β1,5)), move=False, font=('Arial', 18, 'italic'))
t.color('')
t.goto(10, 160)
t.color('blue')
t.write("R\u00B2 : {}".format(round(R2, 5)), move=False, font=('Arial', 18, 'italic'))

#t.bye()
t.done()

