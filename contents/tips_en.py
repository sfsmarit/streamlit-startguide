
import streamlit as st

nl = "  "

st.set_page_config(page_title="Development Tips")
st.title("Development Tips")

st.subheader("Don’t Start with the UI", divider=True)
st.markdown(
    f"""
    In most applications, the most important part is the logic for computation and data processing (functions and processing code).{nl}
    It’s better to complete the logic first, and then implement the UI that handles data input and output.{nl}

    Building the UI and the logic at the same time often leads to the following issues:
    - Execution takes longer, reducing productivity
    - You’re forced into triple debugging: logic / UI / event management

    However, for applications whose primary purpose is to provide a UI, creating a mock UI (dummy inputs + fixed outputs) first can help with stakeholder explanations and reviews.
    """
)

st.subheader("Project Management", divider=True)
st.markdown(
    f"""
    ##### Hide Files with `.gitignore`
    For files that contain sensitive information or files that you want to separate between development and production environments, exclude them from Git by listing them in `.gitignore`.

    1. Create a `.gitignore` file in the project root
    2. List files or folders you want to exclude (example)
    ```
    __pycache__
    .env
    .streamlit/secrets.toml
    *.pptx
    !not_ignored.pptx
    ```

    ---

    ##### Switch Environments with `.env`
    If you need to switch settings between development and production, a `.env` file is convenient.

    1. Create a `.env` file in the project root
    2. Write environment variables (examples)

    ```bash
    # Development
    DEBUG=True
    DB_HOST=localhost
    DB_USER=dev_user
    ```
    ```bash
    # Production
    DEBUG=False
    DB_HOST=prod-db.example.com
    DB_USER=prod_user
    ```

    3. Use `python-dotenv` to load them in Python.
    ```bash
    pip install python-dotenv
    ```
    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()  # Load .env
    db_host = os.getenv("DB_HOST")
    debug_mode = os.getenv("DEBUG") == "True"
    ```

    ---

    ##### Use Branches
    If multiple people are developing or you want to add/fix features safely, Git branches are useful.
    > A branch is a “work divergence” in Git and allows multiple developments to proceed simultaneously within a single repository.{nl}
    > Changes in a branched line of work can be merged into other branches.

    Example branch strategy for small teams
    |Branch|Role|
    |---|---|
    |main|Production|
    |develop|Development|

    Create a branch
    ```bash
    # Create and switch to develop
    git checkout -b develop
    ```

    Separate web pages for `main` and `develop`
    ```bash
    # main
    git clone <repository_url>
    # develop
    git clone -b develop <repository_url>
    # Same method to update data
    git pull
    ```

    **Branch workflow**{nl}
    1. Develop on `develop`
    ```bash
    git checkout develop
    # --- Finish code changes ---
    git add .
    git commit -m "Add new feature"
    git push origin develop
    ```
    2. When `develop` is stable, merge into `main`
    ```bash
    git checkout main
    git merge --no-ff develop
    git push origin main
    ```
    """
)
st.caption("You can do the same operations via the VS Code UI.")

st.subheader("Understand Streamlit’s Behavior", divider=True)
st.markdown(
    f"""
    ##### Streamlit Uses a Re-execution Model
    In Streamlit, the entire script is re-executed whenever the user interacts with the app.
    For example, pressing a button runs the code from the top and re-renders the entire screen.
    As your app grows in size and render cost increases, the usability may degrade.
    > While the whole script re-executes, Python’s import semantics mean that `import` statements are only evaluated once.
    > Be careful when modules you import initialize state internally.

    ---

    ##### Use `st.session_state` for State Management
    When the script re-executes, ordinary variables are not preserved.
    Use `st.session_state` to retain values.
    As an example, a counter that increments each time a button is pressed can be written like this:
    ```python
    # Initialization
    if 'count' not in st.session_state:
        st.session_state['count'] = 0

    # Increment
    if st.button('Count up'):
        st.session_state['count'] += 1

    # Output
    st.write('Current count', st.session_state['count'])
    ```

    :warning: `st.session_state` will also reset in the following cases:
    - The browser-side session is lost (reload, closing the tab, network disconnection, etc.)
    - Server-side restart
    - Session timeout after long inactivity
    """
)
with st.expander("Write `st.session_state` operations in one line"):
    st.markdown(
        """
        Set a value
        ```python
        if 'count' not in st.session_state:
            st.session_state['count'] = 0

        # Single-line
        st.session_state.setdefault('count', 0)
        ```

        Get a value
        ```python
        if 'count' in st.session_state:
            x = st.session_state['count']
        else:
            x = 0

        # Single-line
        x = st.session_state.get('count', 0)
        ```
        """
    )

st.markdown(
    """
    ---

    ##### Single-threaded Behavior
    Streamlit basically runs **one thread per user**.
    When multiple users access simultaneously, the server handles them in separate threads and **state is not shared between users**.
    """
)

st.subheader("UI", divider=True)
st.markdown(
    f"""
    ##### Avoid Overly Fancy UIs
    Streamlit’s strength is fast development using a rich set of pre-built widgets.
    It helps to first understand what widgets are available.

    [API reference](https://docs.streamlit.io/develop/api-reference)

    You can craft advanced widgets on your own using HTML + CSS and complex conditionals.
    However, if development time becomes too long, you lose the advantages of using Streamlit.
    In such cases, it’s better to re-examine your app’s features and logic.

    ---

    ##### Two Ways to Retrieve Input
    **1. Use the widget’s return value**
    ```python
    result = st.radio("Judge", ["OK", "NG", "NA"])
    ```
    Suitable when you process the retrieved value immediately.

    **2. Reference the key assigned to the widget**
    ```python
    st.radio("Judge", ["OK", "NG", "NA"], key="design_check_judge")
    # ...
    result = st.session_state["design_check_judge"]
    ```
    If you assign a key when placing the widget, you can get its state from `st.session_state`.
    This is convenient when the placement code and the processing code are in different locations.

    > Keys must be unique across all widgets on the page, or you’ll get an error.{nl}
    > If you don’t set a key, Streamlit will auto-generate one internally.

    ---

    ##### Use Callbacks
    For example, to change `st.session_state` when a button is pressed:
    ```python
    if st.button('Push here'):
        st.session_state['saved'] = True
    ```
    Note: even if you press the button, it won’t be `True` until the button is re-rendered.
    If you reference `st.session_state['saved']` **before** placing the button, you may see unexpected behavior.

    If you want to apply changes immediately, use widget callbacks:
    ```python
    def func():
        st.session_state['saved'] = True

    st.button('Push here', on_click=func)
    ```
    With this approach, the callback function `func` runs immediately when the button is pressed, and then the whole app re-renders.
    This works well when you need immediate changes such as state updates or data writes.
    """
)

st.subheader("Reading & Writing Data", divider=True)
st.markdown(
    """
    ##### Use Static Files
    “Saving data = Database” is not always true.
    For read-only usage or low update frequency, static files such as `csv` or `json` are sufficient.
    """
)
with st.expander("Read JSON"):
    st.markdown(
        """
        ```python
        import json

        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        ```
        """
    )
with st.expander("Read CSV"):
    st.markdown(
        """
        ```python
        import csv

        rows = []
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)

        # You can also read the whole table with pandas
        import pandas as pd
        df = pd.read_csv(filepath, encoding="utf-8")
        ```
        """
    )

st.markdown(
    """
    ##### Use a Database
    If data is frequently updated, requires lots of searching/filtering, or is used by multiple users simultaneously, a database is safer and more efficient.
    ```
    << Under construction >>
    ```
    """
)

st.subheader("Restricting Access", divider=True)
st.markdown(
    f"""
    If you want to publish the app only to a limited set of members, consider creating a login form with `streamlit-authenticator`.

    [Sample code]("https://github.com/sfsmarit/streamlit-login-form")
    """
)

st.subheader("When Code Starts to Get Complex", divider=True)
st.markdown(
    f"""
    ##### Group Repeated Logic into Functions
    As your code grows, you may end up re-writing the same logic multiple times.
    By extracting it into functions, you can reuse code.
    ```python
    def greet(name: str):
        st.write('Hello', name)

    greet("Alice")
    ```

    ---

    ##### Split Modules
    When code is concentrated in a single file, it becomes hard to manage.
    Move common logic or cohesive features into separate `.py` files and import them to keep things organized.

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

    # Or
    import utils
    email = utils.generate_email_from_name("Tanaka")
    ```

    ---

    ##### Manage `session_state` Keys
    As your app grows, the number of keys in `st.session_state` increases.
    Since `st.session_state` behaves like a dictionary, **keys are not auto-completed by the IDE**.
    With many keys, it becomes hard to remember them and typos can lead to errors.

    A safe way to manage many keys is to use an enumeration (`Enum`).
    ```python
    from enum import Enum, auto

    # Define a Key class that inherits from Enum
    class Key(Enum):
        USER_NAME = auto()
        USER_EMAIL = auto()

    # Key.XXX can be auto-completed in the IDE
    st.text_input("User Name", key=Key.USER_NAME.name)
    ```
    An enumeration is a set of unique names, which fits the requirement that keys must be unique.
    Use the string form `Key.XXX.name` when assigning keys.
    """
)

st.subheader("Handling Heavy Workloads", divider=True)
st.markdown(
    f"""
    ##### Split the App into Multiple Pages
    If too many features are packed into a single page, splitting into multiple pages may improve performance.
    You can easily create multi-page navigation with `st.navigation`.
    ```python
    pages = [
        st.Page('introduction.py', title='Introduction', icon=':material/home:'),
        st.Page('handson.py', title='Hands-on', icon=':material/build:'),
        st.Page('tips.py', title='Tips', icon=":material/lightbulb_2:"),
    ]
    st.navigation(pages, position="sidebar", expanded=True).run()
    ```

    ---

    ##### Use Caching
    Streamlit provides two types of caching: `st.cache_data` and `st.cache_resource`.
    
    ||`st.cache_data`|`st.cache_resource`|
    |---|---|---|
    |Target|Computed results and data|External resources and connections|
    |Purpose|Cache deterministic results to avoid recomputation|Initialize costly resources once and reuse|
    |Examples|Expensive computations, static file loading, API responses|ML model loading, database connections|
    
    Example of `st.cache_data`
    ```python
    import pandas as pd
    
    @st.cache_data(ttl=300, show_spinner=True)  # Cache for 5 minutes
    def load_table(path: str, encoding: str = "utf-8") -> pd.DataFrame:
        return pd.read_csv(path, encoding=encoding)
    
    df = load_table("large_table.csv")
    ```

    Example of `st.cache_resource`
    ```python
    import joblib
    
    @st.cache_resource
    def load_model(path: str):
        return joblib.load(path)

    model = load_model("random_forest.pkl")
    ```

    ---

    ##### Be Transparent to the User
    Simply showing that “work is in progress” improves perceived performance.

    ```python
    # Show a spinner
    with st.spinner("Calculating..."):
        import time
        time.sleep(3)
    ```

    ```python
    # Show a progress bar
    import time
    pbar = st.progress(0, "Step-by-step progress")
    for i in range(3):
        time.sleep(1)
        pbar.progress(100*(i+1)/5)
    ```

    ---

    ##### Offload to a Separate Process
    """
)

with st.expander("Track progress with multiprocessing + Queues"):
    st.markdown(
        """
        ```python
        import streamlit as st
        import multiprocessing as mp
        import time

        # Initialize state
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
            done_q.put({'ok': True, 'summary': 'Processing completed'})

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

        st.title("Run in a separate process (multiprocessing)")

        if st.button("Start heavy work in a separate process"):
            start_process()
            st.info("Background processing started")

        poll_status()
        st.progress(st.session_state['progress'] / 100)
        if st.session_state['done']:
            st.success(st.session_state['msg'])

        if st.session_state['proc'] and st.button("Abort"):
            try:
                st.session_state['proc']['p'].terminate()
                st.session_state['proc']['p'].join(timeout=1)
                st.warning("Process aborted")
            finally:
                st.session_state['proc'] = None
                st.session_state['progress'] = 0
                st.session_state['done'] = False
                st.session_state['msg'] = ""
        ```
        """
    )

with st.expander("Submit functions with ProcessPoolExecutor"):
    st.markdown(
        """
        ```python
        import streamlit as st
        from concurrent.futures import ProcessPoolExecutor, Future
        import time

        # Shared Executor (avoid repeated init cost)
        @st.cache_resource
        def get_executor():
            # Adjust by CPU cores (e.g., 2–4)
            return ProcessPoolExecutor(max_workers=2)

        def heavy_return(n: int) -> dict:
            time.sleep(2)
            return {"input": n, "result": n * n}

        # Hold the Future in session
       tate:
            st.session_state["future"] = None

        executor = get_executor()
        st.title("Run in a separate process (ProcessPoolExecutor)")

        val = st.number_input("Input value", value=42, step=1)
        if st.button("Compute in a separate process"):
            st.session_state["future"] = executor.submit(heavy_return, int(val))
            st.info("Computation started (about 2 seconds)")

        # Check status
        fut: Future = st.session_state["future"]
        if fut:
            if fut.done():
                try:
                    res = fut.result()
                    st.success(f"Done: {res}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.spinner("Computing…")
        ```
        """
    )

with st.expander("Launch another script via subprocess"):
    st.markdown(
        """
        ```python
        import streamlit as st
        import subprocess
        import sys

        st.title("Run in a separate process (subprocess)")

        if st.button("Launch script (show logs)"):
            # Example: launch python worker.py and stream stdout
            # On Windows, prefer shell=False; combine with text=True if needed
            proc = subprocess.Popen(
                [sys.executable, "worker.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            st.session_state["subproc"] = proc
            st.info("Launched worker.py")

        # Read logs
        proc = st.session_state.get("subproc")
        if proc and proc.stdout:
            # Advance reading on each rerun (note: may block if no line is available)
            for _ in range(10):  # Example: read up to 10 lines per rerun
                line = proc.stdout.readline()
                if not line:
                    break
                st.write(line.rstrip())

            code = proc.poll()
            if code is not None:
                if code == 0:
                    st.success("worker.py exited normally")
                else:
                    st.error(f"worker.py exited abnormally (code: {code})")
                st.session_state["subproc"] = None
        ```
        """
    )
