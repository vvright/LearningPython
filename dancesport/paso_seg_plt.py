import matplotlib.pyplot as plt
import librosa.display
import numpy as np
from pydub import AudioSegment

SECOND = 1000
AUDIO_PATH = 'music/'
AUDIO_NAME = '2019CDSF总决赛A组拉丁舞决赛斗牛现场用曲.mp3'

print(AUDIO_PATH + AUDIO_NAME)

def split_music(begin, end, file_path, file_name):
    song = AudioSegment.from_mp3(file_path + file_name)
    song = song[begin * SECOND: end * SECOND]

    temp_path = 'backup/' + file_name + '_' + str(begin) + '_' + str(end)
    song.export(temp_path)

    return temp_path

music, sr = librosa.load(split_music(0, 3, AUDIO_PATH, AUDIO_NAME))

plt.figure(figsize=(14, 5))
librosa.display.waveplot(music, sr=sr)
plt.show()
