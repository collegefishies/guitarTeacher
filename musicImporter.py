'''
	A single class that takes in a guitar tab file and outputs a single format of *unique* note/chord identifiers over time.
'''
import music21 as m21
import pymusicxml
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

                for chord_note in note.pitches:
                    pitch = chord_note.ps
                    volume = note.volume.realized
                    score.append([start, duration, pitch, volume, instrument])

            else:
                start = note.offset
                duration = note.quarterLength
                pitch = note.pitch.ps
                volume = note.volume.realized
                score.append([start, duration, pitch, volume, instrument])

    score = sorted(score, key=lambda x: (x[0], x[2]))
    return score

# xml_data = m21.converter.parse(fn)
# xml_list = xml_to_list(xml_data)

# df = pd.DataFrame(xml_list[:9], columns=['Start', 'End', 'Pitch', 'Velocity', 'Instrument'])
# html = df.to_html(index=False, float_format='%.2f', max_rows=8)
# ipd.HTML(html)


class musicImporter():
	convertedMusic = None

	def returnMusic(self):
		return self.convertedMusic

	def importMIDI(self, filename):
		pass
		# import mido
		# self.midifile = mido.MidiFile(filename)
		# print(self.midifile)
	def importMusicXML(self, filename):
		'''
			#Citations
			##pymusicxml
			See https://github.com/MarcTheSpark/pymusicxml
			and SCAMP http://scamp.marcevanstein.com/narrative/experienced_setup.html
			## music21
			See https://www.audiolabs-erlangen.de/resources/MIR/FMP/C1/C1S2_MusicXML.html
		'''
		xml_list = xml_to_list(filename)
		df = pd.DataFrame(xml_list, columns=['start', 'duration','pitch','velocity','instrument'])
		self.convertedMusic = df

def importMIDI():
	dont_think_twice = 'music/dont_think_twice/dont_think_twice.mid'
	mI = musicImporter()
	midi = mI.importMIDI(dont_think_twice)
	print(midi[0])

def importMusicXML():
	dont_think_twice = 'music/dont_think_twice/dont_think_twice.xml'
	mI = musicImporter()
	mI.importMusicXML(dont_think_twice)
	print(mI.returnMusic())

if __name__ == '__main__':
	importMIDI()
	importMusicXML()