import streamlit as st

# Logo URL from the main app for consistency
LOGO_URL = "https://images.squarespace-cdn.com/content/v1/67463f2cc9d406701fbea2d3/e7053cca-131e-499b-b9aa-83d44838328b/caialogo_transparent.png"

def show_about():
    st.image(LOGO_URL, width=200)
    st.title("About This Project 🧑‍🔬")
    st.markdown("---")

    st.header("Project Overview")
    st.write(
        "This application is an **internship project** developed at **Calcutta University**. "
        "The project's primary purpose is to leverage Artificial Intelligence and Machine Learning "
        "to assist in the preliminary detection of oral cancer and leukoplakia, contributing to early diagnosis."
    )
    st.write(
        "The application serves as a proof of concept, demonstrating the power of modern "
        "computer vision models in addressing real-world healthcare challenges."
    )
    st.markdown("---")

    st.header("Our Mentor")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://media.licdn.com/dms/image/v2/D4D22AQFn27VYsiAobw/feedshare-shrink_800/feedshare-shrink_800/0/1684152138886?e=2147483647&v=beta&t=Ooow-22aLZXo8ZCVTnEquTiYQHnYmzcv7Ps1mG-ILHs", 
                 caption="Dr. Arpan Murmu", use_container_width=True)
    
    with col2:
        st.subheader("Dr. Arpan Murmu")
        st.write("A.I./M.L. and Machine Learning Researcher at Calcutta University.")
        st.write("Dr. Murmu's expertise in AI and Machine Learning was instrumental in guiding the development "
                 "of the project's core algorithms and model architecture.")
    
    st.markdown("---")

    st.header("Developed by")
    st.write("This project was developed by students as part of their academic internship.")
    st.info("Developed by: [Your Name(s) Here]")
