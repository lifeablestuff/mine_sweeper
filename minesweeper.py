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
		# randomizing the bomb locations
		for x in range(10):
			a = random.randint(0,99)
			if self.cords[a] in self.bombs:
				a = random.randint(0,99)
			self.bombs.append(self.cords[a])
			self.redraw()
		
	def numbered_tiles(self):
		# assigns the number of bombs around tile to the tile in a dictionary
		bombs = 0
		for x in range(len(self.cords)):
			bombs = 0
			if self.cords[x] in self.bombs:
				continue 
				
			around = self.find_tiles_around(self.cords[x])


			for y in range(len(around)):
				if around[y] in self.bombs:
					bombs += 1
			
			self.numbered[x] = bombs

	
	def find_tiles_around(self,position):
		around = []
		# returns all cordinates around a given cordinate
		for row in range(-1,2):
			for col in range(-1,2):
				if position[0] != 0 or position[0] != 9:
					if position[1] != 0 or position[1] != 9:
						current_displacement = [position[0]+row,position[1]+col]
						around.append(current_displacement)
				
		return around
							
		
	
	def button_click(self,wid): 
		# reveal event
		if Fl.event_button() == FL_LEFT_MOUSE:
			if self.cords[self.bl.index(wid)] in self.flagged:
				return None
			else:
				if self.cords[self.bl.index(wid)] in self.bombs:
					
					
					for x in self.bombs:
						self.bl[self.cords.index(x)].image(self.minepic)
						self.redraw()
					
					for x in self.flagged:
						if x not in self.bombs:
							self.bl[self.cords.index(x)].label('x')
							self.bl[self.cords.index(x)].labelcolor(FL_RED)
							self.bl[self.cords.index(x)].image(None)
						else:
							self.bl[self.cords.index(x)].image(self.flag)
					self.redraw()
					fl_message('you lose')
				else:
					if self.numbered.get(self.bl.index(wid)) != 0:
						self.uncover_tiles(self.cords[self.bl.index(wid)])
						# prevent clicking already revealed tile
						wid.deactivate()
						# checking if correct amount of tiles revealed and correct amount of flags placed down.
						if len(self.opened) == 90:
							if len(self.flagged) == 10:
								fl_message('you win')
					else:# if clicked on a empty tile
						self.check_around_caller([self.cords[self.bl.index(wid)]])
						
		# flag event
		elif Fl.event_button() == FL_RIGHT_MOUSE:
			if self.cords[self.bl.index(wid)] in self.flagged:
				self.flagged.remove(self.cords[self.bl.index(wid)])
				wid.image(None)
				return None
			
			self.flagged.append(self.cords[self.bl.index(wid)])

			self.bl[self.cords.index(self.flagged[-1])].image(self.flag)
			if len(self.opened) == 90:
						if len(self.flagged) == 10:
							fl_message('you win')
			
			
			
	def uncover_tiles(self,tiles):
		if len(tiles) <= 0:
			return None
		# quick referance by variable
		refer = self.bl[self.cords.index(tiles)]
		dict_value = self.numbered.get(self.cords.index(tiles))
		
		if dict_value == 0:
			refer.color(0)
		elif dict_value == 1:
			refer.color(FL_BLUE)
		elif dict_value == 2:
			refer.color(FL_GREEN)
		elif dict_value == None:
			return None
			
		else:
			refer.color(FL_YELLOW)
		
		refer.label(str(dict_value))
			
		refer.deactivate()
		refer.redraw()
		# adding cleared tiles to list of opened tiles
		if tiles not in self.opened:
			self.opened.append(tiles)

		
	def check_around_caller(self,total, positions = None):
		if len(total) == 0:
			return None
		for x in total:
			# if tile is empty
			if self.numbered.get(self.cords.index(x)) == 0:
				self.check_around(x)
			self.uncover_tiles(x)
		
		
	
	def check_around(self,position):
		
		found = []
		suspect = self.find_tiles_around(position)
		for x in range(len(suspect)):
			# checking if tile cordinates are within boundaries
			if (suspect[x][0] != -1 and suspect[x][0] != 10) and (suspect[x][1] != -1 and suspect[x][1] != 10):
				
				if suspect[x] not in self.revealed and self.numbered.get(self.cords.index(suspect[x])) != None:
					found.append(suspect[x])
					self.revealed.append(suspect[x])
		
		self.check_around_caller(found)
		
				
app = mine(500,500,600,700,'game')
app.show()
Fl.run()
