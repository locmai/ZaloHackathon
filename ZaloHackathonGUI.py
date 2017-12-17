from flask import Flask,render_template,request
import pandas as pd

songs = pd.read_excel('ZMP3_Data_Zalo_Hackathon.xlsx')
# train_data = pd.read_json('TrainData.json')
# lst_song = train_data.loc[train_data[""] == ]

app = Flask(__name__)

current_user = None

user_history = {
    "147141825": [
    "1076375432",
    "1076248654",
    "1075363598",
    "1076392737",
    "1076385159",
    "1075247103",
  ],
    "162979556": [
    "1075552268",
    "1074453544"
  ],
    "167286853": [
    "1076375432",
    "1075543318",
    "1074453544"
  ],
    "172745119": [
    "1075865810",
    "1075865770",
    "1075865773",
    "1075779900"
    ],
    "179066046": [
    "1075762346",
    "1074453544",
  ],
    "147141825": ["1076375432", "1076248654", "1076248654", "1076375432", "1075363598", "1075363598", "1076392737",
                  "1076375432", "1076385159", "1076248654", "1076375432", "1076385159", "1076392737", "1075247103",
                  "1075363598"],
    "129389288": ["1073806765", "1073800439", "1073800439", "1076386607", "1074563700", "1076332831", "1076277310",
                  "1074510541", "1074487623", "1076333351", "1075447435", "1074464028", "1076386598", "1075225659",
                  "1075447435", "1074563700", "1074464028", "1074487623", "1073806765", "1076392737", "1073800444",
                  "1073800444", "1074510541", "1073800439", "1073800439", "1076277310", "1076386599", "1076332831",
                  "1076386598", "1076333347", "1076332830", "1076333348", "1076333349", "1076386607"],
}
title = None
artists = None
composers = None
genre = None

@app.route('/')
def homepage():
    select_button = "Select User"
    list_data = []
    return render_template('home/index.html', title="Welcome to Home", list_data_sample=list_data,select_button=select_button)

@app.route('/user')
def user():
    user = request.args.get('id', default='*', type=int)
    select_button = str(user)
    history = []
    global current_user
    current_user = str(user)
    for i in user_history[str(user)]:
        #title = songs.loc[songs['id'] == 1074453544]['title']
        title = songs.loc[songs['id'] == int(i)]['title'].values[0]
        artists = songs.loc[songs['id'] == int(i)]['artists'].values[0]
        composers = songs.loc[songs['id'] == int(i)]['composers'].values[0]
        genre = songs.loc[songs['id'] == int(i)]['genre'].values[0]
        history.append([title,artists,composers,genre])
    return render_template('home/index.html', title="User History", list_data_sample=history,select_button=select_button)

@app.route('/generate')
def generate():
    global current_user
    user = request.args.get('id', default='147141825', type=int)
    max_recommend_song = 5
    recommend_song = []
    result = pd.read_json("TrainData.json")
    lst_song_id = list(result.loc[result['user_id'] == int(current_user)]['song_id'])
    for id in lst_song_id:
        recommend_users = list(result.loc[result['song_id'] == id]['user_id'])
        for recommend_user in recommend_users:
            other_user_songs = list(result.loc[result['user_id'] == recommend_user]['song_id'])
            recommend_song.extend(other_user_songs)
    return_recommend_song = set(recommend_song) - set(lst_song_id)
    return_recommend_song = list(return_recommend_song)[1:5]
    history = []

    for i in return_recommend_song:
        title = songs.loc[songs['id'] == int(i)]['title'].values[0]
        artists = songs.loc[songs['id'] == int(i)]['artists'].values[0]
        composers = songs.loc[songs['id'] == int(i)]['composers'].values[0]
        genre = songs.loc[songs['id'] == int(i)]['genre'].values[0]
        history.append([title, artists, composers, genre])
    return render_template('home/generate.html', title="User History",list_data_sample=history,select_button="Recommended Musics")

if __name__ == '__main__':
    app.run()
