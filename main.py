import streamlit as st


lang = st.sidebar.radio("Language", ["EN", "JP"], index=1, key="language")

suffix = lang.lower()

pages = [
    st.Page(f"contents/introduction_{suffix}.py", title="はじめに" if lang == "JP" else "Introduction", icon=":material/home:"),
    st.Page(f"contents/handson_{suffix}.py", title="作ってみよう" if lang == "JP" else "Hands-On", icon=":material/build:"),
    st.Page(f"contents/tips_{suffix}.py", title="開発のコツ" if lang == "JP" else "Tips", icon=":material/lightbulb_2:"),
]

st.navigation(pages, position="sidebar", expanded=True).run()
