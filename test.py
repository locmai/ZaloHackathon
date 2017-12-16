# %matplotlib inline
import seaborn
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import sklearn, pandas
import librosa, librosa.display
plt.rcParams['figure.figsize'] = (14, 5)


filename = 'test.mp3'
x_brahms, sr_brahms = librosa.load(filename, duration=180)

n_mfcc = 12
mfcc_brahms = librosa.feature.mfcc(x_brahms, sr=sr_brahms, n_mfcc=n_mfcc).T
print(mfcc_brahms)