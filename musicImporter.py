'''
	
	A single class that takes in a guitar tab file and outputs a single format
	of *unique* note/chord identifiers, frets, and strings over time.

	MusicXML has the fingering and fretting, so that is the best method of import
'''
import os
import pandas as pd
import IPython.display as ipd


def xml_to_list(xml):
	"""Convert a music xml file to a list of note events

	Notebook: C1/C1S2_MusicXML.ipynb

	Args:
		xml (str or music21.stream.Score): Either a path to a music xml file or a music21.stream.Score

	Returns:
		score (list): A list of note events where each note is specified as
			``[start, duration, pitch, velocity, label]``
	"""
	import music21 as m21

	if isinstance(xml, str):
		xml_data = m21.converter.parse(xml)
	elif isinstance(xml, m21.stream.Score):
		xml_data = xml
	else:
		raise RuntimeError('midi must be a path to a midi file or music21.stream.Score')

	score = []

	for part in xml_data.parts:
		instrument = part.getInstrument().instrumentName

		for note in part.flat.notes:
			if note.isChord:
				start = note.offset
				duration = note.quarterLength
				articulations = note.articulations
				strings = articulations[0::2]
				frets = articulations[1::2]
				for chord_note,string,fret in zip(note.pitches,strings,frets):
					pitch = chord_note.ps
					volume = note.volume.realized
					score.append([start, duration, pitch, volume, instrument,string.number, fret.number])

			else:
				start = note.offset
				duration = note.quarterLength
				pitch = note.pitch.ps
				volume = note.volume.realized
				string = note.articulations[0].number
				fret = note.articulations[1].number
				score.append([start, duration, pitch, volume, instrument, string, fret])

	score = sorted(score, key=lambda x: (x[0], x[2]))
	return score

class musicImporter():
	convertedMusic = None

	def returnMusic(self):
		return self.convertedMusic

	def importMIDI(self, filename):
		import pretty_midi
		midi_data = pretty_midi.PrettyMIDI(filename)
		midi_list = []
		for instrument in midi_data.instruments:
			for note in instrument.notes:
				start = note.start
				end = note.end
				pitch = note.pitch,
				velocity = note.velocity
				midi_list.append([start, end, pitch, velocity, instrument.name])
		midi_list = sorted(midi_list, key=lambda x: (x[0], x[2]))
		df = pd.DataFrame(midi_list, columns=['start', 'end','pitch','velocity','instrument'])
		self.convertedMusic = df
	def importMusicXML(self, filename):
		'''
			Returns MusicXML file as a pandas dataframe
			#Citations
			##pymusicxml
			See https://github.com/MarcTheSpark/pymusicxml
			and SCAMP http://scamp.marcevanstein.com/narrative/experienced_setup.html
			## music21
			See https://www.audiolabs-erlangen.de/resources/MIR/FMP/C1/C1S2_MusicXML.html
		'''
		xml_list = xml_to_list(filename)
		# print(xml_list)
		df = pd.DataFrame(xml_list, columns=['start', 'duration','pitch','velocity','instrument','string','fret'])
		self.convertedMusic = df

def importMIDI():
	dont_think_twice = 'music/dont_think_twice/dont_think_twice.mid'
	mI = musicImporter()
	mI.importMIDI(dont_think_twice)
	# print(mI.returnMusic())
def importMusicXML():
	dont_think_twice = 'music/dont_think_twice/dont_think_twice.musicxml'
	mI = musicImporter()
	mI.importMusicXML(dont_think_twice)
	print(mI.returnMusic())

if __name__ == '__main__':
	#test import
	importMIDI()
	importMusicXML()