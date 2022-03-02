from turtle import Turtle
from random import randint

laura = Turtle()

laura.color("red")
laura.shape("turtle")

laura.penup()
laura.goto(-160, 100)
laura.pendown()

rick = Turtle()
rick.color("green")
rick.shape("turtle")
rick.penup()
rick.goto(-160, 70)
rick.pendown()

bob = Turtle()
bob.color("blue")
bob.shape("turtle")
bob.penup()
bob.goto(-160, 40)
bob.pendown()

jil = Turtle()
jil.color("pink")
jil.shape("turtle")
jil.penup()
jil.goto(-160, 10)
jil.pendown()


for _ in range(100):
    laura.forward(randint(1, 5))
    rick.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    jil.forward(randint(1, 5))

input("press to close")
