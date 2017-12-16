get_ipython().magic('matplotlib inline')
import seaborn
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import sklearn, pandas
import librosa, librosa.display
plt.rcParams['figure.figsize'] = (14, 5)

filename_brahms = 'test.mp3'
x_brahms, sr_brahms = librosa.load(filename_brahms, duration=180)


librosa.display.waveplot(x_brahms, sr_brahms)

S_brahms = librosa.feature.melspectrogram(x_brahms, sr=sr_brahms)
Sdb_brahms = librosa.amplitude_to_db(S_brahms)
librosa.display.specshow(Sdb_brahms, sr=sr_brahms, x_axis='time', y_axis='mel')
plt.colorbar()
mfcc_brahms.shape
scaler = sklearn.preprocessing.StandardScaler()
mfcc_brahms_scaled = scaler.fit_transform(mfcc_brahms)
mfcc_brahms_scaled.mean(axis=0)
mfcc_brahms_scaled.std(axis=0)
mfcc_busta = librosa.feature.mfcc(x_busta, sr=sr_busta, n_mfcc=n_mfcc).T
print mfcc_brahms.shape
print mfcc_busta.shape


# Scale the resulting MFCC features to have approximately zero mean and unit variance. Re-use the scaler from above.

# In[ ]:


mfcc_busta_scaled = scaler.transform(mfcc_busta)


# Verify that the mean of the MFCCs for the second audio file is approximately equal to zero and the variance is approximately equal to one.

# In[ ]:


mfcc_busta_scaled.mean(axis=0)


# In[ ]:


mfcc_busta_scaled.std(axis=0)


# ## Train a Classifier

# Concatenate all of the scaled feature vectors into one feature table.

# In[ ]:


features = numpy.vstack((mfcc_brahms_scaled, mfcc_busta_scaled))


# In[ ]:


features.shape


# Construct a vector of ground-truth labels, where 0 refers to the first audio file, and 1 refers to the second audio file.

# In[ ]:


labels = numpy.concatenate((numpy.zeros(len(mfcc_brahms_scaled)), numpy.ones(len(mfcc_busta_scaled))))


# Create a classifer model object:

# In[ ]:


# Support Vector Machine
model = sklearn.svm.SVC()


# Train the classifier:

# In[ ]:


model.fit(features, labels)


# ## Run the Classifier

# To test the classifier, we will extract an unused 10-second segment from the earlier audio fields as test excerpts:

# In[ ]:


x_brahms_test, sr_brahms = librosa.load(filename_brahms, duration=10, offset=120)


# In[ ]:


x_busta_test, sr_busta = librosa.load(filename_busta, duration=10, offset=120)


# Listen to both of the test audio excerpts:

# In[ ]:


ipd.Audio(x_brahms_test, rate=sr_brahms)


# In[ ]:


ipd.Audio(x_busta_test, rate=sr_busta)


# Compute MFCCs from both of the test audio excerpts:

# In[ ]:


mfcc_brahms_test = librosa.feature.mfcc(x_brahms_test, sr=sr_brahms, n_mfcc=n_mfcc).T


# In[ ]:


mfcc_busta_test = librosa.feature.mfcc(x_busta_test, sr=sr_busta, n_mfcc=n_mfcc).T


# In[ ]:


print mfcc_brahms_test.shape
print mfcc_busta_test.shape


# Scale the MFCCs using the previous scaler:

# In[ ]:


mfcc_brahms_test_scaled = scaler.transform(mfcc_brahms_test)


# In[ ]:


mfcc_busta_test_scaled = scaler.transform(mfcc_busta_test)


# Concatenate all test features together:

# In[ ]:


features_test = numpy.vstack((mfcc_brahms_test_scaled, mfcc_busta_test_scaled))


# Concatenate all test labels together:

# In[ ]:


labels_test = numpy.concatenate((numpy.zeros(len(mfcc_brahms_test)), numpy.ones(len(mfcc_busta_test))))


# Compute the predicted labels:

# In[ ]:


predicted_labels = model.predict(features_test)


# Finally, compute the accuracy score of the classifier on the test data:

# In[ ]:


score = model.score(features_test, labels_test)


# In[ ]:


score


# Currently, the classifier returns one prediction for every MFCC vector in the test audio signal. Let's modify the procedure above such that the classifier returns a single prediction for a 10-second excerpt.

# In[ ]:


predicted_labels = model.predict(mfcc_brahms_test_scaled)


# In[ ]:


numpy.argmax([(predicted_labels == c).sum() for c in (0, 1)])
predicted_labels = model.predict(mfcc_busta_test_scaled)
numpy.argmax([(predicted_labels == c).sum() for c in (0, 1)])

df_brahms = pandas.DataFrame(mfcc_brahms_test_scaled)


# In[ ]:


df_brahms.shape




