import turtle

def draw_tri(var):
	for i in range(1,5):
		var.forward(150)
		var.left(120)

def draw_sq(var):
	for i in range(1,5):
		var.forward(50)
		var.left(90)

def draw_box():
	brad = turtle.Turtle()
	brad.towards(0,0)
	brad.speed("fastest")
	brad.color('black')
	brad.shape('arrow')
	for k in range(0, 36):
		draw_sq(brad)
		brad.left(10)

	peter = turtle.Turtle()
	peter.towards(0,0)
	peter.speed('fastest')
	peter.color('red')
	peter.shape('triangle')
	for j in range(1,36):
		draw_tri(peter)
		peter.left(10)



'''def draw_square():
	brad = turtle.Turtle()
	brad.speed("fastest")
	brad.color('black')
	brad.shape('arrow')
	for k in range(0, 60):
		draw_square(brad)
		brad.left(6)
'''

window = turtle.Screen()
window.bgcolor("orange")
#draw_circle()
draw_box()
window.exitonclick()
'''
def draw_circle():
	annie = turtle.Turtle()
	annie.speed("fast")
	annie.color('green')
	annie.shape('circle')
	annie.circle(150)


'''





