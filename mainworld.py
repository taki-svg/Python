from tkinter import*
import time
import math
from objects import*


main_window = Tk()
main_window.title("GAME")
main_window.geometry("1500x800")

canvas_1 = Canvas(main_window,width=1500,height=600,bg="#9DACBE")
canvas_1.grid(row=0,column=0)


ball_1 = Ball(canvas_1,5,585,20,600,"red",0,0,1)


ball_1.Ball_prop(20,30)#(velocity and angle in degrees here)

ball_1.move()

initial_time  = time.time()

while True:
	
	ball_1.gravity(-5,0)
	main_window.update()
	time.sleep(.1)




main_window.mainloop()
