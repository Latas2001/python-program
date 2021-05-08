from turtle import Turtle ,Screen, mainloop
import turtle
def main():
    space=Screen()
    space.setup(450,450),space.title("Mask")
    space.bgcolor("black")

    pen=Turtle(shape="circle",visible=False)
    pen.shapesize(0.3),pen.width(5),pen.speed(1)
    pen.pu(),pen.goto(0,-70),pen.pd()

    draw_mask(pen)


def draw_mask(pen):
    pen.seth(0),pen.color("#ffffff","#eeeeee")
    for i in range(2):
        pen.fd(120),pen.circle(70,180),pen.fd(120)

    pen.pu(),pen.goto(0,-80),pen.pd()
    pen.begin_fill()
    for i in range(2):
        pen.fd(110),pen.circle(10,90),pen.fd(140)
        pen.circle(10,90),pen.fd(110)
        pen.end_fill()

    pen.pu(),pen.goto(0,-60),pen.pd(),pen.width(3)
    pen.color("#778edd","#aab9ea"),pen.begin_fill()
    for i in range(2):
        pen.fd(110),pen.lt(90),pen.fd(120)
        pen.lt(90),pen.fd(110)
    pen.end_fill()


    coor_y = -30
    for i in range(3):
        pen.pu(),pen.goto(-90,coor_y),pen.pd()
        pen.fd(180); coor_y = coor_y + 30


if __name__ == "__main__":
    main()
    mainloop()
