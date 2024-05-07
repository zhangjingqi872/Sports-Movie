# 体育电影 web
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser
import streamlit.components.v1 as components
import time 
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(
    page_title="Sports Films",
    page_icon="🏅",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 禁用错误详情的显示
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 定义动图
def on_gif_click():
    print("已点击")
    # 打开另一个 Streamlit 应用的 URL
    url = "http://192.168.43.133:8501/film1"  # 替换为另一个 Streamlit 应用的 URL
    st.write("已点击")
    webbrowser.open_new_tab(url)

def local_html(html):
    with open(html, "r", encoding="utf-8") as f:
        st.markdown(f"{f.read()}", unsafe_allow_html=True)

def local_css(flie_name):
    with open(flie_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- LOAD ASSETS ----
lottie_coding1 = load_lottieurl("https://lottie.host/5cca82b1-41df-4c6a-a15e-94474fc4df0f/rG7wakcPJl.json")
lottie_coding2 = load_lottieurl("https://lottie.host/2f7892fe-8b46-4847-8e4c-a0d447d06b49/4VIGmlHRet.json")
lottie_coding3 = load_lottieurl("https://lottie.host/0f5f943a-08a1-43a4-a59a-2a7a2c82bd54/xZVSOpoXjr.json")
lottie_coding4 = load_lottieurl("https://lottie.host/3743f588-b54e-4a31-a4ea-975f42e43636/e3AmDJQvTM.json")
lottie_coding5 = load_lottieurl("https://lottie.host/5fe39d57-7a32-4f2a-b3cb-6f3abf2e4592/jX17cZKSoK.json")
lottie_coding6 = load_lottieurl("https://lottie.host/86beba8e-a510-45c2-aba2-9b1a6158336d/tZWALfhdKI.json")
lottie_coding7 = load_lottieurl("https://lottie.host/9d1ead3b-bfcb-4793-871d-c5c42912a948/AS4f7apVJS.json")
lottie_coding8 = load_lottieurl("https://lottie.host/82f65d35-51ac-42e9-bc88-0febcdfb6ffc/8w1QDGbnoF.json")
# st.sidebar.success("Already set a page above!")

# ---- HEADER SECTION ----
# 使用自定义样式的容器
st.markdown(
    """
    <div style="background-color: #99b2d5; padding: 1rem; border-radius: 0.5rem; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);">
        <h3 style="color: white;">风评较好的体育相关电影</h3>
        <h2 style="color: white;">选择你想观看的体育类型</h2>
        <p style="color: white;">Please choose the type of sports</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ----- Type of Sports ----

st.write("---")
left_column, middle_column,right_column = st.columns((3,2,3))

with left_column:
    st_lottie(lottie_coding1, height=100, key="coding1")  # Display the image
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="https://2film1py-gwcqg2ibetteyhovxr3xbf.streamlit.app/">
                <button class="boxing-button">拳击</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st_lottie(lottie_coding5, height=100, key="coding5")  # Display the image
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="http://localhost:8501/film1/">
                <button class="boxing-button">棒球</button>
            </a>
        </div>
    """, unsafe_allow_html=True)  

    st_lottie(lottie_coding3, height=100, key="coding3")  # Display the image
    
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="http://localhost:8501/film1/">
                <button class="boxing-button">篮球</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(0.2)   


    st.markdown("""
    <div style="display: flex; flex-direction: column; align-items: center;">
        <div style="width: 85%; height: 0; padding-bottom: 56%; position: relative; background-color: transparent;">
            <iframe src="https://giphy.com/embed/giLoYdQZH6ulo6Bpkp" width="50%" height="50%" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; margin: auto;" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
        </div>
        <p><a href="https://giphy.com/stickers/emoji-emojivid-womenwrestling-giLoYdQZH6ulo6Bpkp"></a></p>
        <a href="http://localhost:8501/film2/">
            <button class="boxing-button">摔跤</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    local_css("style/button.css")


with right_column:
    st_lottie(lottie_coding4, height=100, key="coding4")  # Display the image
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="http://localhost:8501/film1/">
                <button class="boxing-button">足球</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    st_lottie(lottie_coding2, height=100, key="coding2")
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="http://localhost:8501/film2/">
                <button class="boxing-button">高尔夫</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(0.2)      

    st_lottie(lottie_coding6, height=100, key="coding6")  # Display the image
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="http://localhost:8501/film1/">
                <button class="boxing-button">乒乓球</button>
            </a>
        </div>
    """, unsafe_allow_html=True)   

    st_lottie(lottie_coding7, height=100, key="coding7")  # Display the image
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="http://localhost:8501/film1/">
                <button class="boxing-button">网球</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st_lottie(lottie_coding8, height=100, key="coding8")  # Display the image
    st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <a href="http://localhost:8501/film1/">
                <button class="boxing-button">排球</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
    local_css("style/button.css")

    with middle_column:
        st.image("images/running.gif")

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
        st.markdown('<a href="https://sportspy-hujzhjnbl8wfdyya3bjvkn.streamlit.app/" target="_blank"></a>', unsafe_allow_html=True)       
