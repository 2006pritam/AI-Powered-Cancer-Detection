from streamlit_option_menu import option_menu
import streamlit as st

# Set the page configuration with a tongue or mouth emoji as the page icon
st.set_page_config(page_title="Oral Cancer Detection",
                   page_icon="🦷", layout="wide")

# Logo URL provided by the user
LOGO_URL = "https://images.squarespace-cdn.com/content/v1/67463f2cc9d406701fbea2d3/e7053cca-131e-499b-b9aa-83d44838328b/caialogo_transparent.png"

# Display the logo using the URL
st.logo(LOGO_URL, size="large", link=None, icon_image=None)

# Corrected sidebar title for better branding
st.sidebar.title("Oral Cancer Detection App")

# Merged and corrected CSS blocks
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
        height: 100vh;
    }
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }

    /* This CSS hides Streamlit's native sidebar pages */
    .st-emotion-cache-16txte5.e1g8pov61 .st-emotion-cache-1f19z17.e1g8pov61 {
        display: none !important;
    }
    
    .st-emotion-cache-1f19z17.e1g8pov61 {
        display: none !important;
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
        elif page_name == "Oral Cancer":
            import pages.Oral_cancer as oral_cancer
            oral_cancer.show_oral_cancer()
        elif page_name == "Leukoplakia":
            import pages.Leukoplakia as leukoplakia
            leukoplakia.show_leukoplakia()
        elif page_name == "Oral Cancer - Image Prediction":
            import pages.Image_prediction as image_prediction
            image_prediction.show_image_prediction()
        elif page_name == "Oral Cancer - Real-Time Detection":
            import pages.Real_time_detection as real_time_detection
            real_time_detection.show_real_time_detection()
        elif page_name == "Leukoplakia - Image Prediction":
            import pages.Image_prediction as image_prediction
            image_prediction.show_image_prediction()
        elif page_name == "Leukoplakia - History":
            import pages.History as history
            history.show_history()

# Sidebar for navigation using option_menu
with st.sidebar:
    selected_page = option_menu(
        menu_title=None,
        options=["Home", "About", "---",
                 "Oral Cancer", "Oral Cancer - Image Prediction", "Oral Cancer - Real-Time Detection", "---",
                 "Leukoplakia", "Leukoplakia - Image Prediction", "Leukoplakia - History"],
        icons=["house", "info-circle", "caret-right",
               "mask", "image", "camera-video", "caret-right",
               "disease", "image", "clock-history"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# Call the function to display the selected page content
display_page(selected_page)
