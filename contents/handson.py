import streamlit as st

nl = "  "

st.set_page_config(page_title="作ってみる")
st.title("作ってみる")

st.markdown(
    """
    このページでは、Streamlit の開発環境を用意してアプリを作成し、公開するまでの一連の手順について紹介します。
    """
)

st.subheader("開発環境", divider=True)
st.image("data/dev_env.png")
st.markdown(
    f"""
    開発環境は主に次の3つで構成されます。

    1. **ローカル環境**{nl}
    アプリを作成する場所です。通常は自分の PC でコードを書き、動作確認を行います。
    Streamlit をインストールし、ブラウザでアプリを確認できるようにします。
    統合開発環境として Visual Studio Code を使用します。

    2. **GitHub**{nl}
    コードを安全に管理・共有するためのクラウドサービスです。
    コードのバージョンを管理し、誰がどの変更をしたか追跡できます。
    また、後で Web サーバに公開する際にも GitHub のリポジトリを使います。

    3. **Web サーバ**{nl}
    作成したアプリを公開するための環境です。
    一般に公開してもよければ Streamlit Community Cloud を使うのが最も簡単です。
    社内限定で公開する場合は社内サーバを使用してください。

    以降では、これらの環境を順番に構築していきます。
    """
)


st.subheader("1) ローカル環境の構築", divider=True)
st.markdown(
    """
    #### Visual Studio Code のインストール (初回のみ)
    Visual Studio Code (VS Code) とは、Microsoft が提供する無料のコードエディタです。
    軽量でありながら拡張機能が豊富で、Python の開発に広く利用されています。

    https://azure.microsoft.com/ja-jp/products/visual-studio-code

    1. **VS Code を起動して、以下の拡張機能を追加**
    - **Japanese Language Pack for Visual Studio Code** (日本語表示)
    - **Python**
    - **Pylance** (コード補完と型チェック)
    - **autopep8** (コード自動整形)
    """
)
st.image("data/vscode_extention.png")

st.markdown(
    """
    ---

    #### Streamlit のインストール (初回のみ)
    Streamlit はデフォルトでは Python にインストールされていないため、pip コマンドでインストールする必要があります。

    1. **VS Code のターミナルを起動して、次のコマンドを入力**
    ```bash
    pip install streamlit
    ```
    """
)

st.image("data/vscode_terminal.png")

st.markdown(
    """
    ---

    #### プロジェクトの作成
    アプリケーションごとのコードやデータファイルの集合を**プロジェクト**と呼びます。
    Streamlit でアプリを作る場合、ひとつのプロジェクトがひとつのアプリに対応します。

    1. **フォルダの作成**
    ここではフォルダ名を`sample-app`とします。
    プロジェクト名が複数単語からなる場合、GitHub の慣用表現にならって _ (アンダースコア) ではなく - (ハイフン) で繋ぎます。

    2. **VS Code でプロジェクトを開く**
    『ファイル > フォルダーを開く』で`sample-app`フォルダを指定します。
    すると、プロジェクト全体が VS Code の管理下に置かれ、エクスプローラにファイルやフォルダが表示されます。

    3. **アプリの作成**
    アプリ本体となる Python スクリプト `main.py` を作ります。
    """
)

st.image("data/create_script.png")

st.markdown(
    """
    `main.py`に以下を記述します。
    ```python
    import streamlit as st

    if st.button("Say Hello"):
        st.write("Hello!")
    ```

    4. **アプリの起動**\n
    VS Code のターミナルに次のコマンドを入力します。
    ```bash
    streamlit run main.py
    ```
    ブラウザに 'Say Hello' と書かれたボタンが表示されたら成功です。

    5. **アプリの終了**\n
    ターミナル上で Ctrl + C を押すと終了します。

    ---

    #### 開発の効率化
    1. **autopep8 の有効化**
    PEP8 とは、Python コードの可読性を高めるための公式スタイルガイドです。
    インデント、空白、行の長さ、命名規則などの基本的なルールを定義しています。
    autopep8 を有効にすると、PEP8 に準拠するようにコードが自動でフォーマットされます。

    プロジェクトフォルダの直下に`.vscode`フォルダを作成します。
    その下に`settings.json`ファイルを作成し、以下を記述します。
    ```json
    {
        "[python]": {
            "editor.defaultFormatter": "ms-python.autopep8",
            "editor.formatOnSave": true,
        },
        "autopep8.args": [
            "--max-line-length=120"
        ]
    }
    ```
    `--max-line-length=120`で一行の文字数を定義しています。PEP8 は 79 文字を推奨していますが、長すぎなければ自由に決めてよいです。

    2. **F5 キーで Streamlit を起動できるようにする**
    起動のたびに`streamlit run main.py`と入力するのは大変なので、VS Code のデバッグモード (F5) で起動できるように設定します。
    `.vscode`フォルダの下に`launch.json`を作成します。
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Streamlit",
                "type": "debugpy",
                "request": "launch",
                "module": "streamlit",
                "args": [
                "run",
                "main.py"
                ]
            }
        ]
    }
    ```
    このように設定すると、VS Code で現在編集しているファイルに関わらず、F5 キーを押すと`streamlit run main.py`がデバッグモードで実行されます。
    一方で、プロジェクトの他のスクリプトを F5 キーで実行できなくなります。
    アプリ本体のスクリプトを`main.py`から変更する場合は`args`も修正してください。
    """
)

st.subheader("2) GitHub にアップロード", divider=True)
st.markdown(
    """
    GitHub とは、バージョン管理システム「Git」を利用してコードを管理・共有する Web サービスです。
    後でアプリを Web サーバにデプロイする時にも、GitHub を経由してソースコードをアップロードします。
    GitHub は非常に多機能なツールですが、ここではアプリを公開するまでに必要な手続きのみに限定して説明します。

    ---

    #### Git 管理の全体像
    """
)

st.image("data/git_overview.png")

st.markdown(
    f"""
    Git はファイルの変更履歴を管理するツールです。
    履歴は**リポジトリ**と呼ばれるデータベースに保存されます。
    Git はローカルで動作し、ユーザごとにリポジトリを持ちます。

    GitHub は、 Git のリモートリポジトリを提供するサービスです。
    これにより、複数人でコードを共有したり、バックアップを取ったりできます。

    Git と GitHub を使ってファイルを管理する手順は以下のようになります。

    1. GitHub リポジトリ作成
    2. ローカルリポジトリの初期化 `init`
    3. ローカルファイルの変更をステージング `add`
    4. ステージングされた変更をコミット `commit`
    5. コミット内容を GitHub にアップロード `push`

    Agile で例えると、ステージングはファイル添付、コミットは Change Order に相当します。
    また、ここでは説明しませんが、誰かの GitHub リポジトリをコピー`clone`して使うこともできます。

    ---

    #### Git の初期設定

    **GitHub アカウント登録 (初回のみ)**{nl}
    https://github.co.jp/

    **Git のインストール (初回のみ)**{nl}
    https://git-scm.com/

    **初期設定 (初回のみ)**{nl}
    コミット履歴に記録される作者情報を登録します。{nl}
    以下のコマンドをターミナルに入力します。
    ```bash
    git config --global user.name "Your_Name"
    git config --global user.email "Your_GitHub_email_address"
    ```
    GitHub アカウントに紐づいているメールアドレスを登録しておくことで、プッシュしたときにアカウントが正しく認識されます。

    ---

    #### GitHub リポジトリの作成
    プロジェクトごとに GitHub のリモートリポジトリを作成します。{nl}
    GitHub のホームページから New をクリックし、リポジトリ作成画面で次のように入力します。
    """
)

st.image("data/create_repository.png")

st.markdown(
    """
    Create repository をクリックすると、`sample-app`という名前のリモートリポジトリが作成されます。
    """
)

st.warning(
    f"""
    Visibility をデフォルトの `Public` にすると、リポジトリが世界中に公開されます。{nl}
    機密情報を含む場合など、特定の相手にだけ公開したい場合は `Private` を選択します。
    """
)

st.markdown(
    f"""
    ---

    #### GitHub にアップロードするまで
    Git を操作してファイルを管理する方法は 2 種類あります。
    - VS Code のソース管理画面 (GUI) を使う
    - ターミナルに git コマンドを入力する

    A) **git コマンドを使う方法**{nl}
    作業内容をコンパクトに説明するために、まず git コマンドを使う方法を紹介します。
    実際には、この後に紹介する VS Code の管理画面を使うとよいです。{nl}

    VS Code のターミナルを開き、以下のコマンドを一つずつ実行します。
    ```bash
    # Git の初期化
    # .git フォルダが作成される
    git init

    # リモートリポジトリの紐づけ
    # origin は慣例的に使われている登録名
    git remote add origin https://github.com/<UserName>/sample-app.git

    # すべての変更をステージング
    # ファイルを個別にステージングする場合は git add <filename>
    git add .

    # 変更をコミット
    # '' はコメント
    git commit -m 'First commit'

    # ブランチの作成 (一度だけ)
    git branch -M main

    # GitHub の main ブランチにアップロード
    git push - u origin main
    ```

    B) **VS Code のソース管理画面を使う方法**
    1. Git の初期化 `git init`
    """
)

st.image("data/git_init.png")

st.markdown(
    f"""
    **リモートリポジトリの紐づけ `git remote add`**{nl}
    1. 「... > リモート > リモートの追加」をクリック
    2.  GitHub リポジトリの URL`https://github.com/<UserName>/sample-app.git`を入力
    3.  リモート名に`origin`を指定
    """
)

st.image("data/git_add_remote.png")

st.markdown(
    f"""
    **変更のステージング・コミット** `git add + git commit`{nl}
    コミットをクリックして、コミットメッセージを入力
    """
)

st.image("data/first_commit.png")

st.markdown(
    f"""
    **ブランチの発行・アップロード** `git push`{nl}
    - 初回 :「Branchの発行」をクリック
    - 以降 : 「... > プッシュ」をクリック
    GitHub のリポジトリのページを確認し、main ブランチにファイルがアップロードされていたら成功です。

    **変更を再アップロード**{nl}
    例えば`main.py`にボタンを追加して保存すると、変更が検出されて再びコミットできるようになります。
    「コミットしてプッシュ」を選択すると、ステージング・コミット・プッシュがまとめて実行され、直ちに GitHub に反映されます。
    """
)

st.image("data/git_commit_push.png")

st.subheader("3) Web サーバに公開する", divider=True)

st.markdown(
    f"""
    Web サーバの選択肢は主に 2 通りあります。
    - **Streamlit Community Cloud **{nl}
    https://streamlit.io/cloud{nl}
    Streamlit 公式の無料ホスティングサービスです。
    GitHub と連携して簡単にアプリを公開できます。さらに、URL のカスタマイズや Secrets 機能などもサポートされています。
    ただし、基本的に Public リポジトリしかデプロイできないため、機密情報を扱うアプリには使えません。

    - **社内サーバ**{nl}
    社内ネットワークにあるサーバでアプリを動作させる方法です。
    セキュリティ面で優れており、機密情報を扱うアプリに適しています。
    カスタマイズ性が高いですが、一方で環境構築や安定稼働の仕組みなどを自分で用意する必要があります。

    続いて、先ほど作成した`sample-app`を例に、これらのサーバでアプリを起動(デプロイ)する方法について紹介します。

    ---
 
    #### Streamlit Community Cloud にデプロイ
    1. Streamlit Community Cloud  アカウント登録 (初回のみ){nl}
    https://streamlit.io/cloud{nl}

    2. GitHub リポジトリからアプリ作成{nl}
    右上の「Create app > Deploy a public app from GitHub」を選択{nl}
    """
)


st.image("data/deploy_streamlit_communication_cloud.png")

st.markdown(
    f"""
    ---

    #### 社内サーバにデプロイ
    """
)
