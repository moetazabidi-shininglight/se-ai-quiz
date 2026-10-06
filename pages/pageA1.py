import streamlit as st
import pandas as pd
import time
from utils import set_background
set_background("thumb.jpg")
# Global Score
if "score" not in st.session_state:
    st.session_state.score=0
st.title("Question #1")
st.divider()
# Question title
st.subheader("You're about to submit your assignment. But, you don't really understand that AI-generated part of your code. What do you do?",text_alignment="center")
#st.markdown(st.session_state.args[0]) #temporary
st.divider()
# Answers
b1=st.button("Ask the AI agent for explanation, then submit.",width="stretch")
b2=st.button("Submit it as is.",width="stretch")
b3=st.button("Rewrite that part yourself.",width="stretch")
if b1 or b2 or b3:
    if b1:
        st.session_state.args[0]+=1
    if b2:
        st.session_state.args[0]+=2
    if b3:
        st.session_state.args[0]+=5
    st.switch_page("pages/pageA2.py")