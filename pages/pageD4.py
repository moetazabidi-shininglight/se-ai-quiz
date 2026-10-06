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
st.title("Question #17")
st.divider()
# Question title
st.subheader("A group in your class are presenting their AI-generated code with errors in front of your professor. What do you do?",text_alignment="center")
#st.markdown(st.session_state.score) #temporary
st.divider()
# Answers
b1=st.button("Remain silent.",width="stretch")
b2=st.button("Point out the errors.",width="stretch")
b3=st.button("Talk to them privately about the errors and agree on a way to double-check next time.",width="stretch")
if b1 or b2 or b3:
    if b2:
        st.session_state.args[3]+=0
    if b1:
        st.session_state.args[3]+=3
    if b3:
        st.session_state.args[3]+=5
    st.switch_page("pages/pageD5.py")