import matplotlib.pyplot as plt
import librosa.display

AUDIO_PATH = 'music/2019CDSF总决赛A组拉丁舞决赛斗牛现场用曲.mp3'
music, sr = librosa.load(AUDIO_PATH)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(music, sr=sr)

plt.show()