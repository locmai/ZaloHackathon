from flask import Flask,render_template,request
import pandas as pd

songs = pd.read_excel('ZMP3_Data_Zalo_Hackathon.xlsx')

app = Flask(__name__)

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
    "1074453544"
  ],
}

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
    for i in user_history[str(user)]:
        #title = songs.loc[songs['id'] == 1074453544]['title']
        title = songs.loc[songs['id'] == int(i)]['title'].values[0]
        artists = songs.loc[songs['id'] == int(i)]['artists'].values[0]
        composers = songs.loc[songs['id'] == int(i)]['composers'].values[0]
        genre = songs.loc[songs['id'] == int(i)]['genre'].values[0]
        history.append([title,artists,composers,genre])

    return render_template('home/index.html', title="User History", list_data_sample=history,select_button=select_button)

if __name__ == '__main__':
    app.run()
