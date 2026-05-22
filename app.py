import streamlit as st
from utils.pdf_parser import extract_bill_data

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

    # Extract PDF Data
    bill_data = extract_bill_data(uploaded_file)

    st.subheader("Extracted Bill Data")

    st.write(bill_data)
