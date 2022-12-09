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
		self.revealed = []
		self.flagged = []
		self.opened = []
		for row in range(10):
			for col in range(10):
				self.bl.append(Fl_Button(col*50+50,row*50+50,50,50))
				self.bl[-1].callback(self.button_click)
				num += 1
				self.cords.append([row,col])
		
		Fl.scheme('plastic')
		self.resizable(self)
		self.end()
		self.randomize_bombs()
		self.numbered_tiles()
	
	def randomize_bombs(self):
		for x in range(10):
			a = random.randint(0,99)
			if self.cords[a] in self.bombs:
				a = random.randint(0,99)
				
			self.bombs.append(self.cords[a])
			self.bl[a].image(self.minepic)
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

			for y in range(len(around)):
				if around[y] in self.bombs:
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
				if position[0] != 0 or position[0] != 9:
					if position[1] != 0 or position[1] != 9:
						current_displacement = [position[0]+row,position[1]+col]
						around.append(current_displacement)
				
		return around
							
		
	
	def button_click(self,wid): 
		if Fl.event_button() == FL_LEFT_MOUSE:
			if self.cords[self.bl.index(wid)] in self.flagged:
				return None
			else:
				if wid in self.bombs:
					fl_message('you lose')
				else:
					if self.numbered.get(self.bl.index(wid)) != 0:
						wid.label(str(self.numbered.get(self.bl.index(wid))))
						wid.color(FL_BLUE)
						wid.redraw()
						self.opened.append(self.cords[self.bl.index(wid)])
						wid.deactivate()
						if len(self.opened)-len(self.bombs) == 90:
							if len(self.flagged) == 10:
								fl_message('you win')
					else:
						self.check_around_caller([self.cords[self.bl.index(wid)]])
						
	
		elif Fl.event_button() == FL_RIGHT_MOUSE:
			if self.cords[self.bl.index(wid)] in self.flagged:
				self.flagged.remove(self.cords[self.bl.index(wid)])
				wid.image(None)
				return None
			
			self.flagged.append(self.cords[self.bl.index(wid)])
			print(len(self.opened)-len(self.bombs))
			if len(self.opened)-len(self.bombs) == 90:
						if len(self.flagged) == 10:
							fl_message('you win')
			
			else:
				self.bl[self.cords.index(self.flagged[-1])].image(self.flag)
	def uncover_tiles(self,tiles):
		if len(tiles) <= 0:
			return None
		
		refer = self.bl[self.cords.index(tiles)]
		refer.color(FL_BLUE)
		refer.label('0')
		refer.deactivate()
		refer.redraw()
		self.opened.append(tiles)
		
	def check_around_caller(self,total, positions = None):
		print(total)
		if len(total) == 0:
			return None
			#self.uncover_tiles(total)
		for x in total:
			print('total')
			print(x)
			self.uncover_tiles(x)
			self.check_around(x)
		
		
	
	def check_around(self,position):
		
		found = []
		suspect = self.find_tiles_around(position)
		for x in range(len(suspect)):
			if (suspect[x][0] != -1 and suspect[x][0] != 10) and (suspect[x][1] != -1 and suspect[x][1] != 10):
				
				if suspect[x] not in self.revealed and self.numbered.get(self.cords.index(suspect[x])) == 0:
					found.append(suspect[x])
					self.revealed.append(suspect[x])
		print(found)
		self.check_around_caller(found)
		
				
app = mine(500,500,600,700,'game')
app.show()
Fl.run()
