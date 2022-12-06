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
				
			around = self.find_tiles_around(self.cords[x])
			'''
						#         above the button              1 left above the button                  1 right above the button                 left to the button
			around = [[self.cords[x][0]+1,self.cords[x][1]],[self.cords[x][0]+1,self.cords[x][1]-1],[self.cords[x][0]+1,self.cords[x][1]+1],[self.cords[x][0],self.cords[x][1]-1]
			      # right to the button                    below the button                     1 left below the button                  1 right below the button
			,[self.cords[x][0],self.cords[x][1]+1],[self.cords[x][0]-1,self.cords[x][1]],[self.cords[x][0]-1,self.cords[x][1]-1],[self.cords[x][0]-1,self.cords[x][1]+1]]
			
			
			for surrounding in around:
				if surrounding in self.bombs:
					bombs += 1
			print('around -------------------')	
			print(around)
			print('around -------------------')

			print('bombs -----------------')
			print(self.bombs)
			print('bombs -----------------')
			'''
			
			for x in range(len(around)):
				if around[x] in self.bombs:
					bombs += 1
			
			self.numbered[x] = bombs
		
		print(self.numbered)
	
	def find_tiles_around(self,position):
		around = []
		'''
		around = [[self.cords[position][0]+1,self.cords[position][1]],[self.cords[position][0]+1,self.cords[position][1]-1],[self.cords[position][0]+1,self.cords[position][1]+1],[self.cords[position][0],self.cords[position][1]-1]
			      # right to the button                    below the button                     1 left below the button                  1 right below the button
		,[self.cords[position][0],self.cords[position][1]+1],[self.cords[position][0]-1,self.cords[position][1]],[self.cords[x][0]-1,self.cords[position][1]-1],[self.cords[position][0]-1,self.cords[position][1]+1]]
		'''
		for row in range(-1,2):
			for col in range(-1,2):
				current_displacement = [position[0]+row,position[1]+col]
				if 0<= current_displacement[0] <= 99 and 0<= current_displacement[1] <= 99:
					around.append(current_displacement)
				
		return around
							
		
	
	def button_click(self,wid):
		if wid in self.bombs:
			fl_message('you lose')
		else:
			if self.numbered.get(wid) != 0:
				if self.numbered.get(self.bl.index(wid)) == 0:
					self.check_around_caller(self.cords[self.bl.index(wid)],self.cords[self.bl.index(wid)])
				else:
					wid.label(str(self.numbered.get(self.bl.index(wid))))
					wid.deactivate()
	
	def uncover_tiles(self,tiles):
		if len(tiles) > 0:
			for x in range(len(tiles)):
				self.bl[self.cords.index(tiles[x])].label('0')
				self.bl[self.cords.index(tiles[x])].deactivate()
		win.redraw()
		print(tiles)
		
	def check_around_caller(self,total, positions = None):
		
		around = self.find_tiles_around(total)
		
		if len(total) >= 0:
			self.uncover_tiles(total)
			#self.uncover_tiles(total)
		for x in around:
			self.check_around(x)
		
		
	
	def check_around(self,positions):
		found = []
		for x in range(len(positions)):
			
			if self.numbered.get(self.cords.index(positions[x])) == 0:
				found.append(positions[x])
		print(found)
		return found
		
				
app = mine(500,500,600,700,'game')
app.show()
Fl.run()
