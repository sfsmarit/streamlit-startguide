import streamlit as st

nl = "  "


st.set_page_config(page_title="Hands-On")
st.title("Let's Build Something Right Away")

st.markdown(
    f"""
    On this page, we'll go through the entire development process—from setting up the environment to publishing the app.
    """
)

st.subheader("Development Environment", divider=True)
st.image("data/dev_env.png")
st.markdown(
    f"""
    The development environment consists of three main components:

    1. **Local Environment**{nl}
    This is where you create the app. Typically, you write code and test it on your own PC.
    Install Streamlit and make sure you can view the app in your browser.
    We'll use Visual Studio Code as the integrated development environment.

    2. **GitHub**{nl}
    A cloud service for safely managing and sharing code.
    It tracks versions and changes made by different people.
    Later, we'll also use the GitHub repository when publishing the app to a web server.

    3. **Web Server**{nl}
    The environment where the app will be published.
    If you're okay with making it public, Streamlit Community Cloud is the easiest option.
    For internal use only, use an internal server.

    Next, we'll set up these environments one by one.
    """
)

st.subheader("Setting Up the Local Environment", divider=True)
st.markdown(
    f"""
    #### Install Visual Studio Code (First Time Only)
    https://azure.microsoft.com/en-us/products/visual-studio-code

    > Visual Studio Code (VS Code) is a free code editor provided by Microsoft.{nl}
    > It's lightweight yet highly extensible and widely used for Python development.

    1. **Launch VS Code and add the following extensions**
    - ~~**Japanese Language Pack for Visual Studio Code** (for Japanese UI)~~
    - **Python**
    - **Pylance** (code completion and type checking)
    - **autopep8** (automatic code formatting)
    """
)
st.image("data/vscode_extention.png")

st.markdown(
    """
    ---

    #### Install Streamlit (First Time Only)
    Streamlit is not included by default in Python, so you need to install it using pip.

    1. **Open the VS Code terminal and enter the following command**
    ```bash
    pip install streamlit
    ```
    """
)

st.image("data/vscode_terminal.png")

st.markdown(
    f"""
    ---

    #### Create a Project
    A **project** is a collection of code and data files for an application.
    In Streamlit, one project corresponds to one app.

    1. **Create a folder**{nl}
    Let's name it `sample-app`.
    If the project name has multiple words, follow GitHub conventions and use hyphens (-) instead of underscores (_).

    2. **Open the project in VS Code**{nl}
    Go to 'File > Open Folder' and select the `sample-app` folder.
    This puts the entire project under VS Code management, and files/folders will appear in the Explorer.

    3. **Create a script**{nl}
    Create a Python script named `main.py` for the app.
    """
)

st.image("data/create_script.png")

settings_json = '''
    {
        "[python]": {
            "editor.defaultFormatter": "ms-python.autopep8",
            "editor.formatOnSave": true,
        },
        "autopep8.args": [
            "--max-line-length=120"
        ]
    }
'''

launch_json = '''
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
'''

st.markdown(
    f"""
    Write the following in `main.py`:
    ```python
    import streamlit as st

    if st.button("Say Hello"):
        st.write("Hello!")
    ```

    4. **Run the app**{nl}
    Enter the following command in the VS Code terminal:
    ```bash
    streamlit run main.py
    ```
    If you see a button labeled 'Say Hello' in the browser, it worked!

    5. **Stop the app**{nl}
    Press Ctrl + C in the terminal to stop it.

    ---

    #### Improve Development Efficiency
    1. **Enable autopep8**{nl}
    >PEP8 is the official style guide for Python code readability.{nl}
    >It defines rules for indentation, spacing, line length, etc.
    
    Enabling autopep8 automatically formats your code to comply with PEP8 when you save.

    Create a `.vscode` folder in the project root.
    Inside it, create a `settings.json` file and add:
    ```json
    {settings_json}
    ```
    `--max-line-length=120` sets the maximum line length. PEP8 recommends 79 characters, but you can adjust as needed.

    2. **Run Streamlit with F5**{nl}
    Instead of typing `streamlit run main.py` every time, configure VS Code to run it in debug mode with F5.
    Create a `launch.json` file under `.vscode`:
    ```json
    {launch_json}
    ```
    This lets you run `streamlit run main.py` in debug mode with F5, regardless of the file you're editing.
    Note: Other scripts won't run with F5. If you change the main script name, update `args` accordingly.
    """
)

st.subheader("Upload to GitHub", divider=True)
st.markdown(
    """
    >GitHub is a web service that uses the Git version control system to manage and share code.
    >Deploying the app to a web server is also easier when using GitHub as an intermediary.
    
    Git has many features, but here we'll focus on the steps needed to publish the app.

    #### Overview of Git Management
    """
)

st.image("data/git_overview.png")

st.markdown(
    f"""
    Git manages file change history in a **repository**.
    Git works locally, and each user has their own repository.

    GitHub provides remote repositories for Git.
    This enables code sharing and backups.

    The steps to manage files with Git and GitHub are:

    1. Create a GitHub repository
    2. Initialize a local repository `init`
    3. Stage changes `add`
    4. Commit staged changes `commit`
    5. Upload commits to GitHub `push`

    In Agile terms, staging is like attaching files, and committing is like issuing a Change Order.
    You can also copy someone's GitHub repository using `clone` (not covered here).

    ---

    #### Initial Git Setup

    **Register a GitHub account (First Time Only)**{nl}
    https://github.co.jp/

    **Install Git (First Time Only)**{nl}
    https://git-scm.com/

    **Initial configuration (First Time Only)**{nl}
    Register author info for commit history.{nl}
    Enter the following commands in the terminal:
    ```bash
    git config --global user.name "Your_Name"
    git config --global user.email "Your_GitHub_email"
    ```
    Use the email linked to your GitHub account so your pushes are recognized correctly.

    ---

    #### Create a GitHub Repository
    Create a remote repository for each project.{nl}
    On GitHub's homepage, click **New** and enter the following:
    """
)

st.image("data/create_repository.png")

st.markdown(
    """
    Click **Create repository** to create a remote repository named `sample-app`.
    """
)

st.warning(
    f"""
    If you leave Visibility as `Public`, the repository will be visible worldwide.{nl}
    If it contains sensitive information or you want to restrict access, select `Private`.
    """
)

st.markdown(
    f"""
    ---

    #### Upload to GitHub
    There are two ways to manage files with Git:
    - Use VS Code's Source Control GUI
    - Use `git` commands in the terminal

    A) **Using `git` commands**{nl}
    For brevity, we'll start with the command-line method.{nl}
    Later, we'll show how to use VS Code's GUI.{nl}

    Open the VS Code terminal and run:
    ```bash
    # Initialize Git
    # Creates a .git folder
    git init

    # Link remote repository
    # 'origin' is a common convention
    git remote add origin https://github.com/<UserName>/sample-app.git

    # Stage all changes
    # To stage individual files: git add <filename>
    git add .

    # Commit changes
    git commit -m 'First commit'

    # Create branch (only once)
    git branch -M main

    # Upload to GitHub main branch
    git push -u origin main
    ```

    B) **Using VS Code Source Control**
    1. Initialize Git (`git init`)
    """
)

st.image("data/git_init.png")

st.markdown(
    f"""
    **Link remote repository** `git remote add`{nl}
    1. Click '... > Remote > Add Remote'
    2. Enter the GitHub repository URL: `https://github.com/<UserName>/sample-app.git`
    3. Set remote name to `origin`
    """
)

st.image("data/git_add_remote.png")

st.markdown(
    f"""
    **Stage and commit changes** `git add + git commit`{nl}
    Click Commit and enter a commit message.
    """
)

st.image("data/first_commit.png")

st.markdown(
    f"""
    **Publish branch and upload** `git push`{nl}
    - First time: Click 'Publish Branch'
    - After that: Click '... > Push'
    Check the GitHub repository page to confirm files are uploaded to the main branch.

    **Re-upload changes**{nl}
    When you modify `main.py`, you can commit again.
    Select 'Commit and Push' to stage, commit, and push in one step, updating GitHub immediately.
    """
)


st.image("data/git_commit_push.png")


st.subheader("Publish to a Web Server", divider=True)

st.markdown(
    f"""
    There are two main options for hosting your app:

    - **Streamlit Community Cloud**{nl}
    https://streamlit.io/cloud{nl}
    This is Streamlit's official free hosting service.
    It integrates with GitHub for easy app deployment and supports features like custom URLs and Secrets management.
    However, it only allows deployment from public repositories, so it's not suitable for apps handling sensitive information.

    - **Internal Server**{nl}
    This method runs the app on a server within your internal network.
    It's more secure and suitable for apps that handle confidential data.
    It offers greater customization, but you'll need to set up the environment and ensure stable operation yourself.

    Using the `sample-app` we created earlier as an example, let's look at how to deploy the app on these servers.

    ---

    #### Deploy to Streamlit Community Cloud
    1. Register for a Streamlit Community Cloud account (first time only){nl}
    https://streamlit.io/cloud{nl}

    2. Create an app from your GitHub repository{nl}
    Click 'Create app > Deploy a public app from GitHub' in the top-right corner{nl}
    """
)

st.image("data/deploy_streamlit_communication_cloud.png")

st.markdown(
    f"""
    ---

    #### Deploy to an Internal Server
    1. **Choose the server to use**{nl}
    If Streamlit apps are already in use internally, check with the administrator for access methods and management rules.
    If a new server is needed, request assistance from your IT team.
    
    2. **Set up the Streamlit environment on the server**{nl}
    If pip is available on the server, simply run `pip install streamlit`.{nl}
    If pip cannot be used due to permission restrictions, you'll need to work in a Python virtual environment.
    >A Python virtual environment is an isolated environment for each project.
    >It allows you to manage libraries and Python versions separately for each project.

    Create a virtual environment named `myenv` in your home directory:
    
    ```bash
    # Check Python version
    python --version

    # Move to home directory
    cd
    
    # Create virtual environment
    python -m venv myenv
    # Or specify Python version explicitly
    /usr/bin/python3.xx -m venv myenv
    
    # Activate virtual environment (for csh)
    source myenv/bin/activate.csh
    
    # Install Streamlit
    pip install streamlit
    
    # Deactivate virtual environment
    deactivate
    ```

    3. **Download the app from GitHub**{nl}
    Download the `sample-app` project folder to your home directory:
    ```bash
    # Move to home directory
    cd
    
    # Clone GitHub repository
    git clone https://github.com/<UserName>/sample-app.git
    ```
    
    4. **Run the app**{nl}
    ```bash
    # Move to project folder
    cd ~/sample-app
    
    # Start the app
    ~/myenv/bin/streamlit run main.py
    ```

    5. **Update the code**{nl}
    ```bash
    # Move to project folder
    cd ~/sample-app

    # Update code
    git pull
    ```
    `git pull` downloads updates and merges them into existing files (`fetch + merge`).

    ---

    #### Keep the app running reliably
    ...
    """
)
