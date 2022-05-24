class Ball():

	def __init__ (self,canvas,x1,y1,x2,y2,colour,x_vel,y_vel,elasticity):
		import time
		self.canvas=canvas
		self.x1=x1
		self.y1=y1
		self.x_vel=x_vel
		self.y_vel=y_vel
		self.elasticity=elasticity
		self.initial_time=time.time()

		self.image = canvas.create_oval(x1,y1,x2,y2,fill=colour)

	def Ball_prop(self,vel,angle):
		import math
		ang = ((2*math.pi)/360)*angle
		self.x_vel=vel*math.cos(ang)
		self.y_vel=vel*math.sin(ang)
		print(self.x_vel)

	def move(self):
		self.canvas.move(self.image,self.x_vel,-self.y_vel)

	def gravity(self,accleration,drag):
		coordinates_r=self.canvas.coords(self.image)

		import time
		now = time.time()
		dt = now - self.initial_time
		self.initial_time = now

		time_s = time.time() - self.initial_time
		self.y_vel = self.y_vel + accleration*dt
		if self.y_vel < 0:
			if coordinates_r[3] > self.canvas.winfo_height():
				time_f=time.time()-self.initial_time
				ran=self.x_vel*dt 
				self.y_vel=0
				self.x_vel=0
			
				

		self.canvas.move(self.image,self.x_vel,-self.y_vel)


