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
st.title("Question #15")
st.divider()
# Question title
st.subheader("A teammate wants to ban AI completely from the project. And another one strongly disagree. What do you do?",text_alignment="center")
#st.markdown(st.session_state.score) #temporary
st.divider()
# Answers
b1=st.button("Remain silent.",width="stretch")
b2=st.button("Call an immediate vote by majority.",width="stretch")
b3=st.button("Go with the person you agree with.",width="stretch")
b4=st.button("Ask each person to explain their concerns.",width="stretch")
if b1 or b2 or b3 or b4:
    if b2 or b3:
        st.session_state.args[3]+=2
    if b4:
        st.session_state.args[3]+=5
    st.switch_page("pages/pageD3.py")