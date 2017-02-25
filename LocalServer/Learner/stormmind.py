import turtle
import math


def draw_box():
	inner = turtle.Turtle()
	inner.towards(0,0)
	inner.speed("fastest")
	inner.color('#e6e6e6')
	inner.shape('turtle')
	for k in range(0, 36):
		inner.circle(50)
		inner.left(10)

	middle = turtle.Turtle()
	middle.towards(0,0)
	middle.speed("fastest")
	middle.color('#ff9933')
	middle.shape('turtle')
	for i in range(0, 9):
		middle.goto(0,0)
		middle.forward(150)
		middle.left(40)
		for k in range(0, 36):
			middle.circle(25)
			middle.left(10)

	outter = turtle.Turtle()
	outter.towards(0,0)
	outter.speed("fastest")
	outter.color('#33ff33')
	outter.shape('turtle')
	outter.left(20)
	for i in range(0, 9):
		outter.goto(0,0)
		outter.forward(math.sqrt(2)*100 + math.sqrt(pow(5,5)))
		outter.left(40)
		for k in range(0, 36):
			outter.circle(12.5)
			outter.left(10)

window = turtle.Screen()
window.bgcolor("black")
draw_box()
window.exitonclick()




