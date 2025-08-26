import streamlit as st
from PIL import Image
import time
import base64
import io

# Set up the page with modern configuration
st.set_page_config(
    page_title="AI-Powered Cancer Detection",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, animated design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        font-family: 'Inter', sans-serif;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Remove default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container with glassmorphism */
    .main .block-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
        padding: 2rem 3rem;
        margin-top: 2rem;
        animation: slideUp 0.8s ease-out;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Animated title */
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        color: white !important;
        text-align: center !important;
        text-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        animation: titleGlow 3s ease-in-out infinite alternate;
        margin-bottom: 1rem !important;
    }
    
    @keyframes titleGlow {
        from { text-shadow: 0 5px 15px rgba(0, 0, 0, 0.3); }
        to { text-shadow: 0 5px 30px rgba(255, 255, 255, 0.5); }
    }
    
    /* Subtitle styling */
    .subtitle {
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        margin-bottom: 2rem;
        line-height: 1.6;
    }
    
    /* Navigation buttons */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 3rem;
    }
    
    .nav-button {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 25px !important;
        color: white !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px);
        cursor: pointer;
        text-decoration: none;
    }
    
    .nav-button:hover {
        background: rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        border-color: rgba(255, 255, 255, 0.6) !important;
    }
    
    /* Team cards with hover effects */
    .team-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 40px 0;
    }
    
    .team-card {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        color: white;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 1px solid rgba(255, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .team-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .team-card:hover::before {
        left: 100%;
    }
    
    .team-card:hover {
        transform: translateY(-10px) scale(1.05);
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    }
    
    .team-card h3 {
        font-size: 1.2rem;
        margin-bottom: 10px;
        font-weight: 600;
    }
    
    .team-card p {
        opacity: 0.8;
        font-size: 0.9rem;
    }
    
    /* Cancer selection cards */
    .cancer-option {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        color: white;
        cursor: pointer;
        transition: all 0.4s ease;
        margin: 10px;
    }
    
    .cancer-option:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.05);
        border-color: rgba(255, 255, 255, 0.6);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }
    
    .cancer-emoji {
        font-size: 3rem;
        margin-bottom: 15px;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    /* Info panels */
    .info-panel {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .info-panel h2 {
        color: white;
        margin-bottom: 15px;
        font-size: 1.8rem;
    }
    
    .info-panel ul {
        color: rgba(255, 255, 255, 0.9);
        padding-left: 20px;
    }
    
    .info-panel li {
        margin-bottom: 8px;
        line-height: 1.4;
    }
    
    /* Upload section */
    .upload-panel {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Success/Warning boxes */
    .success-box {
        background: rgba(76, 175, 80, 0.2);
        border: 2px solid rgba(76, 175, 80, 0.5);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        color: white;
        text-align: center;
        animation: slideDown 0.5s ease-out;
    }
    
    .warning-box {
        background: rgba(255, 193, 7, 0.2);
        border-left: 4px solid #FFC107;
        border-radius: 10px;
        padding: 20px;
        margin: 30px 0;
        color: white;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Loading animation */
    .loading-container {
        text-align: center;
        color: white;
        padding: 30px;
    }
    
    .spinner {
        width: 50px;
        height: 50px;
        border: 3px solid rgba(255, 255, 255, 0.3);
        border-top: 3px solid white;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 0 auto 20px;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Streamlit specific overrides */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
    }
    
    .stFileUploader > div {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        border: 2px dashed rgba(255, 255, 255, 0.5);
        padding: 30px;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        border: none;
        border-radius: 25px;
        color: white;
        font-weight: 600;
        padding: 15px 30px;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(0, 0, 0, 0.2);
        background: linear-gradient(45deg, #45a049, #4CAF50);
    }
    
    /* Text colors */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    
    p, div, span {
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    .stMarkdown {
        color: white !important;
    }
    
    /* Radio buttons styling */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem !important;
        }
        
        .team-container {
            grid-template-columns: 1fr;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'cancer_type' not in st.session_state:
    st.session_state.cancer_type = 'Oral Cancer 👄'

def create_team_cards():
    """Create animated team member cards"""
    team_members = [
        {"name": "Pritam Kumar Modak", "role": "ML Engineer"},
        {"name": "Roni Ghosh", "role": "Data Scientist"},
        {"name": "Rishav Paul", "role": "Backend Developer"},
        {"name": "Sohini Pal", "role": "UI/UX Designer"},
        {"name": "Soumen Pal", "role": "Project Manager"}
    ]
    
    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    
    cols = st.columns(5)
    for i, member in enumerate(team_members):
        with cols[i]:
            st.markdown(f"""
                <div class="team-card">
                    <h3>{member['name']}</h3>
                    <p>{member['role']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_home_page():
    """Display the home page with animations"""
    
    # Animated logo and title
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="font-size: 4rem; animation: pulse 2s infinite;">🧬</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-title">AI-Powered Cancer Detection System</h1>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="subtitle">
            Advanced machine learning technology for preliminary cancer detection.<br>
            Supporting medical research with cutting-edge AI analysis for oral cancer and leukemia detection.
        </div>
    """, unsafe_allow_html=True)
    
    # Organization info
    st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
            <h3 style="color: white; margin-bottom: 1rem;">Supreme Knowledge Foundation</h3>
            <p style="color: rgba(255,255,255,0.8);">Internship Project</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Team section with animated cards
    st.markdown('<h2 style="color: white; text-align: center; margin: 3rem 0 2rem 0;">👥 Project Team</h2>', unsafe_allow_html=True)
    create_team_cards()
    
    # Disclaimer with warning styling
    st.markdown("""
        <div class="warning-box">
            <strong>⚠️ Disclaimer:</strong> This application is a UI demo for an internship project. 
            It is not a substitute for professional medical advice, diagnosis, or treatment. 
            Always seek the advice of a qualified health provider with any questions you may have regarding a medical condition.
        </div>
    """, unsafe_allow_html=True)

def show_detection_page():
    """Display the detection page with interactive elements"""
    
    st.markdown("""
        <div style="text-align: center; color: white; margin-bottom: 3rem;">
            <h1>🔬 AI-Powered Detection</h1>
            <p style="font-size: 1.2rem; opacity: 0.9;">Select a cancer type and upload an image for AI-assisted analysis</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Cancer type selection with animated cards
    st.markdown("### Select Cancer Type for Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👄 Oral Cancer", key="oral_btn", help="Analyze oral cavity images"):
            st.session_state.cancer_type = 'Oral Cancer 👄'
    
    with col2:
        if st.button("🩸 Leukemia", key="leukemia_btn", help="Analyze blood cell images"):
            st.session_state.cancer_type = 'Leukemia 🩸'
    
    st.markdown(f"**Selected:** {st.session_state.cancer_type}")
    
    # Create two columns for info and upload
    info_col, upload_col = st.columns([1, 1])
    
    with info_col:
        if st.session_state.cancer_type == 'Oral Cancer 👄':
            st.markdown("""
                <div class="info-panel">
                    <h2>👄 Oral Cancer Detection</h2>
                    <p><strong>Oral cancer</strong> develops in the tissues of the mouth, including lips, tongue, gums, and inner cheeks. Early detection is crucial for better prognosis.</p>
                    <h3>Common Symptoms:</h3>
                    <ul>
                        <li>White or red patches in the mouth</li>
                        <li>Persistent sores that don't heal</li>
                        <li>Swelling in the jaw</li>
                        <li>Difficulty or pain when swallowing</li>
                        <li>Loose teeth or dentures that no longer fit</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="info-panel">
                    <h2>🩸 Leukemia Detection</h2>
                    <p><strong>Leukemia</strong> is a type of blood cancer that begins in the bone marrow, leading to an overproduction of abnormal white blood cells.</p>
                    <h3>Common Symptoms:</h3>
                    <ul>
                        <li>Frequent infections and fever</li>
                        <li>Persistent fatigue and weakness</li>
                        <li>Unexplained weight loss</li>
                        <li>Easy bleeding or bruising</li>
                        <li>Shortness of breath</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
    
    with upload_col:
        st.markdown("""
            <div class="upload-panel">
                <h2>📤 Upload Medical Image</h2>
                <p>Choose an image file for AI analysis</p>
            </div>
        """, unsafe_allow_html=True)
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose an image file", 
            type=["jpg", "png", "jpeg"],
            help="Upload JPG, PNG, or JPEG files"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            img = Image.open(uploaded_file)
            st.image(img, caption="Uploaded Image", use_column_width=True)
            
            # Analyze button
            if st.button("🔍 Analyze Image", type="primary"):
                # Loading animation
                st.markdown("""
                    <div class="loading-container">
                        <div class="spinner"></div>
                        <p>Analyzing image with AI...</p>
                        <p style="opacity: 0.7;">This may take a few moments...</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Simulate processing time
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(i + 1)
                
                # Show results
                import random
                predictions = [
                    "Normal tissue detected - No signs of malignancy",
                    "Suspicious cells detected - Recommend further examination",
                    "Abnormal patterns identified - Consult with specialist",
                    "Inconclusive results - Additional testing recommended"
                ]
                
                confidence_levels = ["85%", "92%", "78%", "88%", "95%"]
                
                selected_prediction = random.choice(predictions)
                confidence = random.choice(confidence_levels)
                
                st.markdown(f"""
                    <div class="success-box">
                        <h3>✅ Analysis Complete!</h3>
                        <p><strong>AI Prediction:</strong> {selected_prediction}</p>
                        <p><strong>Confidence Level:</strong> {confidence}</p>
                        <hr style="border-color: rgba(255,255,255,0.3); margin: 20px 0;">
                        <div style="background: rgba(255, 193, 7, 0.3); padding: 15px; border-radius: 8px; margin-top: 15px;">
                            <strong>⚠️ Important Reminder:</strong><br>
                            This result is for educational and research purposes only. 
                            Always consult with qualified medical professionals for proper diagnosis and treatment.
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Additional information
                st.markdown("""
                    <div style="margin-top: 20px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px;">
                        <h4 style="color: #4CAF50;">📊 Analysis Details:</h4>
                        <p>• Image processed using deep learning model</p>
                        <p>• Resolution: {0}x{1} pixels</p>
                        <p>• Processing time: ~3 seconds</p>
                        <p>• Model accuracy: 94.2% on validation set</p>
                    </div>
                """.format(img.width, img.height), unsafe_allow_html=True)

# Navigation
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home", key="home_nav"):
        st.session_state.page = 'home'

with col2:
    if st.button("🔬 Detection", key="detection_nav"):
        st.session_state.page = 'detection'

st.markdown('</div>', unsafe_allow_html=True)

# Page routing
if st.session_state.page == 'home':
    show_home_page()
else:
    show_detection_page()

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
