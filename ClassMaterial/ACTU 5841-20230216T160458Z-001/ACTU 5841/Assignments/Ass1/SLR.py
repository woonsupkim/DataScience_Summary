##############################################################
### Assignment 1
### Prepared By: Woon Kim
### UNI: wk2371
### Course: ACTU 5841
### Date: January 27 2022

# Question 1
print("Question 1")
import random

X = list()
E = list()
Y = list()

for i in range(50):
    X.append(random.uniform(-200,200))
    E.append(random.gauss(0,20))

print('X: ', X)

#performing 0.5*X on all elements of X
X_temp = list(map(lambda x: x * 0.5, X))

#performing 0.5*X + 10 on all elements of X
X_temp2 = list(map(lambda x: x + 10, X_temp))

#performing X + E for each elements of the vectors
for i in range(len(X_temp2)):
    Y.append(X_temp2[i] + E[i])

print('Y: ', Y)

###########################################################################
print("\n\n Question 2")
#Question 2
import statistics

Xdelta = list()
Xdelta_sq = list()
Xavg = statistics.mean(X)
n = 50

#computing X - Xbar
for i in range(len(X)):
    Xdelta.append(X[i]-Xavg)

#computing (X-Xbar)^2
for i in range(len(Xdelta)):
    Xdelta_sq.append(Xdelta[i]**2)

#computing the summation
Xsum = sum(Xdelta_sq)

#computing Sx^2
S = 1/(n-1) * Xsum
print('Sx^2: ', S)



w = list()
#computing the denominator of w (the constant value)
const = 1/((n-1)*S)

#using Xdelta that was calculated before
w = list(map(lambda x: x * const, Xdelta))
print('wi: ', w)


prod = list()
#computing the product of each elements of w and Y
for i in range(len(w)):
    prod.append(w[i] * Y[i])
B1 = sum(prod)
print('B1: ', B1)


Yavg = statistics.mean(Y)
B0 = Yavg - B1*Xavg
print('B0: ', B0)


#Yhat = B0 + B1*xi
Yhat = list()

#computing B1 * xi
B1X = list(map(lambda x: x * B1, X))

for i in range(len(X)):
    Yhat.append(B0 + B1X[i])

print('Yhat: ', Yhat)



###########################################################################
print("\n\n Question 3")
#Question 3
#Question 3
Yhat_delta = list()
Yhat_delta_sq = list()

#computing RSS
#compute Yhat - Ybar
for i in range(len(Yhat)):
    Yhat_delta.append(Yhat[i]-Yavg)

#compute (Yhat - Ybar)^2
for i in range(len(Yhat_delta)):
    Yhat_delta_sq.append(Yhat_delta[i]**2)

RSS = sum(Yhat_delta_sq)
print('RSS: ', RSS)


#computing TSS
Ydelta = list()
Ydelta_sq = list()

#compute Y - Ybar
for i in range(len(Y)):
    Ydelta.append(Y[i]-Yavg)

#compute (Y - Ybar)^2
for i in range(len(Ydelta)):
    Ydelta_sq.append(Ydelta[i]**2)

TSS = sum(Ydelta_sq)
print('TSS: ', TSS)


R2 = RSS/TSS
print('R2: ', R2)


###########################################################################
print("\n\n Question 2-3 Verification")

import csv
with open('sanity_check.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',)
    writer.writerow(['X'] + X)
    writer.writerow(['Y'] + Y)
    writer.writerow(['B0', B0, 'B1', B1, 'R2', R2])

print("intercept() on excel produces the same result as B0")
print("slope() on excel produces the same result as B1")
print("rsq() on excel produces the same result as R2")


###########################################################################
print("\n\n Question 4")
#Question 4
X.sort()
Y.sort()

import turtle as t

t.TurtleScreen._RUNNING=True
turtle_window = t.Screen()

t.screensize(600,300)

#draw axis
t.color('black')
t.penup(); t.goto(-250,0); t.pendown(), t.forward(500), t.stamp()
t.penup(); t.seth(90); t.goto(0,-200); t.pendown(), t.forward(400), t.stamp()

#scatter plot of (Yi,Xi)
t.color('blue')
t.shapesize(0.5,0.5,0.1)
t.shape('circle')

for i in range(len(X)):
    t.penup(); t.setposition(X[i],Y[i]); t.stamp()

#line
t.color('red')
t.pensize(3)
xmin = min(X)
xmax = max(X)
ymin = min(Yhat)
ymax = max(Yhat)

p1 = (xmin, ymin)
p2 = (xmax, ymax)

t.penup()
t.goto(p1)
t.pendown()
t.goto(p2)

#Annotation
Yi = 'Y{0}'.format(chr(0x1D62))
xi = 'x{0}'.format(chr(0x1D62))
ei = 'e{0}'.format(chr(0x1D62))
R_2 = 'R{0}'.format(chr(0x00B2))
Yhat_txt = chr(0x0177)
B0_txt = str(round(B0,4))
B1_txt = str(round(B1,4))

t.penup()
t.goto(50,180)
t.color('blue')
t.write("truth: " + Yi + " = 10 + 0.5 " + xi + " + " + ei, True, align="left")
t.goto(50,167)

t.write("fitted: " + Yhat_txt + " = " + B0_txt + " + "
        + B1_txt + " x ", True, align="left")
t.goto(50,154)
R2_txt = str(round(R2,4))
t.write(R_2 + " = " + R2_txt, True, align="left")


#instruction
t.penup()
t.goto(-270,200)
t.color('red')
t.write("Click on the screen to exit", font=("Arial", 16, "normal"))

t.hideturtle()

turtle_window.exitonclick()
