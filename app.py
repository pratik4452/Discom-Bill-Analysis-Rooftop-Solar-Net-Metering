import streamlit as st
import pandas as pd

from utils.pdf_parser import (
    extract_bill_data
)

from utils.solar_calculator import (
    calculate_without_solar
)

from utils.tariff_engine import (
    calculate_bill_estimation
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

    # ---------------------------------
    # EXTRACT DATA
    # ---------------------------------

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

    # ---------------------------------
    # SOLAR ANALYSIS
    # ---------------------------------

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

    # ---------------------------------
    # BILL ESTIMATION
    # ---------------------------------

    if (
        "Without Solar Units"
        in solar_results
    ):

        without_solar_units = (
            solar_results[
                "Without Solar Units"
            ]
        )

        estimated_bill = (
            calculate_bill_estimation(
                without_solar_units
            )
        )

        st.subheader(
            "Estimated Bill Without Solar"
        )

        estimated_df = pd.DataFrame(
            estimated_bill.items(),
            columns=["Parameter", "Value"]
        )

        st.table(estimated_df)

        # ---------------------------------
        # KPI METRICS
        # ---------------------------------

        current_bill = (
            bill_data.get(
                "Bill Amount",
                0
            )
        )

        estimated_total = (
            estimated_bill.get(
                "Estimated Bill",
                0
            )
        )

        try:

            current_bill = float(
                str(current_bill)
                .replace(",", "")
            )

            savings = (
                estimated_total
                - current_bill
            )

        except:

            savings = 0

        st.subheader(
            "Savings Summary"
        )

        col1, col2, col3 = (
            st.columns(3)
        )

        col1.metric(
            "Current Bill",
            f"₹ {current_bill:,.0f}"
        )

        col2.metric(
            "Without Solar Bill",
            f"₹ {estimated_total:,.0f}"
        )

        col3.metric(
            "Estimated Savings",
            f"₹ {savings:,.0f}"
        )
