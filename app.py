
import streamlit as st
import pandas as pd
#import pickle 
import numpy as np
from utils import load_data, Tv_show_similarity
from api.api import fetch_image_path

# Load the dataframe and saved array
df = load_data()
similarity_score = Tv_show_similarity()

# Function to recommend similar TV shows based on tv id
def show_similarity(series):
    try:
        series_index = df[df['name'] == series].index[0]
        similarity = similarity_score[series_index]
        five_similar = sorted(list(enumerate(similarity)), reverse=True, key= lambda x: x[1])[1:6]

        recommended_tv_shows = []
        recommended_posters = []
        for i, score in five_similar:
            #
            tv_ids = df.loc[i]['id']
            recommended_tv_shows.append(df.loc[i]['name'])
            recommended_posters.append(fetch_image_path(tv_ids))
        return recommended_tv_shows, recommended_posters
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

# The title for the webpage
st.title("Tv Shows Reocommending Model")


selected_tvshow = st.selectbox("Select a TV Show", df['name'])

if st.button('Recommendation'):
        names, posters = show_similarity(selected_tvshow)
        for i in names:
            #st.write(i)

            col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.markdown(f"#### {names[0]}")  # Use H3 for smaller text
            st.image(posters[0])

        with col2:
            st.markdown(f"#### {names[1]}")  # Use H3 for smaller text
            st.image(posters[1])

        with col3:
            st.markdown(f"#### {names[2]}")  # Use H3 for smaller text
            st.image(posters[2])

        with col4:
            st.markdown(f"#### {names[3]}")  # Use H3 for smaller text
            st.image(posters[3])

        with col5:
            st.markdown(f"#### {names[4]}")  # Use H3 for smaller text
            st.image(posters[4])

