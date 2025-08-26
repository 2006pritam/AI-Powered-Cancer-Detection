import streamlit as st
from PIL import Image

# Set up the page with a wider layout and a professional theme
st.set_page_config(
    page_title="AI-Powered Cancer Detection",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a modern, clean look
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
        color: #1a1a1a;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    .st-bu {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        border: none;
    }
    .st-bu:hover {
        background-color: #45a049;
    }
    .st-bk {
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        padding: 15px;
        margin-bottom: 20px;
    }
    .st-bk:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }
    .st-ex {
        background-color: #e6f7ff;
        border-left: 6px solid #2196F3;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation with a clean title
st.sidebar.title("🧬 Navigation")
pages = ["🏠 Home", "🔬 Detection"]
choice = st.sidebar.radio("", pages)

# ---------------- HOME PAGE ----------------
if choice == "🏠 Home":
    st.image("https://www.skf.edu.in/images/skf-newlogo-new1.jpg?v=2", width=200)
    st.title("AI-Powered Cancer Detection System")
    st.markdown("### Internship Project | Supreme Knowledge Foundation")
    
    st.markdown("---")
    
    st.subheader("Project Overview")
    st.write("This project utilizes a deep learning model to assist in the preliminary detection of oral cancer and leukemia from medical images. This tool is designed for **research and educational purposes** to support the medical community.")
    
    st.markdown("---")
    
    # Use columns to neatly display team members
    st.subheader("👥 The Project Team")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.info("Pritam Kumar Modak")
    with col2:
        st.info("Roni Ghosh")
    with col3:
        st.info("Rishav Paul")
    with col4:
        st.info("Sohini Pal")
    with col5:
        st.info("Soumen Pal")

    st.markdown("---")
    st.markdown('<div class="st-ex"><b>Disclaimer:</b> This application is a UI demo for an internship project. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified health provider with any questions you may have regarding a medical condition.</div>', unsafe_allow_html=True)

# ---------------- CANCER DETECTION PAGE ----------------
elif choice == "🔬 Detection":
    st.title("🔬 AI-Powered Detection")
    st.write("Select a cancer type below and upload an image for AI-assisted analysis.")

    st.markdown("---")
    
    # Add a custom-styled radio button or tabs for a better look
    cancer_type = st.radio("Select Cancer Type:", ["Oral Cancer 👄", "Leukemia 🩸"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("---")
    
    # Create two columns for a clean layout
    info_col, upload_col = st.columns([1, 1])

    with info_col:
        # Oral Cancer Section
        if cancer_type == "Oral Cancer 👄":
            st.markdown('<div class="st-bk">', unsafe_allow_html=True)
            st.subheader("👄 Oral Cancer")
            st.image("https://github.com/2006pritam/AI-Powered-Cancer-Detection/blob/main/photos/tongue-cancer%20(1).jpg?raw=true", caption="Oral Cancer Example", use_container_width=True)
            st.write("""
            **Oral cancer** develops in the tissues of the mouth, including the lips, tongue, gums, and inner cheeks. **Early detection is crucial** for a better prognosis.
            
            **Common symptoms can include:**
            - White or red patches in the mouth.
            - Persistent sores that don't heal.
            - Swelling in the jaw.
            - Difficulty or pain when swallowing.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # Leukemia Section
        else:
            st.markdown('<div class="st-bk">', unsafe_allow_html=True)
            st.subheader("🩸 Leukemia")
            st.image("https://github.com/2006pritam/AI-Powered-Cancer-Detection/blob/main/photos/LeukemiaWBC_share.jpg?raw=true", caption="Leukemia Example", use_container_width=True)
            st.write("""
            **Leukemia** is a type of blood cancer that begins in the bone marrow, leading to an overproduction of abnormal white blood cells.
            
            **Common symptoms can include:**
            - Frequent infections and fever.
            - Persistent fatigue and weakness.
            - Unexplained weight loss.
            - Easy bleeding or bruising.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    with upload_col:
        st.markdown('<div class="st-bk">', unsafe_allow_html=True)
        st.subheader("📤 Upload Medical Image")
        uploaded_file = st.file_uploader("Choose an image file (JPG/PNG)", type=["jpg", "png", "jpeg"])
        
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image", use_container_width=True)
            
            # Use a spinner to simulate a busy state
            with st.spinner('Analyzing image...'):
                # Simulate a delay for a more realistic feel
                import time
                time.sleep(2)
                
            st.success("✅ Image successfully analyzed!")
            st.info("The AI model predicts: [Prediction will be shown here]")
            st.warning("⚠️ **Reminder:** This result is for educational purposes only.")

        st.markdown('</div>', unsafe_allow_html=True)
