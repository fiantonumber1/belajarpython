import matplotlib.pyplot as plt
import librosa
import numpy as np
import librosa.display

y, sr = librosa.load(librosa.ex('trumpet'))
librosa.feature.melspectrogram(y=y, sr=sr)

D = np.abs(librosa.stft(y))**2
S = librosa.feature.melspectrogram(S=D, sr=sr)

S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                    fmax=8000)


fig, ax = plt.subplots()
S_dB = librosa.power_to_db(S, ref=np.max)
img = librosa.display.specshow(S_dB, x_axis='time',
                         y_axis='mel', sr=sr,
                         fmax=8000, ax=ax)
fig.colorbar(img, ax=ax, format='%+2.0f dB')
ax.set(title='Mel-frequency spectrogram')
