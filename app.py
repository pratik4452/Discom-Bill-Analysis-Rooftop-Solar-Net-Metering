import streamlit as st

st.set_page_config(
    page_title="DISCOM Bill Analysis",
    layout="wide"
)

st.title("⚡ DISCOM Bill Analysis")

st.write("Upload DISCOM Net Metering Bill")

uploaded_file = st.file_uploader(
    "Upload PDF Bill",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")
