import streamlit as st
import pandas as pd
import time
from utils import set_background
set_background("thumb.jpg")
# Global Score
if "score" not in st.session_state:
    st.session_state.score=0
if "args" not in st.session_state:
    st.session_state.args=[0,0,0,0]
st.title("Question #16")
st.divider()
# Question title
st.subheader("I find it hard to understand why some people can do their work without AI.",text_alignment="center")
#st.markdown(st.session_state.score) #temporary
st.divider()
# Answers
slider=st.select_slider("Choose how much you agree with this:",options=[1, 2, 3, 4, 5]);
b=st.button("Next Question",width="stretch")
if b:
    st.session_state.args[3]+=int(slider) #normal-scored
    st.switch_page("pages/pageD4.py")