import streamlit as st
import pandas as pd

from utils.pdf_parser import (
    extract_bill_data
)

from utils.solar_calculator import (
    calculate_solar_analysis
)

from utils.tariff_engine import (
    estimate_without_solar_bill
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(

    page_title="DISCOM Bill Analysis",
    layout="wide"

)

# -----------------------------------
# TITLE
# -----------------------------------

st.title(
    "⚡ DISCOM Bill Analysis"
)

st.markdown(
    "### Rooftop Solar Net Metering Intelligence"
)

# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(

    "Upload MSEDCL Solar Bill",
    type=["pdf"]

)

# -----------------------------------
# PROCESS FILE
# -----------------------------------

if uploaded_file:

    # -----------------------------------
    # EXTRACT BILL DATA
    # -----------------------------------

    data = extract_bill_data(
        uploaded_file
    )

    # -----------------------------------
    # SOLAR ANALYSIS
    # -----------------------------------

    solar_analysis = (
        calculate_solar_analysis(
            data
        )
    )

    # -----------------------------------
    # BILL ESTIMATION
    # -----------------------------------

    estimated_bill = (
        estimate_without_solar_bill(

            data,
            solar_analysis

        )
    )

    # -----------------------------------
    # KPI SECTION
    # -----------------------------------

    st.subheader(
        "Financial Summary"
    )

    current_bill = data.get(
        "Current Bill",
        0
    )

    without_solar_bill = (
        estimated_bill.get(
            "Estimated Bill",
            0
        )
    )

    savings = (
        without_solar_bill
        - current_bill
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

        f"₹ {without_solar_bill:,.0f}"

    )

    col3.metric(

        "Estimated Savings",

        f"₹ {savings:,.0f}"

    )

    # -----------------------------------
    # ENERGY ANALYTICS
    # -----------------------------------

    st.subheader(
        "Energy Analytics"
    )

    col4, col5, col6 = (
        st.columns(3)
    )

    col4.metric(

        "Import Units",

        data.get(
            "Import Units",
            0
        )

    )

    col5.metric(

        "Solar Generation",

        data.get(
            "Solar Generation",
            0
        )

    )

    col6.metric(

        "Self Consumption",

        solar_analysis.get(
            "Self Consumption",
            0
        )

    )

    # -----------------------------------
    # SIDE BY SIDE COMPARISON
    # -----------------------------------

    st.subheader(
        "Charge Comparison"
    )

    comparison_data = []

    charges = [

        "Demand Charges",
        "Wheeling Charges",
        "Energy Charges",
        "TOD Charges",
        "FAC Charges",
        "Electricity Duty",
        "Tax on Sale",
        "Grid Support Charge"

    ]

    for charge in charges:

        comparison_data.append({

            "Charge": charge,

            "Current Bill": data.get(
                charge,
                0
            ),

            "Without Solar": estimated_bill.get(
                charge,
                0
            )

        })

    comparison_df = pd.DataFrame(
        comparison_data
    )

    st.dataframe(

        comparison_df,
        use_container_width=True

    )

    # -----------------------------------
    # RAW DATA
    # -----------------------------------

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
