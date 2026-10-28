import turtle
import tkinter
import random

farby = ["purple", "red", "green", "blue", "brown", "yellow"]

kor = turtle.Turtle()
kor.pensize(5)

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
    for _ in range(pocet):
        if kor.xcor() + 2 * dlzka > 500:
            break

        kor.forward(dlzka)
        kor.penup()
        kor.forward(dlzka)
        kor.pendown()

def spirala(pocet: int, dlzka: int, stupen: int = 30):
    for _ in range(pocet):
        kor.forward(dlzka)
        kor.left(stupen)
        dlzka += 20


def rekurzivna_spirala(pocet: int, dlzka: int, stupen: int = 30):
    if pocet == 0:
        return

    kor.forward(dlzka)
    kor.left(stupen)
    rekurzivna_spirala(pocet - 1, dlzka + 20, stupen)


def urob_list(dlzka: int):
    kor.pencolor("green")
    kor.dot(dlzka)
    kor.pencolor("black")



def binarny_strom(dlzka: int):
    if dlzka < 25:
        urob_list(dlzka)
        return

    kor.forward(dlzka)
    kor.left(60)
    binarny_strom(random.randrange(dlzka // 2, dlzka // 3 * 2))
    kor.right(120)
    binarny_strom(random.randrange(dlzka // 2, dlzka // 3 * 2))

    kor.left(60)
    kor.backward(dlzka)


def nachystaj_sa():
    kor.left(90)
    kor.penup()
    kor.backward(500)
    kor.pendown()
    kor.speed(0)


nachystaj_sa()
binarny_strom(500)


turtle.done()
