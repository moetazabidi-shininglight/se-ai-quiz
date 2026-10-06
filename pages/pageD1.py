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
st.title("Question #14")
st.divider()
# Question title
st.subheader("A teammate admits they used AI for the group project and is afraid of being caught. What do you do first?",text_alignment="center")
#st.markdown(st.session_state.score) #temporary
st.divider()
# Answers
b1=st.button("It's not a big deal, everyone is using it.",width="stretch")
b2=st.button("Say nothing.",width="stretch")
b3=st.button("Help them to be more independent to AI and redo the key parts.",width="stretch")
b4=st.button("Tell them it's their problem (politely).",width="stretch")
if b1 or b2 or b3 or b4:
    if b1 :
        st.session_state.args[3]+=2
    if b3:
        st.session_state.args[3]+=5
    st.switch_page("pages/pageD2.py")