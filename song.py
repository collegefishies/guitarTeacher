
class Song():
	df = None
	bpm = None
	beat = 1/4
	beats_per_measure = 4
	ordered_music = None

	def __init__(self, df):
		self.df = df

	def _orderMusic(self):
		print(self.df)
		pass
