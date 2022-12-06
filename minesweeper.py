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
		num = 0
		for row in range(10):
			for col in range(10):
				self.bl.append(Fl_Button(col*50+50,row*50+50,50,50))
				self.bl[-1].callback(self.button_click)
				num += 1
				self.cords.append([row,col])
		
		Fl.scheme('gtk+')
		self.resizable(self)
		self.end()
		self.randomize_bombs()
		self.numbered_tiles()
	
	def randomize_bombs(self):
		for x in range(10):
			a = random.randint(0,99)
			self.bombs.append(self.cords[a])
			self.bl[a].label('bomb')
			self.redraw()
		
	def numbered_tiles(self):
		bombs = 0
		print(self.cords)
		for x in range(len(self.cords)):
			bombs = 0
			if self.cords[x] in self.bombs:
				continue 
						#         above the button              1 left above the button                  1 right above the button                 left to the button
			around = [[self.cords[x][0]+1,self.cords[x][1]],[self.cords[x][0]+1,self.cords[x][1]-1],[self.cords[x][0]+1,self.cords[x][1]+1],[self.cords[x][0],self.cords[x][1]-1]
			      # right to the button                    below the button                     1 left below the button                  1 right below the button
			,[self.cords[x][0],self.cords[x][1]+1],[self.cords[x][0]-1,self.cords[x][1]],[self.cords[x][0]-1,self.cords[x][1]-1],[self.cords[x][0]-1,self.cords[x][0]+1]]

			for surrounding in around:
				if surrounding in self.bombs:
					bombs += 1
			print('around -------------------')	
			print(around)
			print('around -------------------')

			print('bombs -----------------')
			print(self.bombs)
			print('bombs -----------------')
			self.numbered[x] = bombs
		
		print(self.numbered)
							
		
	
	def button_click(self,wid):
		if wid in self.bombs:
			fl_message('you lose')
		else:
			if self.numbered.get(wid) != 0:
				wid.label(str(self.numbered.get(self.bl.index(wid))))
				print(self.cords[self.bl.index(wid)])
				wid.deactivate()
		
		
				
app = mine(500,500,600,700,'game')
app.show()
Fl.run()
