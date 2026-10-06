import streamlit as st
import pandas as pd
import time
from utils import set_background
set_background("thumb.jpg")
# Global Score
if "score" not in st.session_state:
    st.session_state.score=0
st.title("Question #2")
st.divider()
# Question title
st.subheader("I sometimes use AI-generated code without fully understanding it.",text_alignment="center")
#st.write(st.session_state.args[0]) #temporary
st.divider()
# Answers
slider=st.select_slider("Choose how much you agree with this:",options=[1, 2, 3, 4, 5]);
b=st.button("Next Question",width="stretch")
if b:
    st.session_state.args[0]+=6-int(slider) #reverse-scored
    st.switch_page("pages/pageA3.py")