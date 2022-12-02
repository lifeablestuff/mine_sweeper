from fltk import *
import random

class mine(Fl_Window):
	def __init__(self,x,y,w,h,l=None):
		super().__init__(x,y,w,h,l)
		self.begin
		self.bl = []
		self.bombs = []
		self.numbered = {}
		self.cords = []
		self.flag = Fl_PNG_Image('flag.png').copy(50,50)
		self.minepic=Fl_JPEG_Image('bomb.jpg').copy(50,50)
		
		for row in range(10):
			for col in range(10):
				self.bl.append(Fl_Button(row*50+50,col*50+50,50,50))
				self.bl[-1].callback(self.button_click)
				self.cords.append([row,col])
				
		
		Fl.scheme('gtk+')
		self.resizable(self)
		self.end()
		self.randomize_bombs()
		self.numbered_tiles()
	
	def randomize_bombs(self):
		for x in range(10):
			a = random.randint(1,100)
			self.bombs.append(self.bl[a])
		
	def numbered_tiles(self):
		bombs = 0
		for x in range(len(self.bl)):
			if self.bl[x] in self.bombs:
				continue
			else:
				# right side
				if self.cords[x][1] == 10:
					# if top right
					if self.cords[x][0] == 0:
						if self.bl[x-1] in self.bombs:
							bombs += 1
						if self.bl[x+10] in self.bombs:
							bombs += 1
						if self.bl[x+9] in self.bombs:
							bombs += 1
					# if bottom right
					elif self.cords[x][0] == 10:
						if self.bl[x-1] in self.bombs:
							bombs += 1
						if self.bl[x-10] in self.bombs:
							bombs += 1
						if self.bl[x-11] in self.bombs:
							bombs += 1
					else:
						if self.bl[x-1] in self.bombs:
							bombs += 1
						if self.bl[x-10] in self.bombs:
							bombs += 1
						if self.bl[x-9] in self.bombs:
							bombs += 1
						if self.bl[x+10] in self.bombs:
							bombs += 1
						if self.bl[x+9] in self.bombs:
							bombs += 1
				# top side
				elif self.cords[x][0] == 0:
					# if top left
					if self.cords[x][1] == 0:
						if self.bl[x+10] in self.bombs:
							bombs += 1
						if self.bl[x+11] in self.bombs:
							bombs += 1
						if self.bl[x+1] in self.bombs:
							bombs += 1
							
					else:
						if self.bl[x-1] in self.bombs:
							bombs += 1
						if self.bl[x+1] in self.bombs:
							bombs += 1
						if self.bl[x+9] in self.bombs:
							bombs += 1
						if self.bl[x+10] in self.bombs:
							bombs += 1
						if self.bl[x+11] in self.bombs:
							bombs += 1
				# left side
				elif self.cords[x][1] == 0:
					if self.cords[x][0] == 0:
						if self.bl[x+10] in self.bombs:
							bombs += 1
						if self.bl[x+1] in self.bombs:
							bombs += 1
						if self.bl[x+11] in self.bombs:
							bombs += 1
					# if bottom left
					elif self.cords[x][0] == 10:
						if self.bl[x-10] in self.bombs:
							bombs += 1
						if self.bl[x-9] in self.bombs:
							bombs += 1
						if self.bl[x+1] in self.bombs:
							bombs += 1
					
					else:
						if self.bl[x-1] in self.bombs:
							bombs += 1
						if self.bl[x+1] in self.bombs:
							bombs += 1
						if self.bl[x+9] in self.bombs:
							bombs += 1
						if self.bl[x+10] in self.bombs:
							bombs += 1
						if self.bl[x+11] in self.bombs:
							bombs += 1
				
				# bottom side
				elif self.cords[x][0] == 10:
					if self.bl[x+1] in self.bombs:
						bombs += 1
					if self.bl[x-1] in self.bombs:
						bombs += 1
					if self.bl[x-11] in self.bombs:
						bombs += 1
					if self.bl[x-10] in self.bombs:
						bombs += 1
					if self.bl[x-9] in self.bombs:
						bombs += 1
				
				# if anywhere else in grid
				else:
					if self.bl[x+1] in self.bombs:
						bombs += 1
					if self.bl[x-1] in self.bombs:
						bombs += 1
					if self.bl[x-11] in self.bombs:
						bombs += 1
					if self.bl[x-10] in self.bombs:
						bombs += 1
					if self.bl[x-9] in self.bombs:
						bombs += 1
					if self.bl[x+9] in self.bombs:
						bombs += 1
					if self.bl[x+10] in self.bombs:
						bombs += 1
					if self.bl[x+11] in self.bombs:
						bombs += 1
		
			self.numbered[x] = bombs
		print(self.numbered)
							
		
	
	def button_click(self,wid):
		if wid in self.bombs:
			fl_message('you lose')
		
				
app = mine(500,500,600,700,'game')
app.show()
Fl.run()
