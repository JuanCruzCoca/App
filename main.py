import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("Img/photo.jpg" , width=300)

with col2:
    st.title("Juan Cruz Coca")
    content = """
    I am a software engineer with a passion for data science and machine learning. I have experience in Python, R, and SQL, 
    and I am always eager to learn new technologies and improve my skills. 
    I enjoy working on challenging projects that require creative problem-solving and collaboration with others.
    In my free time, I like to read about new trends in technology, 
    play video games, and spend time with my family and friends.
    """
    st.info(content)