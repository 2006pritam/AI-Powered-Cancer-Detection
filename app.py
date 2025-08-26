import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Cancer Detection App",
    page_icon="🩺",
    layout="wide"
)

# Header
st.title("🩺 AI-Powered Cancer Detection")
st.markdown("### Detect **Oral Cancer** and **Leukemia** with AI Assistance")
st.write("This application is designed for research & educational purposes. Upload your medical images and explore AI-based diagnostic support.")

st.markdown("---")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966488.png", width=100)
st.sidebar.title("⚙️ Options")
cancer_type = st.sidebar.radio("Select Cancer Type", ["Oral Cancer", "Leukemia"])
st.sidebar.info("Choose a cancer type and upload image for detection.")

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    if cancer_type == "Oral Cancer":
        st.image("https://www.indiatoday.in/diabetes-myths-and-facts/assets/oral-cancer-2.jpg", caption="Oral Cancer Example", use_container_width=True)
    else:
        st.image("https://www.researchgate.net/profile/Asma-Mahmoud-3/publication/331013169/figure/fig1/AS:726640285278209@1550481713902/Leukemia-cells-under-the-microscope.png", caption="Leukemia Example", use_container_width=True)

with col2:
    if cancer_type == "Oral Cancer":
        st.subheader("👄 Oral Cancer Detection")
        st.write("""
        Oral cancer refers to cancer that develops in any part of the mouth 
        (lips, gums, tongue, inner lining of cheeks, roof and floor of mouth).
        
        **Early Symptoms:**
        - White or red patches inside the mouth  
        - Persistent mouth sores  
        - Swelling in jaw  
        - Difficulty in swallowing  
        """)
    else:
        st.subheader("🩸 Leukemia Detection")
        st.write("""
        Leukemia is a type of blood cancer that originates in the bone marrow 
        and affects white blood cells.

        **Early Symptoms:**
        - Frequent infections  
        - Fatigue and weakness  
        - Unexplained weight loss  
        - Easy bleeding or bruising  
        """)

st.markdown("---")

# Upload Section
st.subheader("📤 Upload Your Image")
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    st.success("✅ Image uploaded successfully!")
    st.markdown("🚀 *AI model prediction will appear here in future integration.*")

# Footer
st.markdown("---")
st.markdown("🔬 **Disclaimer:** This tool is for research & educational purposes only. Always consult a medical professional for accurate diagnosis.")
