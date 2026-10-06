import streamlit as st
import time
import pandas as pd
from utils import set_background
set_background("thumb.jpg")
# Global Score
from utils import log_visit
log_visit()
if "score" not in st.session_state:
    st.session_state.score=0
if "args" not in st.session_state:
    st.session_state.args=[0,0,0,0]
st.set_page_config(initial_sidebar_state="collapsed")
# Home page
st.header("Quiz",text_alignment="center")
st.title("Software Engineering & Generative AI",text_alignment="center")
st.markdown("Test your daily interaction with generative AI as software engineering student.",text_alignment="center")
st.divider()
# Buttons
b1=st.button("Take Quiz",width="stretch")
st.divider()
st.markdown("- 18 questions; no right or wrong answers, just answer honestly.",text_alignment="center")
st.markdown("- Your answers are NOT going anywhere. It's compltely anonymous and voluntary.",text_alignment="center")
st.markdown("- At the end you'll get your own personalized profile.",text_alignment="center")
st.markdown("")
st.caption("© 2026 Moetaz Abidi | Khalil Gharbi | Yassine Ben Youssef",text_alignment="center");
if b1:
    bar=st.progress(0, text="")
    for complete in range(50):
        time.sleep(0.01)
        bar.progress(complete + 2, text="")
    time.sleep(1)
    bar.empty()
    st.switch_page("Pages/pageA1.py")