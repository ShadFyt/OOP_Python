from shapes import Paper, Triangle, Rectangle, Oval


paper = Paper()

rect1 = Rectangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()

rect2 = Rectangle()

rect2.set_width(300)
rect2.set_height(100)
rect2.set_color("red")
rect2.set_x(100)
rect2.set_y(50)
rect2.draw()


paper.display()
