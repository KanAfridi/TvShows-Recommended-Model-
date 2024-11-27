
import streamlit as st
import pandas as pd
import pickle 
import numpy as np
from utils import load_data, Tv_show_similarity

# Load the dataframe
df = load_data()

# Load the saved array
similarity_score = Tv_show_similarity()


def show_similarity(series):
    try:
        series_index = df[df['name'] == series].index[0]
        similarity = similarity_score[series_index]
        five_similar = sorted(list(enumerate(similarity)), reverse=True, key= lambda x: x[1])[1:6]

        recommended_tv_shows = []
        for i, score in five_similar:
            recommended_tv_shows.append(df.loc[i]['name'])
        return recommended_tv_shows
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

# The title for the webpage
st.title("Tv Shows Reocommending Model")


selected_tvshow = st.selectbox("Select a TV Show", df['name'])

if st.button('Recommendation'):
        similar_tvshow = show_similarity(selected_tvshow)
        for i in similar_tvshow:
            st.write(i)

