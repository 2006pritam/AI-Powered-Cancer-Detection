import streamlit as st

def show_home_content():
    st.title("Welcome to the AI-Powered Cancer Detection App 🦷🔬")
    st.markdown("---")

    st.header("Empowering Early Detection of Oral Cancers")
    st.write(
        "This application leverages advanced Artificial Intelligence to assist in the **early detection of oral cancer and leukoplakia**. "
        "Our goal is to provide an accessible and intuitive platform for preliminary screening, "
        "helping users and healthcare professionals identify potential concerns faster, leading to quicker diagnoses and better patient outcomes."
    )
    st.markdown("---")

    st.header("What We Detect")
    
    st.subheader("Oral Cancer")
    # Corrected parameter here: use_column_width -> use_container_width
    st.image("https://placehold.co/600x250/FF6347/FFFFFF?text=Oral+Cancer+Image", caption="Illustrative example of Oral Cancer", use_container_width=True)
    st.write(
        "Oral cancer, also known as mouth cancer, can affect any part of the mouth. "
        "Early signs can often be subtle, but timely detection is critical for successful treatment. "
        "Our AI models are trained to analyze images for suspicious lesions and patterns associated with oral cancer."
    )
    st.markdown("---")

    st.subheader("Leukoplakia")
    # Corrected parameter here: use_column_width -> use_container_width
    st.image("https://placehold.co/600x250/98FB98/000000?text=Leukoplakia+Image", caption="Illustrative example of Leukoplakia", use_container_width=True)
    st.write(
        "Leukoplakia presents as **thickened, white patches** on the mucous membranes of the mouth. "
        "While many cases are benign, it is considered a **precancerous condition**, meaning it has the potential to develop into cancer. "
        "This app helps identify these patches, prompting further medical evaluation."
    )
    st.markdown("---")

    st.header("Technology Powering Our App 🤖")
    st.write(
        "Our detection system is built upon a foundation of cutting-edge machine learning and deep learning technologies:"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("PyTorch")
        # Corrected parameter here: use_column_width -> use_container_width
        st.image("https://img.icons8.com/color/96/pytorch.png", caption="PyTorch Icon", use_container_width=True)
        st.write(
            "The core of our **deep learning models** is built using **PyTorch**, a powerful open-source machine learning framework. "
            "It enables us to develop and train complex neural networks for highly accurate image analysis."
        )

    with col2:
        st.subheader("Google Colab")
        # Corrected parameter here: use_column_width -> use_container_width
        st.image("https://img.icons8.com/color/96/google-colab.png", caption="Google Colab Icon", use_container_width=True)
        st.write(
            "Development and experimentation were primarily conducted on **Google Colaboratory (Colab)**. "
            "This cloud-based platform provided the necessary computational resources, including GPUs, for efficient model training and prototyping."
        )

    with col3:
        st.subheader("Scikit-learn & NumPy")
        # Corrected parameter here: use_column_width -> use_container_width
        st.image("https://img.icons8.com/color/96/scikit-learn.png", caption="Scikit-learn Icon", use_container_width=True)
        st.write(
            "For classical machine learning tasks, data preprocessing, and numerical operations, we leverage **scikit-learn** "
            "(including algorithms like **K-Nearest Neighbors (KNN)** and **K-Means Clustering**) alongside **NumPy** for high-performance array computing. "
            "These tools are essential for feature engineering and statistical analysis."
        )
    st.markdown("---")

    st.warning(
        "**Disclaimer:** This application is intended as a supplementary screening tool and for educational purposes only. "
        "It does not provide medical advice, diagnosis, or treatment. Always consult with a qualified healthcare professional "
        "for any health concerns or before making any decisions related to your health or treatment."
    )
