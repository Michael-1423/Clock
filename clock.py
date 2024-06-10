import streamlit as st
import time
from datetime import datetime

# Set the title of the app
# st.title("Real-Time Clock")

# Function to get the current time
def get_time():
    return datetime.now().strftime('%H:%M:%S')

# CSS to center the clock and style it
st.markdown(
    """
    <style>
    .clock {
        font-size: 72px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center the title
st.markdown('<div class="title"><h1>Real-Time Clock</h1></div>', unsafe_allow_html=True)

# Create a placeholder for the clock
clock_placeholder = st.empty()

# Run an infinite loop to continuously update the time
while True:
    current_time = get_time()
    clock_html = f'<div class="clock">{current_time}</div>'
    clock_placeholder.markdown(clock_html, unsafe_allow_html=True)
    time.sleep(1)
    st.experimental_rerun()
