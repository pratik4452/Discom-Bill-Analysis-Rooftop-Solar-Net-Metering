import streamlit as st
import pandas as pd

from utils.pdf_parser import extract_bill_data

st.set_page_config(
    page_title="DISCOM Bill Analysis",
    layout="wide"
)

st.title("⚡ DISCOM Bill Analysis")

uploaded_file = st.file_uploader(
    "Upload MSEDCL Solar Bill",
    type=["pdf"]
)

if uploaded_file:

    data = extract_bill_data(uploaded_file)

    st.subheader("Extracted Bill Details")

    df = pd.DataFrame(
        data.items(),
        columns=["Parameter", "Value"]
    )

    st.table(df)

    # -----------------------------------
    # WITHOUT SOLAR CALCULATION
    # -----------------------------------

    if (
        "Import Units" in data
        and "Solar Generation" in data
    ):

        import_units = int(data["Import Units"])
        solar_units = int(data["Solar Generation"])

        without_solar_units = (
            import_units + solar_units
        )

        st.subheader("Solar Savings Analysis")

        st.metric(
            "Without Solar Consumption",
            f"{without_solar_units} Units"
        )
