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
st.title("Question #13")
st.divider()
# Question title
st.subheader("How well could you explain to a family member how a generative AI produces its answer?",text_alignment="center")
#st.markdown(st.session_state.score) #temporary
st.divider()
# Answers
slider=st.select_slider("Choose on a scale of 1 to 5:",options=range(1,6));
b=st.button("Next Question",width="stretch")
if b:
    st.session_state.args[2]+=int(slider) #normal-scored
    st.switch_page("pages/pageD1.py")