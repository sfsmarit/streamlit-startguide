import streamlit as st


nl = "  "

st.set_page_config(page_title="開発のコツ")
st.title("開発のコツ")


st.subheader("いきなり UI を作らない", divider=True)
st.markdown(
    f"""
    多くのアプリにおいて最も重要なのは、計算やデータ処理のロジック (関数や処理部分) です。{nl}
    まずはロジックを完成させ、その後にデータの入出力を行う UI を実装するとよいでしょう。{nl}

    UI とロジックを同時に作ると次のような問題が起きやすくなります。
    - 実行に時間がかかり、作業効率が落ちる
    - ロジック / UI / イベント管理の三重デバッグを強いられる

    ただし、UI を提供することが主目的のアプリでは、最初にハリボテの UI (ダミー入力 + 固定出力) を作っておくと、関係者への説明に役立ちます。
    """
)

st.subheader("プロジェクト管理", divider=True)
st.markdown(
    f"""
    ##### .gitignore でファイルを非公開にする
    機密情報を含むファイルや、開発環境と本番環境で分離したいファイルは`.gitignore`を使って Git 管理から除外します。

    1. プロジェクトフォルダ直下に `.gitignore` ファイルを作成
    2. 除外したいファイルやフォルダを記述 (例)
    ```
    __pycache__
    .env
    .streamlit/secrets.toml
    *.pptx
    !not_ignored.pptx
    ```

    ---

    ##### .env で環境を切り替える
    開発環境と本番環境で設定を切り替える場合、`.env`ファイルを使うと便利です。

    1. プロジェクト直下に `.env` ファイルを作成
    2. 環境変数を記述 (例)

    ```bash
    # 開発環境
    DEBUG=True
    DB_HOST=localhost
    DB_USER=dev_user
    ```
    ```bash
    # 本番環境
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
    複数人での開発や、機能追加・修正を安全に進めたい場合には、Git のブランチが便利です。
    > ブランチとは、Gitにおける「作業の分岐」であり、ひとつのリポジトリで複数の開発を同時に進めるための仕組みです。{nl}
    > 分岐したブランチの変更は他のブランチにマージできます。

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
st.caption("VS Code の UI 上でも同じことができます。")


st.subheader("Streamlit の仕様を理解する", divider=True)
st.markdown(
    f"""
    ##### Streamlit は再実行モデル
    Streamlit ではユーザーが操作するたびにスクリプト全体が再実行されます。
    例えば、ボタンを押すとコードが最初から実行され、画面全体が再描画されます。
    アプリの規模が大きくなり描画コストが増えると、操作性が悪化する可能性があります。
    > コード全体は再実行されますが、Python の仕様により import 文は最初の一度しか評価されません。
    > インポートしたモジュール内で状態を初期化する場合などは注意が必要です。

    ---

    ##### 状態管理には`st.session_state`を使う
    スクリプトが再実行されると通常の変数は保持されません。
    値を保持するには`st.session_state`を使います。
    例として、ボタンを押すたびにカウントを進めるコードは次のように書けます。
    ```python
    # 初期化
    if 'count' not in st.session_state:
        st.session_state['count'] = 0

    # カウントを増やす
    if st.button('Count up'):
        st.session_state['count'] += 1

    # 画面出力
    st.write('Current count', st.session_state['count'])
    ```

    :warning: 次のような場合には`st.session_state`もリセットされます。
    - ブラウザ側のセッションが切れる (リロード・タブを閉じる・ネットワーク切断など)
    - サーバ側の再起動
    - 長時間操作せずセッションタイムアウト
    """
)
with st.expander("`st.session_state`の操作を 1 行で書く"):
    st.markdown(
        """
        値の設定
        ```python
        if 'count' not in st.session_state:
            st.session_state['count'] = 0

        # 1行で書くと
        st.session_state.setdefault('count', 0)

        ```

        値の取得
        ```python
        if 'count' in st.session_state:
            x = st.session_state['count']
        else:
            x = 0

        # 1行で書くと
        x = st.session_state.get('count', 0)
        ```
        """
    )

st.markdown(
    """
    ---

    ##### シングルスレッド動作
    Streamlit は基本的に 1 ユーザーにつき 1 スレッドで動作します。
    複数ユーザーが同時アクセスすると、サーバー側では別スレッドで処理され、ユーザー間で状態は共有されません。
    """
)

st.subheader("UI", divider=True)
st.markdown(
    f"""
    ##### 凝った UI を作らない
    Streamlit のメリットは、あらかじめ用意された豊富なウィジェットで高速に開発できることです。
    まずはどのようなウィジェットが利用可能か把握しておくとよいでしょう。

    [API reference](https://docs.streamlit.io/develop/api-reference)

    HTML+CSS や複雑な条件分岐を駆使すれば高機能なウィジェットも自作できます。
    しかし、開発に時間がかかってしまうと Streamlit を使うメリットが薄れてしまいます。
    そのような場合には、アプリの機能やロジックを見直すべきでしょう。

    ---

    ##### 入力を取得する方法は 2 通りある
    **1. ウィジェットの戻り値を使う**
    ```python
    result = st.radio("Judge", ["OK", "NG", "NA"])
    ```
    取得した値をすぐに処理するような場合に適しています。

    **2. ウィジェットに設定したキーを参照する**
    ```python
    st.radio("Judge", ["OK", "NG", "NA"], key="design_check_judge")
    # ...
    result = st.session_state["design_check_judge"]
    ```
    ウィジェットを配置する時にキーを設定すると、ウィジェットの状態を`st.session_state`から取得できます。
    配置するコードと値を処理するコードが離れている場合に便利です。

    > キーはページ内の全ウィジェットで一意でないとエラーになります。{nl}
    > キーを設定しなかった場合、Streamlit が内部でキーを自動生成します。

    ---

    ##### コールバックを活用する
    例えば、ボタンが押されたときに`st.session_state`の状態を変更するには次のように書けます。
    ```python
    if st.button('Push here'):
        st.session_state['saved'] = True
    ```
    ここで注意したいのは、ボタンを押しても、ボタンが再描画されるまでは`True`にならないということです。
    ボタンを配置する前に`st.session_state['saved']`を参照すると想定と異なる挙動をします。

    変更を即座に反映させたい場合、ウィジェットのコールバック機能を使いましょう。
    ```python
    def func():
        st.session_state['saved'] = True

    st.button('Push here', on_click=func)
    ```
    このように書くと、ボタンが押された直後にまずコールバック関数`func`が呼ばれ、その後に全体が再描画されます。
    `st.session_state`の状態管理やデータの書き込みなど、変更を直ちに反映させたい時に使うとよいです。
    """
)

st.subheader("データの読み書き", divider=True)
st.markdown(
    """
    ##### 静的ファイルを使う
    「データの保存 = データベース」ではありません。
    読み込みだけ行う場合や更新頻度が低い場合などは、`csv`や`json`といった静的ファイルで十分です。
    """
)
with st.expander("json の読み込み"):
    st.markdown(
        """
        ```python
        import json

        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        ```
        """
    )
with st.expander("csv の読み込み"):
    st.markdown(
        """
        ```python
        import csv

        rows = []
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)

        # pandas でテーブル全体を読み込むこともできる
        import pandas as pd
        df = pd.read_csv(filepath, encoding="utf-8")
        ```
        """
    )

st.markdown(
    """
    ##### データベースを活用する
    頻繁に更新される、検索や絞り込みが多い、複数ユーザーが同時に使うといった場合には、データベースを使うほうが安全で効率的です。
    ```
    # 作成中
    ```
    """
)

st.subheader("アクセスを制限する", divider=True)
st.markdown(
    f"""
    限られたメンバーにのみアプリを公開したい場合、`streamlit-authenticator`でログインフォームを作るとよいです。

    [サンプルコード]("https://github.com/sfsmarit/streamlit-login-form")
    """
)

st.subheader("コードが複雑になってきたら", divider=True)
st.markdown(
    f"""
    ##### 同じ処理を関数にまとめる
    コードが長くなると、同じ処理を何度も書いてしまうことがあります。
    関数にまとめることでコードの再利用できます。
    ```python
    def greet(name: str):
        st.write('Hello', name)

    greet("Alice")
    ```

    ---

    ##### モジュールを分割する
    コードがひとつのファイルに集中すると扱いづらくなります。
    共通処理や機能のまとまりを別の`.py`ファイルに分けて、import で読み込むと整理できます。

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
    アプリの規模が大きくなってくると`st.session_state`のキーも増えてきます。
    `st.session_state`は辞書としてふるまうため、キーは IDE で補完されません。
    キーが増加すると覚えられなくなったり、タイポによるエラーのもとになります。

    多数のキーを安全に管理する手段として、列挙型`Enum`を使う方法があります。
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
    キーには文字列である`Key.XXX.name`を指定します。
    """
)

st.subheader("重い処理の対策", divider=True)
st.markdown(
    f"""
    ##### アプリを複数ページに分ける
    ひとつのページに機能を詰め込みすぎている場合、ページを分けることでパフォーマンスの改善が期待されます。
    `st.navigation`を使うと簡単にマルチページを作成できます。
    ```python
    pages = [
        st.Page('introduction.py', title='Introduction', icon=':material/home:'),
        st.Page('handson.py', title='Hands-on', icon=':material/build:'),
        st.Page('tips.py', title='Tips', icon=":material/lightbulb_2:"),
    ]
    st.navigation(pages, position="sidebar", expanded=True).run()
    ```

    ---

    ##### キャッシュを使う
    Streamlit のキャッシュには`st.cache_data`と`st.cache_resource`の 2 種類あります。
    
    ||`st.cache_data`|`st.cache_resource`
    |---|---|---|
    |対象|計算結果やデータ|外部リソースや接続|
    |用途|同じ入力で同じ結果になる処理をキャッシュして再計算を避ける|初期化コストが高いリソースを一度だけ作って再利用する|
    |例|高コストの計算、静的ファイル読み込み、APIレスポンス|機械学習モデルの読み込み、データベース接続|
    
    `st.cache_data`の使用例
    ```python
    import pandas as pd
    
    @st.cache_data(ttl=300, show_spinner=True)  # 5分キャッシュ
    def load_table(path: str, encoding: str = "utf-8") -> pd.DataFrame:
        return pd.read_csv(path, encoding=encoding)
    
    df = load_table("large_table.csv")
    ```

    `st.cache_resource`の使用例
    ```python
    import joblib
    
    @st.cache_resource
    def load_model(path: str):
        return joblib.load(path)

    model = load_model("random_forest.pkl")
    ```

    ---

    ##### 正直に見せる
    ユーザーに「動いている」ことを伝えるだけで体感が改善します。

    ```python
    # スピナーで進行中を見せる
    with st.spinner("計算中..."):
        time.sleep(3)
    ```

    ```python
    # プログレスバーを表示する
    pbar = st.progress(0, "ステップごとの進捗")
    for i in range(3):
        time.sleep(1)
        pbar.progress(100*(i+1)/5)
    ```

    ---

    ##### 別プロセスに分離する
    """
)

with st.expander("multiprocessing + Que で進捗確認"):
    st.markdown(
        """
        ```python
        import streamlit as st
        import multiprocessing as mp
        import time

        # 状態初期化
        for k, v in {
            'proc': None,
            'progress': 0,
            'done': False,
            'msg': ""
        }.items():
            if k not in st.session_state:
                st.session_state[k] = v

        def heavy_job(progress_q: mp.Queue, done_q: mp.Queue):
            for i in range(10):
                time.sleep(0.4)
                progress_q.put((i + 1) * 10)
            done_q.put({'ok': True, 'summary': '処理が完了しました'})

        def start_process():
            progress_q = mp.Queue()
            done_q = mp.Queue()
            p = mp.Process(target=heavy_job, args=(progress_q, done_q), daemon=True)
            p.start()
            st.session_state['proc'] = {'p': p, 'progress_q': progress_q, 'done_q': done_q}
            st.session_state['progress'] = 0
            st.session_state['done'] = False
            st.session_state['msg'] = ""

        def poll_status():
            proc = st.session_state['proc']
            if not proc:
                return
            try:
                while True:
                    st.session_state['progress'] = proc['progress_q'].get_nowait()
            except Exception:
                pass
            try:
                result = proc['done_q'].get_nowait()
                st.session_state['done'] = True
                st.session_state['msg'] = result.get('summary', '')
            except Exception:
                pass

        st.title("別プロセスで実行（multiprocessing）")

        if st.button("重い処理を別プロセスで開始"):
            start_process()
            st.info("バックグラウンドで処理を開始しました")

        poll_status()
        st.progress(st.session_state['progress'] / 100)
        if st.session_state['done']:
            st.success(st.session_state['msg'])

        if st.session_state['proc'] and st.button("中断する"):
            try:
                st.session_state['proc']['p'].terminate()
                st.session_state['proc']['p'].join(timeout=1)
                st.warning("プロセスを中断しました")
            finally:
                st.session_state['proc'] = None
                st.session_state['progress'] = 0
                st.session_state['done'] = False
                st.session_state['msg'] = ""
        ```
        """
    )

with st.expander("ProcessPoolExecutor で関数を投げる"):
    st.markdown(
        """
        ```python
        import streamlit as st
        from concurrent.futures import ProcessPoolExecutor, Future
        import time

        # 共有 Executor（初期化コストを抑える）
        @st.cache_resource
        def get_executor():
            # CPUコア数に応じて調整（例：2〜4）
            return ProcessPoolExecutor(max_workers=2)

        def heavy_return(n: int) -> dict:
            time.sleep(2)
            return {"input": n, "result": n * n}

        # Future をセッションに保持
        if "future" not in st.session_state:
            st.session_state.future = None

        executor = get_executor()
        st.title("別プロセスで実行（ProcessPoolExecutor）")

        val = st.number_input("入力値", value=42, step=1)
        if st.button("別プロセスで計算"):
            st.session_state.future = executor.submit(heavy_return, int(val))
            st.info("計算を開始しました（2秒程度）")

        # 状態チェック
        fut: Future = st.session_state.future
        if fut:
            if fut.done():
                try:
                    res = fut.result()
                    st.success(f"完了: {res}")
                except Exception as e:
                    st.error(f"エラー: {e}")
            else:
                st.spinner("計算中…")

        ```
        """
    )

with st.expander("subprocess で別スクリプトを起動"):
    st.markdown(
        """
        ```python
        import streamlit as st
        import subprocess
        import sys

        st.title("別プロセスで実行（subprocess）")

        if st.button("スクリプトを起動（ログを表示）"):
            # 例：python worker.py を起動（stdout を取り込んで逐次表示）
            # Windows の場合は shell=False を基本に、必要なら text=True を併用
            proc = subprocess.Popen(
                [sys.executable, "worker.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            st.session_state.subproc = proc
            st.info("worker.py を起動しました")

        # ログの取り込み
        proc = st.session_state.get("subproc")
        if proc and proc.stdout:
            # 再実行のたびに読み進める（注意：この方法は行がないとブロックしうる）
            for _ in range(10):  # 1回の再実行で最大10行まで表示する例
                line = proc.stdout.readline()
                if not line:
                    break
                st.write(line.rstrip())

            code = proc.poll()
            if code is not None:
                if code == 0:
                    st.success("worker.py が正常終了しました")
                else:
                    st.error(f"worker.py が異常終了（コード: {code}）")
                st.session_state.subproc = None
        ```
        """
    )
