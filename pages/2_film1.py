from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(
    page_title="Sports Films-boxing",
    page_icon="🥊",
    layout="wide",
)

def local_css(flie_name):
    with open(flie_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
# 禁用错误详情的显示
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

# ---- Perpare ----
img_Yolo = Image.open("images/hot.jpg")
img_Billion = Image.open("images/million dollar baby.jpeg")

# ---- Background ----
local_css("style/background.css")

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
    st.link_button("返回首页", "https://sportspy-hujzhjnbl8wfdyya3bjvkn.streamlit.app/")

# ---- Container with films ----
with st.container():
    st.write("---")
    image_column, text_column, margain_column = st.columns((0.5,2,0.5))
    with margain_column:
        st.link_button("进入详情", "https://yolopy-arbcrp8rts4goawzdwfugh.streamlit.app/")
        
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
        
with st.container():
    st.write("---")
    image_column, text_column, margain_column = st.columns((0.5,2,0.5))
    with margain_column:
        st.link_button("进入详情", "https://yolopy-arbcrp8rts4goawzdwfugh.streamlit.app/")
        
    with image_column:
    # insert image
        st.image(img_Billion)

    with text_column:
        st.subheader("百万美元宝贝")
        st.write(
            """
            导演: 克林特·伊斯特伍德&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;类型: 剧情 / 喜剧\n
            编剧: F·X·图尔 / 保罗·哈吉斯\n
            制片国家/地区: 美国\n
            上映日期: 2004-12-15(美国)
            """
        )
        code = '''主演: 克林特·伊斯特伍德 / 希拉里·斯万克 / 摩根·弗里曼 / 杰伊·巴鲁切尔 / 麦克·柯尔特 /
        露西娅 瑞科尔 / 布莱恩·F·奥博恩 / 安东尼·麦凯 / 玛格·马丁戴尔 / 瑞琪·琳德赫姆 / 迈克尔·佩纳 / 
        本尼托·马丁内斯 / Bruce MacVittie / David Powledge / 乔·达安格里奥
        '''
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
       st.markdown("""<script>window.location.href="https://sportspy-hujzhjnbl8wfdyya3bjvkn.streamlit.app/";</script>""", unsafe_allow_html=True)
