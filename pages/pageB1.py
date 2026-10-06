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
st.title("Question #7")
st.divider()
# Question title
st.subheader("I don't really understand people who use AI in their code.",text_alignment="center")
#st.markdown(st.session_state.score) #temporary
st.divider()
# Answers
slider=st.select_slider("Choose how much you agree with this:",options=[1, 2, 3, 4, 5]);
b=st.button("Next Question",width="stretch")
if b:
    st.session_state.args[1]+=6-int(slider) #reversed-scored
    st.switch_page("pages/pageB2.py")