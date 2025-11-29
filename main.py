import streamlit as st


pages = [
    st.Page("contents/overview.py", title="はじめに", icon=":material/home:"),
    st.Page("contents/workflow.py", title="開発手順", icon=":material/settings:"),
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
