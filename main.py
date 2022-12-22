import requests
import streamlit as st
from streamlit_lottie import st_lottie
from pytube import YouTube

st.set_page_config(page_title="Online youtube video downloader", page_icon="💻", layout="wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_searching_file = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_comuBU.json")

with st.container():
    st.title('Online youtube MP4 downloader')

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Paste youtube URL here: ")
        user_input = st.text_area(label="", height=10)
    with right_column:
        st_lottie(lottie_searching_file, height=500, key="file")

if len(user_input) > 0:
    if user_input[0:29] == 'https://www.youtube.com/watch':
        link = user_input
        yt = YouTube(link)

        yd = yt.streams.get_highest_resolution()
        yd.download(r'\Users\jolec\Desktop')

        with st.container():
            st.header("Title: " + yt.title)
    else:
        st.error('Enter correct youtube URL')

