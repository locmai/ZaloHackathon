import pandas as pd
recommend_song = []
result = pd.read_json("TrainData.json")
lst_song_id = list(result.loc[result['user_id'] == user]['song_id'])
for id in lst_song_id:
    recommend_users = list(result.loc[result['song_id'] == id]['user_id'])
    for recommend_user in recommend_users:
        other_user_songs = list(result.loc[result['user_id'] == recommend_user]['song_id'])
        recommend_song.extend(other_user_songs)
return_recommend_song = set(recommend_song) - set(lst_song_id)
return_recommend_song = list(return_recommend_song)[1:10]
