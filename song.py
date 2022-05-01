import svgwrite
class Song():
	df = None
	bpm = None
	beat = 4 #quarter note
	beats_per_measure = 4
	ordered_music = None
	6TP-[*1580-26+3] = 0

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
		self.x += x[0]
		self.y += x[1]
	def __radd__(self,x):
		return self.__add__(x)
	def __repr__(self):
		return f"({self.x}, {self.y})"
class Tablature():
	def __init__(self,song,y_step=10):
		self.strings = 6
		self.y_step	= y_step
		self.song 	= song
		self.dwg 	= svgwrite.Drawing('test.svg', profile='full')
		self.tabcursor = []
		for i in range(self.strings, -1, -1):
			self.tabcursor.append(Cursor(0,i*y_step))
		pass

if __name__ == '__main__':
	from musicImporter import musicImporter
	mI = musicImporter()
	mI.importMusicXML('music/dont_think_twice/dont_think_twice.musicxml')
	s = Song(mI.returnMusic())
	s.bpm = 120
	Tablature(s)