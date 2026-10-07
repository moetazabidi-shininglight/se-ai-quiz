import streamlit as st
import time
import pandas as pd
from utils import set_background, save_result
set_background("thumb.jpg")
# Global Score
if "score" not in st.session_state:
    st.session_state.score=0
if "args" not in st.session_state:
    st.session_state.args=[0,0,0,0]

#save_results_to_admin_sheets
if not st.session_state.get("saved_sheet"):
    save_result(st.session_state.args)
    st.session_state.saved_sheet = True

st.set_page_config(initial_sidebar_state="collapsed")
# Home page
st.header("Final Result",text_alignment="center")
st.title("Your Score:",text_alignment="center")
st.title(str(sum(st.session_state.args))+"/100",text_alignment="center")
st.divider()
st.markdown("Critical Thinking: "+str(st.session_state.args[0])+"/30",text_alignment="center")
st.markdown("Self-Regulation: "+str(st.session_state.args[1])+"/20",text_alignment="center")
st.markdown("Self-Assessment: "+str(st.session_state.args[2])+"/25",text_alignment="center")
st.markdown("Empathy/Social Intelligence: "+str(st.session_state.args[3])+"/25",text_alignment="center")
st.divider()
if sum(st.session_state.args)>80 :
    st.balloons()
# Results
st.markdown("")
st.caption("© 2026 Moetaz Abidi | Khalil Gharbi ",text_alignment="center");
#b=st.button("Return to Home Page",width="stretch")
#if b:
#    bar=st.progress(0, text="")
#    for complete in range(50):
#        time.sleep(0.01)
#        bar.progress(complete + 2, text="")
#    time.sleep(1)
#    bar.empty()
#    st.switch_page("main.py")
