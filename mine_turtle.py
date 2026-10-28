import turtle
import tkinter
import random

farby = ["purple", "red", "green", "blue", "brown", "yellow"]

kor = turtle.Turtle()

def vykresli(dlzka: int, stran: int):
    uhol = 360 / stran

    kor.begin_fill()
    farba = farby[random.randrange(len(farby))]
    kor.fillcolor(farba)
    for _ in range(stran):
        farba = farby[random.randrange(len(farby))]
        kor.color(farba)

        kor.pensize(random.randrange(2, 10))

        kor.forward(dlzka)
        kor.left(uhol)
    kor.end_fill()


def prerusovana_ciara(pocet: int, dlzka: int):
    kor.pensize(5)

    for _ in range(pocet):
        if kor.xcor() + 2 * dlzka > 500:
            break

        kor.forward(dlzka)
        kor.penup()
        kor.forward(dlzka)
        kor.pendown()

def 


prerusovana_ciara(5, 20)

turtle.done()
