import streamlit as st


st.sidebar.radio("Language", ["JP", "EN"], key="language")

if st.session_state["language"] == "JP":
    pages = [
        st.Page("contents/introduction_jp.py", title="はじめに", icon=":material/home:"),
        st.Page("contents/handson_jp.py", title="作ってみよう", icon=":material/build:"),
        st.Page("contents/develop_jp.py", title="開発のコツ", icon=":material/lightbulb_2:"),
    ]
else:
    pages = [
        st.Page("contents/introduction_en.py", title="Introduction", icon=":material/home:"),
        st.Page("contents/handson_en.py", title="Hands-On", icon=":material/build:"),
        st.Page("contents/develop_en.py", title="Tips", icon=":material/lightbulb_2:"),
    ]
st.navigation(pages, position="sidebar", expanded=True).run()
