import librosa 
import matplotlib.pyplot as plt 

audio=r"D:\Python\Projects\Github\awesome-python-projects\Python_Projects\audio.mp3"

x,sr= librosa.load(audio)
X=librosa.stft(x)
xdb= librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(10,5))
librosa.display.specshow(xdb, sr = sr , x_axis= 'time', y_axis= 'hz')
plt.colorbar()
plt.title('Spectrogram of '+ audio)
plt.show()

