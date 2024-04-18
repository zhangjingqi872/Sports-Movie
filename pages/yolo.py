from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_drawable_canvas import st_canvas
import base64
from streamlit_extras.stylable_container import stylable_container 
import streamlit.components.v1 as components

# 设置页面配置
st.set_page_config(page_title="热辣滚烫",page_icon="🎞️", layout="wide")

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
    
def local_css(flie_name):
    with open(flie_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def color_text(color,string):
    text = "<span style='color: {};'>{}</span>".format(color, string)
    return text

def set_sidebar_background_transparent():
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: transparent;
        }
    </style>
    """, unsafe_allow_html=True)

# ---- Perpare ----
set_background('images/tolo3.jpg')# 加载背景图像

text = rf""" **:orange[拳击运动注意事项：]**"""
content = rf"""
           -1、热身时间要足够，否则身体得不到充分的伸展。上课时腿部应每15-20分钟作一次伸展。<br>
           -2、腹部、下颚收紧，两手握拳于脸前(防御姿势)保持呼吸，不屏气。<br>
           -3、避免和专业运动员一样进行长时间的训练，应交替进行大运动量和低运动量的练习。<br>
           -4、侧踢时不向前扭胯，否则会导致压力集中膝部，绷脚尖会扭伤。<br>
           -5、膝盖不要僵直，以减缓冲力，在转身时要抬起膝盖，否则会扭伤十字韧带。<br>
           -6、击拳时要由肩部带动出拳，在完成击拳和踢腿动作前一直看着目标。<br>
           -7、避免在拥挤的房间内进行后踢的动作。<br>
           -8、避免肘、膝部用力过猛;避免进行闪躲或猛击动作时由于动作过大而脱臼，避免扭转动作。<br>
           -9、若发生以下情况，可停止练习(腿部疲劳、人体局部出现痛状不适、眩晕、心率过快等)。"""

induction = "大学毕业后仅仅工作短暂的一段时间，杜乐莹（贾玲 饰）便退回家中，宅家长达十年之久。她无所事事，拒绝和外界做过多接触，甚至和家人的关系也变得紧张起来。在和离婚回到娘家的妹妹乐丹（张小斐 饰）一次激烈的冲突后乐莹选择离家出走，并且在烧烤店找了服务员的工作勉强维生。爱情、亲情、人生，似乎一时间均跌入了谷底，而阴差阳错间乐莹又结识了落魄的拳击教练昊坤（雷佳音 饰）。她支持着他的梦想，彼此又不得不去面对残酷的现实。人生至暗时刻，随波逐流的女孩是否决心逆流而上？<br>本片改编自日本电影《百元之恋》"

# ---- Sidebar ----
set_sidebar_background_transparent()
with st.sidebar.expander(text,expanded=True):
    st.markdown(
            f"""
            <div style="color:#ffdeb9; font-family: 宋体; height: 1020px; border: 1px solid rgba(49, 51, 63, 0.1); border-radius: 1rem; padding: calc(1em - 1px); background-color: rgba(255, 255, 255, 0.2);">
                <p style="margin-bottom: 0;">{content}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

col1, col2 = st.columns((3, 2))

with col2:
    st.markdown(
        f"""
        <div style="margin-bottom: 0; font-size: 28px; font-weight: bold; font-family: 宋体, sans-serif;color:white;">电影简介：</div>
        <div style="overflow-y: scroll; color:white; font-family: 宋体; height: 150px; border: 1px solid rgba(49, 51, 63, 0.1); border-radius: 1rem; padding: calc(1em - 1px); background-color: rgba(255, 255, 255, 0.2);">
            <p style="margin-bottom: 0;">{induction}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
    <style>
        .custom-divider {
            border: none;
            border-top: 1px solid rgba(255, 255, 255, 0.2);
            margin: 20px 0;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="margin-bottom: 0; font-size: 28px; font-weight: bold; font-family: 宋体, sans-serif;color:white;">猜你喜欢：</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    row1 = st.columns(2)
    
    col1_ = row1[0]
    tile = col1_.container(height=255)
    tile.image("images/million dollar baby.jpeg", use_column_width=True) 
    st.write("百万美元宝贝")
    col2_ = row1[1]
    tile = col2_.container(height=255)
    tile.image("images/100dollars.jpg", use_column_width=True)  
    
    
    st.divider()
    with st.container(height=400):
        with open("html/淘宝key.html", "r",encoding = 'utf-8') as f:
            map_html = f.read()
        st.components.v1.html(map_html,height=800,width=800)


# 在 col2 中添加辅助内容
with col1:
    st.markdown(
        """
        <div style="margin-bottom: 0; margin-top: -80px; font-size: 70px; font-weight: bold; font-family: '方正仿宋', cursive; color: white;">热辣滚烫</div>
        """,unsafe_allow_html=True
    )
    with col1.container(height=1000):
        st.image("images/图片1.png")

with open("html/lda_pass6.html", "r") as f:
    html = f.read()

# 使用st.components.v1.html函数将HTML文件嵌入到Streamlit中
st.components.v1.html(html, width=1300, height=800)
    



    
