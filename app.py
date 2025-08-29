from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st
# The streamlit_lottie library was mentioned in your original prompt,
# but not used in the provided snippets. I'm commenting it out if not needed.
# If you plan to use Lottie animations, uncomment the line below.
# from streamlit_lottie import st_lottie
import json
import base64
import io

# Set the page configuration with a tongue or mouth emoji as the page icon
st.set_page_config(page_title="Oral Cancer Detection",
                   page_icon="🦷", layout="wide")

# Load and display logo
try:
    # Ensure 'logo1.png' exists in the 'assets' folder
    st.logo("./assets/logo1.png", size="large", link=None, icon_image=None)
except FileNotFoundError:
    st.warning("Logo file not found. Please ensure 'assets/logo1.png' exists in your project.")

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
    with st.spinner(f"Loading {page_name}..."): # Added page_name to spinner message
        # Import and display content for each page
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
        menu_title=None,  # No title for the menu itself
        options=["Home", "About", "Model Comparison", "Image Prediction",
                 "Real-Time Detection", "History", "Oral Cancer", "Leukoplakia"], # Added new pages
        icons=["house", "info-circle", "list-task", "image", "camera-video",
               "clock-history", "mask", "disease"], # Icons for each page, 'mask' and 'disease' for new pages
        menu_icon="cast",  # Main menu icon
        default_index=0,  # Home page selected by default
        orientation="vertical",  # Vertical menu in sidebar
    )

# Call the function to display the selected page content
display_page(selected_page)
