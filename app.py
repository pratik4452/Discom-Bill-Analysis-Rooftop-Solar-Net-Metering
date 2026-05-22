import streamlit as st
import pandas as pd

from utils.pdf_parser import extract_bill_data
from utils.solar_calculator import (
    calculate_without_solar
)

st.set_page_config(
    page_title="DISCOM Bill Analysis",
    layout="wide"
)

st.title(
    "⚡ DISCOM Bill Analysis"
)

uploaded_file = st.file_uploader(
    "Upload MSEDCL Solar Bill",
    type=["pdf"]
)

if uploaded_file:

    # -------------------------------
    # EXTRACT BILL DATA
    # -------------------------------

    bill_data = extract_bill_data(
        uploaded_file
    )

    st.subheader(
        "Extracted Bill Details"
    )

    bill_df = pd.DataFrame(
        bill_data.items(),
        columns=["Parameter", "Value"]
    )

    st.table(bill_df)

    # -------------------------------
    # SOLAR CALCULATIONS
    # -------------------------------

    solar_results = (
        calculate_without_solar(
            bill_data
        )
    )

    st.subheader(
        "Solar Savings Analysis"
    )

    solar_df = pd.DataFrame(
        solar_results.items(),
        columns=["Parameter", "Value"]
    )

    st.table(solar_df)

    # -------------------------------
    # KPI METRICS
    # -------------------------------

    if (
        "Without Solar Units"
        in solar_results
    ):

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Without Solar Units",
            solar_results[
                "Without Solar Units"
            ]
        )

        col2.metric(
            "Solar Generation",
            solar_results[
                "Solar Generation"
            ]
        )

        col3.metric(
            "Self Consumption",
            solar_results[
                "Self Consumption"
            ]
        )
