from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(
    page_title="Sports Films-wrestling",
    page_icon="🤼‍♂️",
    layout="wide"
)

st.title("摔跤-wrestling")

if st.button("返回首页"):
    st.switch_page("Sports.py")

with st.container():
    st.write("---")
    image_column, text_column, margain_column = st.columns((0.5,2,1))
    with margain_column:
        st.link_button("进入详情", "http://localhost:8501/wrestlig")