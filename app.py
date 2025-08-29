import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar Title
st.sidebar.title("AI Cancer Detection System")

# First level menu (Cancer Types)
cancer_type = option_menu(
    menu_title=None,
    options=["Oral Cancer Detection", "Leukemia Cancer Detection"],
    icons=["capsule", "activity"],  # Choose icons from Bootstrap Icons
    menu_icon="hospital",
    default_index=0,
    orientation="vertical"
)

# Show sub-menu for Oral Cancer
if cancer_type == "Oral Cancer Detection":
    with st.sidebar:
        oral_option = option_menu(
            menu_title="Oral Cancer Detection",
            options=["Home", "About", "Model Comparison", "Image Prediction", "Real-Time Detection", "History"],
            icons=["house", "info-circle", "list-task", "image", "camera-video", "clock-history"],
            menu_icon="cast",
            default_index=0
        )

    # Display selected page
    if oral_option == "Home":
        st.write("# 🏠 Oral Cancer Home Page")
    elif oral_option == "About":
        st.write("# ℹ️ About Oral Cancer Detection")
    elif oral_option == "Model Comparison":
        st.write("# 📊 Oral Cancer Model Comparison")
    elif oral_option == "Image Prediction":
        st.write("# 🖼️ Oral Cancer Image Prediction")
    elif oral_option == "Real-Time Detection":
        st.write("# 🎥 Oral Cancer Real-Time Detection")
    elif oral_option == "History":
        st.write("# 🕒 Oral Cancer Detection History")

# Show sub-menu for Leukemia Cancer
elif cancer_type == "Leukemia Cancer Detection":
    with st.sidebar:
        leukemia_option = option_menu(
            menu_title="Leukemia Cancer Detection",
            options=["Home", "About", "Model Comparison", "Image Prediction", "Real-Time Detection", "History"],
            icons=["house", "info-circle", "list-task", "image", "camera-video", "clock-history"],
            menu_icon="cast",
            default_index=0
        )

    # Display selected page
    if leukemia_option == "Home":
        st.write("# 🏠 Leukemia Cancer Home Page")
    elif leukemia_option == "About":
        st.write("# ℹ️ About Leukemia Cancer Detection")
    elif leukemia_option == "Model Comparison":
        st.write("# 📊 Leukemia Cancer Model Comparison")
    elif leukemia_option == "Image Prediction":
        st.write("# 🖼️ Leukemia Cancer Image Prediction")
    elif leukemia_option == "Real-Time Detection":
        st.write("# 🎥 Leukemia Cancer Real-Time Detection")
    elif leukemia_option == "History":
        st.write("# 🕒 Leukemia Cancer Detection History")
