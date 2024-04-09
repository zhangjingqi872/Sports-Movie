from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(layout="wide")

st.header("Custom geolocation component")
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

with open(r"C:\Users\JQZhang\Desktop\remap.html", "r", encoding="utf-8") as f:
    html = f.read()


# 在Streamlit中显示修改后的HTML
st.components.v1.html(html,width=1000,height=1000)