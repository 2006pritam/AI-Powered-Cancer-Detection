import streamlit as st
from PIL import Image

# App Config
st.set_page_config(page_title="AI Powered Cancer Detection", page_icon="🩺", layout="wide")

# Sidebar Navigation
pages = ["🏠 Home", "🩺 Cancer Detection"]
choice = st.sidebar.radio("Navigate", pages)

# ---------------- HOME PAGE ----------------
if choice == "🏠 Home":
    st.image("https://www.skf.edu.in/images/skf-newlogo-new1.jpg?v=2", width=250)
    st.title("AI Powered Cancer Detection System")
    st.markdown("### Internship Project - Supreme Knowledge Foundation")
    
    st.markdown("---")
    st.subheader("👥 Project Team Members")
    
    if st.button("Show Team Members"):
        st.success("✅ Team Members:")
        st.write("- **Pritam Kumar Modak**")
        st.write("- **Roni Ghosh**")
        st.write("- **Rishav Paul**")
        st.write("- **Sohini Pal**")
        st.write("- **Soumen Pal**")

    st.markdown("---")
    st.info("This project is part of the internship program at **Supreme Knowledge Foundation**, focusing on AI-based cancer detection for research and educational purposes.")

# ---------------- CANCER DETECTION PAGE ----------------
elif choice == "🩺 Cancer Detection":
    st.title("AI-Powered Cancer Detection")
    st.write("Detect **Oral Cancer** and **Leukemia** using AI-powered assistance (UI Demo).")

    st.markdown("---")
    cancer_type = st.radio("Select Cancer Type:", ["Oral Cancer", "Leukemia"], horizontal=True)

    col1, col2 = st.columns([1, 2])

    # Oral Cancer Section
    if cancer_type == "Oral Cancer":
        with col1:
            st.image("https://github.com/2006pritam/AI-Powered-Cancer-Detection/blob/main/photos/tongue-cancer%20(1).jpg?raw=true", 
                     caption="Oral Cancer Example", use_container_width=True)
        with col2:
            st.subheader("👄 Oral Cancer Detection")
            st.write("""
            Oral cancer develops in the mouth region such as lips, tongue, gums, and inner lining of cheeks.  
            
            **Early Symptoms may include:**
            - White or red patches inside the mouth  
            - Persistent mouth sores  
            - Swelling in jaw  
            - Difficulty in swallowing  
            """)

    # Leukemia Section
    else:
        with col1:
            st.image("https://github.com/2006pritam/AI-Powered-Cancer-Detection/blob/main/photos/LeukemiaWBC_share.jpg?raw=true", 
                     caption="Leukemia Example", use_container_width=True)
        with col2:
            st.subheader("🩸 Leukemia Detection")
            st.write("""
            Leukemia is a type of blood cancer that originates in bone marrow and affects white blood cells.  

            **Early Symptoms may include:**
            - Frequent infections  
            - Fatigue and weakness  
            - Unexplained weight loss  
            - Easy bleeding or bruising  
            """)

    st.markdown("---")

    # Upload Section
    st.subheader("📤 Upload Medical Image for Testing")
    uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)
        st.success("✅ Image uploaded successfully! (Model prediction will be integrated here)")

    st.markdown("---")
    st.markdown("🔬 **Disclaimer:** This is an internship project UI demo. The results shown here are for educational purposes only. Always consult medical professionals for real diagnosis.")
