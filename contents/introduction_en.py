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

st.subheader("Features of Web Applications", divider=True)
st.markdown(
    """
    ##### :white_check_mark: Advantages
    Web applications offer significant benefits for both developers and users.  
    - For developers, distributing and updating the app is extremely easy. Once deployed on a server, all users can access the latest version without manual updates. In addition, centralized code management prevents unauthorized modifications and version inconsistencies.  
    - For users, all that’s needed is a browser—no special setup or technical knowledge required. Web apps are also less dependent on operating systems or device types, which is a major advantage.

    ##### :no_entry: Disadvantages
    There are some drawbacks to consider.  
    - Development generally takes more time compared to local macros or scripts  
    - A server is required to run the application  
    - Security restrictions apply (e.g., limited access to local files)

    > Web applications are ideal for tasks that need to be shared among multiple people or standardized processes.  
    > However, they are not well-suited for handling large volumes of local data.
    """
)


st.subheader("What is Streamlit?", divider=True)
st.markdown(
    """
    Streamlit is an open-source framework that makes it easy to build web applications using Python.  
    It was founded in 2018 with the goal of quickly visualizing data analysis results and became open source the following year.
    
    ##### :white_check_mark: Advantages
    Built entirely with Python  
    - No need for front-end knowledge (HTML, CSS, JavaScript, etc.)

    Rapid development  
    - Create UI with minimal code  
    - Rich set of pre-built UI components  
    - Real-time updates when code changes

    Strong for data visualization  
    - Graphs: Matplotlib, Plotly  
    - Tabular data: Pandas  
    - Machine learning support

    ##### :no_entry: Disadvantages
    - Difficult to build complex UIs  
    - Not suitable for large-scale applications  
    - Performance limitations

    > Streamlit is best described as a library specialized for building small-scale apps quickly.
    """
)


st.subheader("What Kind of Apps is Streamlit Best For?", divider=True)
st.markdown(
    """
    ##### :white_check_mark: Recommended Use Cases
    - Used within a team or department  
    - Small-scale applications  
    - No heavy data processing or high concurrent access  
    - Frequent customization required  
    - Prototyping

    ##### :no_entry: When to Consider Other Options
    - Used across multiple departments or by a single person only  
    - Large-scale or multi-functional systems  
    - High-load scenarios  
    - Critical internal systems  
    - Requires direct access to local files  
    - Development and maintenance demand specialized IT knowledge

    > If technical or operational challenges arise, consult your IT team.
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
