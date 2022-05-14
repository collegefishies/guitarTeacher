import svgwrite
from svgwrite.shapes import Line
class Song():
	df = None
	bpm = None
	beat = 4 #quarter note
	beats_per_measure = 4
	ordered_music = None

	def __init__(self, df):
		self.df = df
		self._orderMusic()

	def _orderMusic(self):
		self.ordered_music = list(self.df.groupby('start'))
	def pop(self):
		'''Remove element from the beginning of the list.'''
		notes = self.ordered_music[self._index]
		if self._index < len(self.ordered_music):
			self._index += 1
			return notes
		else:
			return None
	def rewind(self):
		self._index = 0

class Cursor():
	x = None
	y = None
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __assign__(self,x):
		self.x = x[0]
		self.y = y[0]
	def __add__(self, x):
		return Cursor(self.x + x[0], self.y + x[1])
	def __radd__(self,x):
		return self.__add__(x)
	def __repr__(self):
		return f"({self.x}, {self.y})"
	def __truediv__(self, a):
		return Cursor(self.x/a, self.y/a)
	def __iter__(self):
		return (self.x, self.y).__iter__()

class Tablature():
	def __init__(self,song,y_step=10):
		self.strings = 6
		self.y_step	= y_step
		self.song 	= song
		self.dwg 	= svgwrite.Drawing('test.svg', profile='full')
		self.tabcursor = []
		self.step = Cursor(10,0)
		print(tuple(Cursor(10,0)))
		for i in range(self.strings, -1, -1):
			self.tabcursor.append(Cursor(0,i*y_step))
	def newCursor(step):
		newcursor = self.tabcursor
		for i in range(self.strings + 1):
			newcursor[i] = self.tabcursor[i] + self.step
		return newcursor

	def addChord(self, chord_df):
		#add lines
		nc = self.newCursor(self.step)
		oc = self.tabcursor
		for i in range(1, self.strings + 1):
			l 
		l = Line(oc[i],nc[i])
		pass



if __name__ == '__main__':
	from musicImporter import musicImporter
	mI = musicImporter()
	mI.importMusicXML('music/dont_think_twice/dont_think_twice.musicxml')
	s = Song(mI.returnMusic())
	s.bpm = 120
	Tablature(s)