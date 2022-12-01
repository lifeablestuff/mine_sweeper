from fltk import *
import random

class mine(Fl_Window):
	def __init__(self,x,y,w,h,l=None):
		super().__init__(x,y,w,h,l)
		self.begin
		self.bl = []
		self.bombs = []
		self.numbered = {}
		for row in range(10):
			for col in range(10):
				self.bl.append(Fl_Button(row*50+50,col*50+50,50,50))
				self.bl[-1].callback(self.button_click)
		
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
			if self.bl[x] in bombs:
				continue
			else:
				try:
					if self.bl[x+1] in bombs:
						bombs.append(self.bl[x+1])
					if self.bl[x-1] in bombs:
						bombs.append(self.bl[x-1])
					if self.bl[x-11] in bombs:
						bombs.append(self.bl[x-11])
					if self.bl[x-10] in bombs:
						bombs.append(self.bl[x-10])
					if self.bl[x-9] in bombs:
						bombs.append(self.bl[x-9])
					if self.bl[x+9] in bombs:
						bombs.append(self.bl[x+9])
					if self.bl[x+10] in bombs:
						bombs.append(self.bl[x+10])
					if self.bl[x+11] in bombs:
						bombs.append(self.bl[x+10])
				except:
					print('')
			if len(bombs) == 0:
				self.numbered[bl[x]] = 0
		print(self.numbered)
		
	
	def button_click(self,wid):
		if wid in self.bombs:
			fl_message('you lose')
		
				
app = mine(500,500,600,700,'game')
app.show()
Fl.run()
