from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import Sports
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(
    page_title="Sports Films-boxing",
    page_icon="🥊",
    layout="wide",
)

# 禁用错误详情的显示
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# ---- Perpare ----
img_Yolo = Image.open("images/hot.jpg")

# ---- Title ----
Sports.local_css("style/background.css")

left_column,right_column = st.columns((3,1))

with left_column:
    st.markdown(
        """
            <div style="background-color: #99b2d5; padding: 1rem; border-radius: 0.5rem; box-shadow: 0 0px 0px rgba(0, 0, 0, 0.1); color: white;">
            <h1 style="color: white;">拳击-boxing</h1>
            <p>Please choose the type of sports</p>
        </div>
        """,
        unsafe_allow_html=True
    )
with right_column:
    if st.button("返回首页"):
        st.switch_page("Sports.py")

# ---- Container with films ----
with st.container():
    st.write("---")
    image_column, text_column, margain_column = st.columns((0.5,2,0.5))
    with margain_column:
        st.link_button("进入详情", "http://localhost:8501/yolo")
        
    with image_column:
    # insert image
        st.image(img_Yolo)

    with text_column:
        st.subheader("热辣滚烫")
        st.write(
            """
            导演: 贾玲&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;类型: 剧情 / 喜剧\n
            编剧: 贾玲 / 孙集斌 / 刘宏禄 / 郭宇鹏 / 卜钰\n
            制片国家/地区: 中国大陆\n
            上映日期: 2024-02-10(中国大陆)
            """
        )
        code = '''主演: 贾玲 / 雷佳音 / 张小斐 / 杨紫 / 沙溢 / 乔杉 / 李雪琴 / 马丽 / 魏翔 / 赵海燕 / 张琪 /
    沈春阳 /沈涛 / 许君聪 / 卜钰 / 朱天福 / 刘宏禄 / 张泰维 / 郭宇鹏 / 李海银 / 李国麟 /
    张桂玲 / 孙婉竹 / 赵婷婷 / 法志远 / 姬晴 / 曹贺军 / 刘頔 / 贾文田 / 雷鸣武'''
        st.code(code, language='txt')

# ---- Sidebar ----

st.markdown('<style>' + open('style/style_tab.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['首页', '电影', '运动'], 
                         iconName=['dashboard', 'money', 'economy'], 
                         styles = {'navtab': {'background-color':'#99b2d5',
                                                  'color': '#111',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'white',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")

    if tabs =='首页':
        st.switch_page("Sports.py")
    