import librosa
import numpy as np

#Design principles
#y represents audio_buffer
#sr represents smpling_rate

filename = librosa.util.example_audio_file()
print(filename)
#Conventions
y, sr = librosa.load(filename, offset=0.0, duration=20.0)
duration_seconds = float(len(y)) / sr
print(duration_seconds, len(y))

#Package organization
#core.load core.resample core.to_mono core.autocorrelate core.zero_crossings

#Spectral features
spectrogram = np.abs(librosa.stft(y))
melspec = librosa.feature.melspectrogram(y=y, sr=sr)
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
tonnetz = librosa.feature.tonnetz(y=y, sr=sr)

#Display
#display.waveplot display.specshow

#Onsets, tempo, and beats

#Structural analysis

#Decompositions

#Effects

#Output

#Caching


