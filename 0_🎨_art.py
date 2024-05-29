import streamlit as st
from PIL import Image

# set sidebar 
st.set_page_config(
    page_title="Art Inquiry Project",
    page_icon="🎨",
)

#############
# Title
st.title("Inquiry Project")
st.caption("By: Ryan")
st.divider()
st.write(
"""
    In my project, I asked the question what is the sound of the gym.

""")


#############
# Dumbells
st.divider()
st.image(r"dumbell.png")
st.audio("dumbell.m4a", format="audio/mpeg")

##################
# Strong
st.divider()
st.image(r"strong.png")
st.audio("strong.m4a", format="audio/mpeg")