from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st
import json
import base64
import io

# Set the page configuration with a tongue or mouth emoji as the page icon
st.set_page_config(page_title="Cancer Detection",
                   page_icon="🦷", layout="wide")

# Logo URL provided by the user
LOGO_URL = "https://images.squarespace-cdn.com/content/v1/67463f2cc9d406701fbea2d3/e7053cca-131e-499b-b9aa-83d44838328b/caialogo_transparent.png"

# Display the logo using the URL
st.logo(LOGO_URL, size="large", link=None, icon_image=None)

st.sidebar.title("Oral Cancer Detection")

# Add CSS for the spinner (can be customized further)
st.markdown(
    """
    <style>
    .streamlit-spinner {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;  /* Full height for centering */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to display the selected page content
def display_page(page_name):
    with st.spinner(f"Loading {page_name}..."):
        if page_name == "Home":
            import pages.Home as home
            home.show_home_content()
        elif page_name == "About":
            import pages.About as about
            about.show_about()
        elif page_name == "Model Comparison":
            import pages.Model_comparison as model_comparison
            model_comparison.show_model_comparison()
        elif page_name == "Image Prediction":
            import pages.Image_prediction as image_prediction
            image_prediction.show_image_prediction()
        elif page_name == "Real-Time Detection":
            import pages.Real_time_detection as real_time_detection
            real_time_detection.show_real_time_detection()
        elif page_name == "History":
            import pages.History as history
            history.show_history()
        elif page_name == "Oral Cancer":
            import pages.Oral_cancer as oral_cancer
            oral_cancer.show_oral_cancer()
        elif page_name == "Leukoplakia":
            import pages.Leukoplakia as leukoplakia
            leukoplakia.show_leukoplakia()

# Sidebar for navigation using option_menu
with st.sidebar:
    selected_page = option_menu(
        menu_title=None,
        options=["Home", "About", "Model Comparison", "Image Prediction",
                 "Real-Time Detection", "History", "Oral Cancer", "Leukoplakia"],
        icons=["house", "info-circle", "list-task", "image", "camera-video",
               "clock-history", "mask", "disease"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# Call the function to display the selected page content
display_page(selected_page)
