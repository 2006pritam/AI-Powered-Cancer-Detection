import streamlit as st

st.set_page_config(page_title="AI Cancer Detection System", page_icon="🧪", layout="wide")

# ------------------ Logo ------------------
logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZP24UBvfPqQX9tO8c7CrQxUw8Id9XV5Zu6Q&s"

# Sidebar Title + Logo
st.sidebar.image(logo_url, use_container_width=True)  # ✅ updated param
st.sidebar.title("AI Cancer Detection System")

# ------------------ Main Navigation ------------------
cancer_type = st.sidebar.radio(
    "Select Cancer Type",
    ["Oral Cancer", "Leukemia Cancer"]
)

# ------------------ Oral Cancer ------------------
if cancer_type == "Oral Cancer":
    option = st.sidebar.radio(
        "Oral Cancer Options",
        ["Home", "About", "Model Comparison", "Image Prediction", "Real-Time Detection", "History"]
    )

    if option == "Home":
        st.image(logo_url, width=120)  # width is fine to keep here
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

# ------------------ Leukemia Cancer ------------------
elif cancer_type == "Leukemia Cancer":
    option = st.sidebar.radio(
        "Leukemia Cancer Options",
        ["Home", "About", "Model Comparison", "Image Prediction", "Real-Time Detection", "History"]
    )

    if option == "Home":
        st.image(logo_url, width=120)
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
