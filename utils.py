import streamlit as st
import pickle 
import pandas
#import h5py

# Load the data and convert it to pandas dataframe
def load_data():
    try:
        with open('data.pkl', 'rb') as file:
            data = pickle.load(file)
            data = pandas.DataFrame(data)
            return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None


# similarity fuction
def Tv_show_similarity():
    try:
        with open('similarity_score.pkl', 'rb') as file:
            score = pickle.load(file)
            return score
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    