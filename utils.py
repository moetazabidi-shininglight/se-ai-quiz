import base64
from pathlib import Path
import streamlit as st
import uuid
import csv
import os
import threading
import uuid
from datetime import datetime
import streamlit as st
import gspread
_lock = threading.Lock()

def log_visit():
    if "visitor_id" not in st.session_state:
        st.session_state.visitor_id = uuid.uuid4().hex[:8]
        with _lock:
            new_file = not os.path.exists("visits.csv")
            with open("visits.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if new_file:
                    writer.writerow(["visitor_id", "date"])
                writer.writerow([st.session_state.visitor_id,
                                 datetime.now().isoformat(timespec="seconds")])


SHEET_NAME = "quiz_results"

@st.cache_resource
def get_spreadsheet():
    gc = gspread.service_account_from_dict(dict(st.secrets["gcp_service_account"]))
    return gc.open(SHEET_NAME)

def save_result(args):
    """Append one respondent's scores to the first tab."""
    sheet = get_spreadsheet().sheet1
    sheet.append_row([
        datetime.now().isoformat(timespec="seconds"),
        *args,
        sum(args),
    ])

def log_visit():
    """Log one visit per session in the 'visits' tab."""
    if "visitor_id" not in st.session_state:
        st.session_state.visitor_id = uuid.uuid4().hex[:8]
        try:
            get_spreadsheet().worksheet("visits").append_row([
                st.session_state.visitor_id,
                datetime.now().isoformat(timespec="seconds"),
            ])
        except Exception:
            pass   
def set_background(filename="thumb.jpg"):
    image_path = Path(__file__).parent / "assets" / filename
    encoded = base64.b64encode(image_path.read_bytes()).decode()
    ext = image_path.suffix.lower().lstrip(".")
    mime = "jpeg" if ext == "jpg" else ext 

    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                              url("data:image/{mime};base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        [data-testid="stHeader"] {{
            background: rgba(0, 0, 0, 0);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )