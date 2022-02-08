import turtle 
import random

window = turtle.Screen()
window.bgcolor('black')

# Create a turtle, named Kevin
jimmy = turtle.Turtle()
jimmy.speed(0)
#variable to show how far the turtle should travel

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
# function to draw fireworks 
def draw_firework(t):
  #distance to be moved by turtle
  distance = random.randint(5,100)
  x = random.randint(-300,300)
  y = random.randint(-300,300)

  jimmy.penup()
  jimmy.goto(x,y)
  jimmy.pendown()
  
  # TODO #1: create a variable to change the firework size then use that variable in the forward and backward methods 
  for i in range(36):
    jimmy.forward(distance)
    jimmy.backward(distance)
    jimmy.right(10)
    

# Draw five fireworks
for i in range(7):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  #TODO #2: Create three variables r, g, and b and set their values equal to a random number between 0 and 255. Replace the color blue with jimmy.color(r,g,b)
  jimmy.color(r,g,b)
  draw_firework(jimmy)
#changing turtle color to white
jimmy.color('white')
x = random.randint(-500,500)
y = random.randint(-500,500)
z = 0
while z <= 100:
  jimmy.penup()
  jimmy.goto(x,y)
  jimmy.pendown()
  for i in range(5):
    jimmy.forward(10)
    jimmy.right(144)
  z += 1
  x = random.randint(-500,500)
  y = random.randint(-500,500)
