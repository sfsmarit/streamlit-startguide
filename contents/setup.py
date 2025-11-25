import streamlit as st
from PIL import Image


st.set_page_config(page_title="環境構築")
st.title("環境構築")


st.subheader("開発環境", divider=True)
st.image(Image.open("data/development_environment.png"))


st.subheader("全体の流れ", divider=True)
st.markdown(
    """
    1. ツールのインストール
    2. GitHub リポジトリの作成
    3. 簡単なアプリの作成
    """
)
