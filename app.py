import streamlit as st
import pandas as pd

from utils.pdf_parser import (
    extract_bill_data
)

from utils.tariff_engine import (
    estimate_without_solar_bill
)

st.set_page_config(

    page_title="DISCOM Bill Analysis",
    layout="wide"

)

st.title(
    "⚡ DISCOM Solar Bill Intelligence"
)

uploaded_file = st.file_uploader(

    "Upload MSEDCL Solar Bill",
    type=["pdf"]

)

if uploaded_file:

    # ---------------------------------
    # EXTRACT DATA
    # ---------------------------------

    data = extract_bill_data(
        uploaded_file
    )

    # ---------------------------------
    # ESTIMATE WITHOUT SOLAR
    # ---------------------------------

    estimated = (
        estimate_without_solar_bill(
            data
        )
    )

    # ---------------------------------
    # KPI
    # ---------------------------------

    st.subheader(
        "Financial Summary"
    )

    current_bill = data.get(
        "Current Bill",
        0
    )

    estimated_bill = estimated.get(
        "Estimated Bill Without Solar",
        0
    )

    savings = (
        estimated_bill
        - current_bill
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Current Bill",
        f"₹ {current_bill:,.0f}"
    )

    col2.metric(
        "Without Solar Bill",
        f"₹ {estimated_bill:,.0f}"
    )

    col3.metric(
        "Estimated Savings",
        f"₹ {savings:,.0f}"
    )

    # ---------------------------------
    # SIDE-BY-SIDE TABLE
    # ---------------------------------

    st.subheader(
        "Side-by-Side Charge Analysis"
    )

    comparison_data = []

    charge_list = [

        "Demand Charges",
        "Wheeling Charges",
        "Energy Charges",
        "TOD Charges",
        "FAC Charges",
        "Electricity Duty",
        "Tax on Sale",
        "Grid Support Charge"

    ]

    for charge in charge_list:

        comparison_data.append({

            "Charge":

                charge,

            "Current Bill":

                data.get(charge, 0),

            "Without Solar":

                estimated.get(charge, 0)

        })

    comparison_df = pd.DataFrame(
        comparison_data
    )

    st.dataframe(

        comparison_df,
        use_container_width=True

    )

    # ---------------------------------
    # RAW EXTRACTED DATA
    # ---------------------------------

    st.subheader(
        "Extracted Bill Data"
    )

    raw_df = pd.DataFrame(

        data.items(),
        columns=["Parameter", "Value"]

    )

    st.dataframe(

        raw_df,
        use_container_width=True

    )
