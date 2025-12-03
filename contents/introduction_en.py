import streamlit as st

nl = "  "


st.set_page_config(page_title="Introduction")
st.title("How to Build Business Web Apps with Python + Streamlit")

st.subheader("Purpose", divider=True)
st.markdown(
    f"""
    The goal is to enable non-IT engineers to develop apps that streamline repetitive tasks and share them with their team. {nl}
    """
)

st.subheader("Features of Web Apps", divider=True)
st.markdown(
    f"""
    :white_check_mark: **Advantages**
    - For developers:
      - Easy distribution and updates
      - Centralized management (users cannot modify the app)
    - For users:
      - Low technical barrier to use
      - Minimal environment dependency (usable with just a browser)
    
    :no_entry: **Disadvantages**
    - Higher development cost compared to macros or scripts
    - Requires a server to run the app
    - Security restrictions (limited file access)
    
    >Web apps are effective for standardizing team workflows. {nl}
    >However, they are not suitable for tasks like processing large amounts of local data.
    """
)

st.subheader("What is Streamlit ?", divider=True)
st.markdown(
    """
    Streamlit is an open-source framework that makes it easy to build web apps with Python.
    It was founded in 2018 to quickly visualize data analysis results and became open source the following year.
    
    :white_check_mark: **Advantages**
    - Built entirely with Python
        - No need for frontend knowledge (HTML, CSS, JavaScript, etc.)
        - Great for learning data analysis
    - Fast development
        - Create UI with minimal code
        - Real-time code updates
        - Rich preset UI components with good design
    - Strong in data visualization
        - Graphs: Matplotlib, Plotly
        - Table data: Pandas
        - Machine learning demos

    :no_entry: **Disadvantages**
    - Difficult to create complex UIs
    - Not suitable for large-scale apps
    - Limited performance

    >Streamlit is best described as a library specialized for “building small apps quickly.”
    """
)

st.subheader("What kind of apps is it suitable for ?", divider=True)
st.markdown(
    f"""
    :white_check_mark: **Recommended**
    - Used within a team or department
    - Small-scale
    - No heavy data processing or massive concurrent access
    - Frequent customization
    - Prototyping
    
    :no_entry: **Consider other options if**
    - Used across multiple departments or only by yourself
    - Large-scale or multi-functional
    - High load
    - Critical internal systems
    - Requires local file access
    - Needs IT expertise for development or operation

    >If technically or operationally challenging, consult your IT team.
    """
)

st.subheader("Development Flow", divider=True)
st.markdown(
    """
    1. Set up the development environment
    2. Build the app locally
    3. Deploy to a server and share the app
    
    Details are explained on the next page.
    """
)

st.subheader("Background Knowledge", divider=True)
st.markdown("Read this section if you're interested.")

st.markdown("---")

st.markdown("##### How a typical web app works")
st.markdown(
    f"""
    1. **Client/Server**{nl}
    The client is the browser operated by the user, displaying screens and sending input.
    The server runs the application, located on an internal server or in the cloud, receiving requests from the browser and returning processed results.

    2. **HTTP Request/Response**{nl}
    When the browser accesses a URL, it sends an HTTP request.
    This uses methods like GET or POST to request data.
    The server processes the request and returns an HTTP response containing HTML, JSON, images, etc.
    Page navigation and button actions rely on this request-response cycle.

    3. **Frontend/Backend**{nl}
    The frontend builds the UI using HTML, CSS, and JavaScript.
    The backend handles logic and data processing, using Python, databases, and business rules.
    Typical web apps separate frontend and backend with different languages, but Streamlit generates the UI using Python alone.

    4. **Routing**{nl}
    Standard web apps switch content based on URLs like /home or /items/123.
    Streamlit uses `st.Page` or `st.navigation` for page switching.

    5. **State Management**{nl}
    Apps need to maintain “state” like form inputs, temporary settings, or login status.
    Typical web apps use JavaScript, cookies, or localStorage, while Streamlit uses a dictionary called `st.session_state`.

    6. **Database**{nl}
    Simple data can be stored in static files like CSV or JSON.
    For more complex data or frequent updates/searches, use databases like SQLite or MariaDB.
    Databases enable efficient queries and support concurrent access.

    ---
    
    ##### Why Streamlit is not ideal for large-scale apps
    
    1. **Re-execution model overhead**{nl}
    Streamlit re-runs the entire script whenever the user interacts. For large apps, this increases cost and slows response.
    Features like `st.cache_data` and `st.fragment` can help mitigate this.

    2. **Complex state management**{nl}
    State across pages or many users depends on `st.session_state`.
    Large apps require careful key management to avoid collisions.
    Advanced authentication and permissions need extra design or external services.

    3. **Code bloat**{nl}
    Streamlit combines UI and logic in Python, making files grow quickly.
    To prevent this, organize the project and separate responsibilities (UI, logic, data access).

    4. **Scalability limits**{nl}
    Streamlit runs as a single process; more concurrent users increase CPU/memory load.
    Large-scale use requires load balancing or containerization.

    5. **Customization constraints**{nl}
    Streamlit prioritizes simplicity in UI creation, making complex layouts or dynamic UIs difficult.
    It lacks the flexibility of frontend frameworks like React or Vue.

    >Streamlit can still be used for large apps, but due to its limitations in extensibility and performance, other web development approaches are often preferable.
    """
)
