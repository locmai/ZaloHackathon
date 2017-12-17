
# coding: utf-8

# In[1]:


import pandas as pd
import json
import sklearn
from sklearn.decomposition import NMF
import numpy as np
import _pickle as cPickle


# In[68]:


f = open('zmp3_log/xaa')
print('Opened File')
# f = open('data/xaa')
songs = pd.read_excel('ZMP3_Data_Zalo_Hackathon.xlsx', dtype=np.str)
genres = list(songs.genre.unique())
albums = list(songs.album.unique())
composers = list(songs.composers.unique())
artists = list(songs.artists.unique())


# In[54]:


users = {}
# print(songs['id'])
with open('zmp3_log/xaa') as f:
    for l in f:
        # print(l)
        tokens = l.split('\t')
        song_id = tokens[1]
        user_id = tokens[0]
        detail = users.get(user_id, {})
        
        data = songs.loc[songs['id'] == song_id]
        if len(data) > 0:
            print('data')
            if tokens[4] != 'null\n' and float(tokens[4])!=0:
                time = float(tokens[3])/float(tokens[4])
            else:
                time = 1

            for genre in data.genre:
                genre_key = 'genre_' + str(genre)
                genre_time = detail.get(genre_key, 0)
                genre_time += time
                detail[genre_key] = genre_time

            author = str(data.composers.unique()[0])
            if author != 'nan':
                author_key = 'author_' + str(author)
                author_time = detail.get(author_key, 0)
                author_time += time
                detail[author_key] = author_time

            artist = str(data.artists.unique()[0])
            if artist:
                artist_key = 'artist_' + str(artist)
                artist_time = detail.get(artist_key, 0)
                artist_time += time
                detail[artist_key] = artist_time

            album = str(data.album.unique()[0])
            if album:
                album_key = 'album_' + str(album)
                album_time = detail.get(album_key, 0)
                album_time += time
                detail[album_key] = album_time

            users[user_id] = detail


# In[74]:
print("Done calculate")

m_genre = []
m_composer = []
m_album = []
m_artist = []
users_id = []

for user, data in users.items():
    users_id.append(user)
    user_genre = [0] * len(genres)
    user_album = [0] * len(albums)
    user_author = [0] * len(composers)
    user_artist = [0] * len(artists)
    
    for k,v in data.items():
        keys = k.split('_')
        t = keys[0]
        if t == 'genre':
            user_genre[genres.index(keys[1])] = v
        elif t == 'author':
            user_author[composers.index(keys[1])] = v
        elif t == 'artist':
            user_artist[artists.index(keys[1])] = v
        elif t == 'album':
            # print(keys[1])
            user_album[albums.index(keys[1])] = v
    
    # print(user_genre)
    m_genre.append(user_genre)
    m_composer.append(user_author)
    m_album.append(user_album)
    m_artist.append(user_artist)


print('Done Computing')
# In[72]:
file_genre = open(b'm_genre.obj','wb')
cPickle.dump(m_genre,file_genre)

file_composer = open(b'm_composer.obj','wb')
cPickle.dump(m_composer,file_composer)

file_album = open(b'm_album.obj','wb')
cPickle.dump(m_album,file_album)


file_artist = open(b'm_artist.obj','wb')
cPickle.dump(m_artist,file_artist)

print('Done')


# In[ ]:




