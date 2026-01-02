import streamlit as st


nl = "  "

st.set_page_config(page_title="開発のコツ")
st.title("開発のコツ")


st.subheader("いきなり UI を作らない", divider=True)
st.markdown(
    f"""
    多くのアプリにおいて最も重要な機能は、計算やデータ処理のロジックです。{nl}
    最初にロジックのコードを完成させ、その後にデータの入出力を行う UI を実装するとよいでしょう。{nl}
    いきなり UI から着手すると次のような問題が起きます。
    - 実行に時間がかかり、作業効率が落ちる
    - ロジック / UI / イベントハンドリングの三重デバッグを強いられる

    ただし、UI を提供することが主目的のアプリでは、最初にハリボテの UI を作っておくと関係者への説明に役立ちます。
    """
)

st.subheader("プロジェクトの管理", divider=True)
st.markdown(
    f"""
    ##### .gitignore でファイルを非公開にする
    機密情報を含むファイルや、開発環境と本番環境で分離したいファイルは **`.gitignore`** を使って Git 管理から除外します。

    1. プロジェクトフォルダ直下に `.gitignore` ファイルを作成
    2. 除外したいファイルやフォルダを記述
    ```
    .env
    .streamlit/secrets.toml
    __pycache__
    *.pptx
    !not_ignored.pptx
    ```

    ---

    ##### .env で環境を切り替える
    開発環境と本番環境で設定を切り替える場合、`.env`ファイルを使うと便利です。

    1. プロジェクト直下に `.env` ファイルを作成
    2. 環境変数を記述

    ```bash
    # 開発環境の .env
    DEBUG=True
    DB_HOST=localhost
    DB_USER=dev_user
    ```
    ```bash
    # 本番環境の .env
    DEBUG=False
    DB_HOST=prod-db.example.com
    DB_USER=prod_user
    ```

    3. Python で読み込むには`python-dotenv`を利用します。
    ```bash
    pip install python-dotenv
    ```
    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()  # .envを読み込む
    db_host = os.getenv("DB_HOST")
    debug_mode = os.getenv("DEBUG") == "True"
    ```

    ---

    ##### ブランチを分ける
    複数人での開発や、機能の追加 / 修正を安全に進めたい場合には、Git のブランチが便利です。
    > ブランチとは、Gitにおける「作業の分岐」であり、ひとつのリポジトリで複数の開発を同時に進めるための仕組みです。{nl}
    > 分岐したブランチの変更は他のブランチにマージすることができます。

    小規模開発におけるブランチ戦略の例
    |ブランチ名|役割|
    |---|---|
    |main|本番用|
    |develop|開発用|

    ブランチの作成
    ```bash
    # develop ブランチを作成して切り替える
    git checkout -b develop
    ```

    `main`と`develop`で Web ページを分ける
    ```bash
    # main
    git clone <repository_url>
    # develop
    git clone -b develop <repository_url>
    # データの更新方法は同じ
    git pull
    ```

    **ブランチ開発の流れ**{nl}
    `git`コマンドで説明しますが、VS Code の UI でも同じことができます。
    1. `develop`で開発
    ```bash
    git checkout develop
    # --- コード修正完了 ---
    git add .
    git commit -m "新機能の追加"
    git push origin develop
    ```
    2. `develop`の状態が安定したら`main`にマージ
    ```bash
    git checkout main
    git merge --no-ff develop
    git push origin main
    ```
    """

)

st.subheader("Streamlit の独特な仕様", divider=True)
st.markdown(
    """
    """
)

st.subheader("UI", divider=True)
st.markdown(
    f"""
    ##### 凝った UI を作らない
    Streamlit のメリットは、あらかじめ用意された豊富なウィジェットで高速に開発できることです。
    まずはどのようなウィジェットが利用可能か把握しておくとよいです。
    https://docs.streamlit.io/develop/api-reference

    HTML+CSS や複雑な条件分岐を駆使すれば高機能なウィジェットも自作できます。
    しかし、開発に時間がかかってしまうと Streamlit を使うメリットが薄れてしまいます。
    そのような場合には、アプリの機能やロジックを見直すべきでしょう。

    ---

    ##### コールバックを活用する
    例えば、ボタンが押されたときに`session_state`の状態を変更するには次のように書けます。
    ```python
    if st.button('Push here'):
        st.session_state['saved'] = True
    ```
    ここで注意したいのは、ボタンが押されてボタンが再描画されるまでは`True`にならないということです。
    ボタンを配置する前に`st.session_state['saved']`を参照しようとすると想定と異なる挙動をします。

    変更を即座に反映させたい場合、ウィジェットのコールバック機能を使いましょう。
    ```python
    def func():
        st.session_state['saved'] = True

    st.button('Push here', on_click=func)
    ```
    このように書くと、ボタンが押された直後にまずコールバック関数`func`が呼ばれ、その後に全体が再描画されます。
    `session_state`の状態管理やデータの書き込みなど、変更を直ちに反映させたい時に使うとよいです。
    """
)

st.subheader("コードが複雑になってきたら", divider=True)
text = "f'Hello, {name}!'"
st.markdown(
    f"""
    ##### 同じ処理を関数にまとめる
    コードが長くなると、同じ処理を何度も書いてしまうことがあります。{nl}
    関数にまとめることで、コードの再利用性と可読性が向上します。
    ```python
    def greet(name: str):
        st.write({text})
        
    greet("Alice")
    ```

    ---

    ##### モジュールを分割する
    コードがひとつのファイルに集中すると扱いづらくなります。
    共通処理や機能のまとまりを別の Python スクリプトに分けて、import で読み込むと整理できます。

    ```python
    # utils.py
    def generate_email_from_name(name: str, domain: str = "gmail.com"):
        address = ".".join(name.lower().split())
        return address + '@' + domain
    ```
    ```python
    # main.py
    from utils import generate_email_from_name
    email = generate_email_from_name("Tanaka")

    # もしくは
    import utils
    email = utils.generate_email_from_name("Tanaka")
    ```
    
    ---

    ##### session_state のキー管理
    アプリの規模が大きくなってくると`session_state`のキーも増えてきます。
    `session_state`は辞書としてふるまうため、キーは IDE で補完されません。
    キーが増加すると覚えられなくなったりタイポでエラーになったりします。
    
    大量のキーを安全に管理する手段として、列挙型`Enum`を使う方法があります。
    ```python
    from enum import Enum, auto
    
    # Enumクラスを継承したKeyクラスを定義    
    class Key(Enum):
        USER_NAME = auto()
        USER_EMAIL = auto()
    
    # Key.XXXはIDEで補完可能    
    st.text_input("User Name", key=Key.USER_NAME.name)
    ```
    列挙型は一意的な名前の集合であり、重複が許されないキーに使えます。
    `session_state`のキーは文字列のため`Key.XXX.name`を指定します。

    ---

    """
)

st.subheader("重い処理の対策", divider=True)
st.markdown(
    """
    """
)

st.subheader("データベースを活用する", divider=True)
st.markdown(
    """
    """
)

st.subheader("ログイン認証", divider=True)
st.markdown(
    f"""
    限られたメンバーにのみアプリを公開したい場合、`streamlit-authenticator`でログインフォームを作るとよいです。{nl}
    こちらで使い方を説明しています。{nl}
    https: // github.com/sfsmarit/streamlit-login-form

    """
)

st.subheader("ログと監視", divider=True)
st.markdown(
    """
    """
)
