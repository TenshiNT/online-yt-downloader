import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog
from streamlit_player import st_player

st.set_page_config(page_title="Online youtube video downloader", page_icon="💻", layout="wide")

root = tk.Tk()
root.withdraw()

root.wm_attributes('-topmost', 1)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

username = os.getlogin()

lottie_done = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_pktj8ecn.json")
lottie_youtube = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_NI497MPlTg.json")

with st.container():
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        st_lottie(lottie_youtube, height=100)
    with right_column1:
        st.title('Online youtube MP4 downloader')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Paste youtube URL here: ")
        user_input = st.text_input(label="")

with st.container():
    left_column2, right_clumn2 = st.columns(2)

if len(user_input) > 0:
    if user_input[0:29] == 'https://www.youtube.com/watch':

        
        link = user_input
        yt = YouTube(link)
        title = str(yt.title) + '.mp4'
        
        with st.container():
            st.header("Title: " + yt.title)
        with right_column:
            button0 = st.button
            
            if button0('Download'):
                path = filedialog.askdirectory(master=root)
                yd = yt.streams.get_highest_resolution()
                yd.download(path)
                
                # st_lottie(lottie_done)
            
        with left_column:
            st_player(link)
            
    else:
        st.error('Enter correct youtube URL')

