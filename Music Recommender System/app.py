import streamlit as st
import pickle as pk
import pandas as pd


def recommendation(name):
    idx = songs[songs['song'] == name].index[0]
    distances = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])
    
    song = []
    for m_id in distances[1:11]:
        song.append(songs.iloc[m_id[0]].song)
        
    return song
songs_dict=pk.load(open('songs_dict.pkl','rb'))
songs=pd.DataFrame(songs_dict)

similarity=pk.load(open('similarity.pkl','rb'))

st.title('Music Recommender System:Made by Pratham')
selected_song_name=st.selectbox(
'What Music recommendation do you want',
songs['song'].values    
)

if st.button('Recommend Songs'):
    recommendation=recommendation(selected_song_name)
    for i in recommendation:
        st.write(i)