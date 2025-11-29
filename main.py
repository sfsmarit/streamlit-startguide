import streamlit as st


pages = [
    st.Page("contents/overview.py", title="はじめに", icon=":material/home:"),
    st.Page("contents/handson.py", title="作ってみる", icon=":material/settings:"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
