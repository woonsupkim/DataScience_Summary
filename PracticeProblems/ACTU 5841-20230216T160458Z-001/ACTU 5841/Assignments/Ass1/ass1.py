# Question 1
import random

X = list()
E = list()
Y = list()

for i in range(50):
    X.append(random.uniform(-200,200))
    E.append(random.gauss(0,20))

X_temp = list(map(lambda x: x * 0.5, X))

X_temp2 = list(map(lambda x: x + 10, X_temp))

for i in range(len(X_temp2)):
    Y.append(X_temp2[i] + E[i])

print('Y is')
print(Y)


#Question 2
import statistics
n = 50
Xavg = statistics.mean(X)
Xdelta = list()
Xdelta_sq = list()

for i in range(len(X)):
    Xdelta.append(X[i]-Xavg)

for i in range(len(Xdelta)):
    Xdelta_sq.append(Xdelta[i]**2)

Xsum = sum(Xdelta_sq)
S = 1/(n-1) * Xsum



w = list()
const = 1/((n-1)*S)
w = list(map(lambda x: x * const, Xdelta))


prod = list()
for i in range(len(w)):
    prod.append(w[i] * Y[i])
B1 = sum(prod)


Yavg = statistics.mean(Y)
B0 = Yavg - B1*Xavg


#Yhat = B0 + B1*xi
Yhat = list()
B1X = list(map(lambda x: x * B1, X))
for i in range(len(X)):
    Yhat.append(B0 + B1X[i])

print('Yhat is')
print(Yhat)


#Question 3
Yhat_delta = list()
Yhat_delta_sq = list()

for i in range(len(Yhat)):
    Yhat_delta.append(Yhat[i]-Yavg)

for i in range(len(Yhat_delta)):
    Yhat_delta_sq.append(Yhat_delta[i]**2)

RSS = sum(Yhat_delta_sq)


Ydelta = list()
Ydelta_sq = list()

for i in range(len(Y)):
    Ydelta.append(Y[i]-Yavg)

for i in range(len(Ydelta)):
    Ydelta_sq.append(Ydelta[i]**2)

TSS = sum(Ydelta_sq)


R2 = RSS/TSS

print('R2 is')
print(R2)


import turtle as t
t.Screen()
t.screensize(600,300)

#draw axis
t.color('black')
t.penup(); t.goto(-600,0); t.pendown(), t.forward(1200), t.stamp()
t.penup(); t.seth(90); t.goto(0,-600); t.pendown(), t.forward(1200), t.stamp()

#scatter plot of (Yi,Xi)
t.resizemode('user')
t.turtlesize(0.5,0.5,1)
t.shape('circle')

for i in range(len(X)):
    t.penup(); t.setposition(X[i],Y[i]); t.stamp()

#line
t.color('red')
xmin = min(X)
xmax = max(X)
ymin = min(Yhat)
ymax = max(Yhat)

x = (xmin, ymin)
y = (xmax, ymax)

t.penup()
t.goto(x)
t.pendown()
t.goto(y)

t.hideturtle()
t.done()