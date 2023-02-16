"""Assignment 1 - Eric Thompson"""
# Imports---------------------------------------------------------------------------------------------------------------
import random
import turtle as t
random.seed(2)

# Generate Data---------------------------------------------------------------------------------------------------------
num_pts = range(50)

x = []
ep = []
for i in num_pts:
    x.append(random.uniform(-200, 200))
    ep.append(random.gauss(0, 400 ** .5))

y_obs = list(map(lambda a, b: 10 + .5 * a + b, x, ep))


# Linear Regression-----------------------------------------------------------------------------------------------------
def mean(a):
    return sum(a)/len(a)


# Regression
x_bar = mean(x)
y_bar = mean(y_obs)

x_diff = list(map(lambda a: (a - x_bar), x))
x_diff_y_obs = list(map(lambda a, b: a * b, x_diff, y_obs))
x_diff_sq = list(map(lambda a: a**2, x_diff))

b_1 = sum(x_diff_y_obs) / sum(x_diff_sq)
b_0 = y_bar - b_1 * x_bar
y_predict = list(map(lambda a: b_0 + b_1 * a, x))

# R squared calculation
tss = list(map(lambda a: (a - y_bar)**2, y_obs))
tss = sum(tss)

rss = list(map(lambda a: (a-y_bar)**2, y_predict))
rss = sum(rss)

r_sq = rss / tss


# Graph-----------------------------------------------------------------------------------------------------------------
# group and sort by x-values
pts = list(zip(x, y_obs, y_predict))
pts = sorted(pts, key=lambda x_small: x_small[0])

t.Screen()
t.hideturtle()
t.screensize(800, 800)

# Axis
t.color('black')
t.penup(); t.goto(-400, 0); t.pendown(); t.forward(800); t.stamp()
t.penup(); t.goto(0, -400); t.pendown(); t.setheading(90); t.forward(800); t.stamp()

# Points (observations)
t.shape('circle'); t.color('blue', ''); t.shapesize(.3, .3)
for i in num_pts:
    # x, y_obs
    t.penup(); t.goto(pts[i][0], pts[i][1]); t.stamp()

# Line
t.pencolor('red'); t.pensize(3)
# x, y_predict
t.penup(); t.goto(pts[0][0], pts[0][2]); t.pendown(); t.goto(pts[len(num_pts)-1][0], pts[len(num_pts)-1][2])

# Labels
# \u1D62 = _i
# \u0176 = Y^Hat
# \u00b2 = squared
label_1 = 'Truth: Y\u1D62 = 10 + 0.5x\u1D62 + e\u1D62'
label_2 = f'Fitted: \u0176 = {b_0:.5f} + {b_1:.5f}x'
label_3 = f'R\u00b2 = {r_sq:.5f}'

t.pencolor('blue'); t.pensize()
t.penup(); t.goto(5, 300)
t.pendown(); t.write(label_1 + '\n' +
                     label_2 + '\n' +
                     label_3,
                     font=('Arial', 12, 'italic')
                     )

t.done()
