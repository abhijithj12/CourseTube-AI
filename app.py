import streamlit as st
from crew import Youtubecrew
from memory import create_table_courses, save_course, get_cached_course
from validation import url_validation


st.title("CourseTube AI")

if 'course' not in st.session_state:
    st.session_state['course'] = None

create_table_courses()

url = st.text_input("Enter YouTube URL here")

if st.button("Generate"):
    try:
        if not url_validation(url):
            st.error("Please enter a valid YouTube URL")

        else:
            cached_course = get_cached_course(url)

            if cached_course:
                st.session_state['course'] = cached_course

            else:
                with st.spinner("Generating Please Wait....."):
                    ytc = Youtubecrew().crew().kickoff(
                        inputs={"video_url": url}
                    )

                save_course(url, ytc.raw)

                st.session_state['course'] = ytc.raw

        if st.session_state['course']:
            st.markdown(st.session_state['course'])

    except Exception as e:
        st.error(f"An error occurred: {e}")