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
st.title("Question #18")
st.divider()
# Question title
st.subheader("A teammate of your group suggested to use their AI-generated code to your project. What do you do?",text_alignment="center")
#st.markdown(st.session_state.args) #temporary
st.divider()
# Answers
b1=st.button("Refuse to use it.",width="stretch")
b2=st.button("Double-check it so it doesn't seem like AI and use it.",width="stretch")
b3=st.button("Remain silent.",width="stretch")
b4=st.button("Paste it into your code as it is.",width="stretch")
if b1 or b2 or b3 or b4:
    if b1 or b4:
        st.session_state.args[3]+=1
    if b2:
        st.session_state.args[3]+=5
    bar=st.progress(0, text="")
    for complete in range(50):
        time.sleep(0.01)
        bar.progress(complete + 2, text="")
    time.sleep(1)
    bar.empty()
    st.switch_page("pages/results.py")