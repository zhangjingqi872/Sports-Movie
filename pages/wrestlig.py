from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_drawable_canvas import st_canvas
import base64
from streamlit_extras.stylable_container import stylable_container 
import streamlit.components.v1 as components

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 设置页面配置
st.set_page_config(page_title="摔跤吧爸爸",page_icon="🎞️", layout="wide")

# ---- Perpare ----
set_background('images/摔跤.jpg')# 加载背景图像

col1, col2 = st.columns((3, 1.3))

with col1:
    st.markdown(
        """
        <div style="margin-bottom: 0; margin-top: -80px; font-size: 70px; font-weight: bold; font-family: '宋体', cursive; color: white;">摔跤吧爸爸</div>
        """,unsafe_allow_html=True
    )
    with col1.container(height=600):
        st.image("images/摔跤吧爸爸(1).png")