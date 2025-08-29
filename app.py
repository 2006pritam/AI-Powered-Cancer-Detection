import streamlit as st

# Sidebar Title
st.sidebar.title("AI Cancer Detection System")

# Main Navigation (Cancer Types)
cancer_type = st.sidebar.radio(
    "Select Cancer Type",
    ["Oral Cancer", "Leukemia Cancer"]
)

# Sub-navigation for Oral Cancer
if cancer_type == "Oral Cancer":
    option = st.sidebar.radio(
        "Oral Cancer Options",
        ["Home", "About", "Model Comparison", "Image Prediction", "Real-Time Detection", "History"]
    )

    if option == "Home":
        st.write("# 🏠 Oral Cancer Home")
    elif option == "About":
        st.write("# ℹ️ About Oral Cancer Detection")
    elif option == "Model Comparison":
        st.write("# 📊 Model Comparison (Oral Cancer)")
    elif option == "Image Prediction":
        st.write("# 🖼️ Image Prediction (Oral Cancer)")
    elif option == "Real-Time Detection":
        st.write("# 🎥 Real-Time Detection (Oral Cancer)")
    elif option == "History":
        st.write("# 🕒 History (Oral Cancer)")

# Sub-navigation for Leukemia Cancer
elif cancer_type == "Leukemia Cancer":
    option = st.sidebar.radio(
        "Leukemia Cancer Options",
        ["Home", "About", "Model Comparison", "Image Prediction", "Real-Time Detection", "History"]
    )

    if option == "Home":
        st.write("# 🏠 Leukemia Cancer Home")
    elif option == "About":
        st.write("# ℹ️ About Leukemia Cancer Detection")
    elif option == "Model Comparison":
        st.write("# 📊 Model Comparison (Leukemia Cancer)")
    elif option == "Image Prediction":
        st.write("# 🖼️ Image Prediction (Leukemia Cancer)")
    elif option == "Real-Time Detection":
        st.write("# 🎥 Real-Time Detection (Leukemia Cancer)")
    elif option == "History":
        st.write("# 🕒 History (Leukemia Cancer)")
