#https://docs.python.org/3/library/turtle.html
from turtle import *
color('red', 'yellow')
begin_fill()
for x in range(1000000):
    if x == 3: break
    forward(200)
end_fill()
done()