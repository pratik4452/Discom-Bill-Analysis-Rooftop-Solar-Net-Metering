import streamlit as st
import pandas as pd

from utils.pdf_parser import (
    extract_bill_data
)

from utils.tariff_engine import (
    calculate_before_after_solar
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
    "⚡ DISCOM Solar Bill Intelligence"
)

st.markdown(
    "### Before Solar vs After Solar Analysis"
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
    # EXTRACT DATA
    # -----------------------------------

    data = extract_bill_data(
        uploaded_file
    )

    # -----------------------------------
    # CALCULATE
    # -----------------------------------

    analysis = (
        calculate_before_after_solar(
            data
        )
    )

    # -----------------------------------
    # KPI SECTION
    # -----------------------------------

    st.subheader(
        "Financial Summary"
    )

    after_bill = (
        analysis["Total Bill"]
        ["After Solar"]
    )

    before_bill = (
        analysis["Total Bill"]
        ["Before Solar"]
    )

    savings = (
        analysis["Savings"]
    )

    col1, col2, col3 = (
        st.columns(3)
    )

    col1.metric(

        "After Solar Bill",

        f"₹ {after_bill:,.0f}"

    )

    col2.metric(

        "Before Solar Bill",

        f"₹ {before_bill:,.0f}"

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

        "Before Solar Units",

        analysis.get(
            "Before Solar Units",
            0
        )

    )

    # -----------------------------------
    # SIDE-BY-SIDE TABLE
    # -----------------------------------

    st.subheader(
        "Before Solar vs After Solar"
    )

    table_data = []

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

        table_data.append({

            "Charge": charge,

            "After Solar":

                analysis[charge]
                ["After Solar"],

            "Before Solar":

                analysis[charge]
                ["Before Solar"]

        })

    comparison_df = pd.DataFrame(
        table_data
    )

    st.dataframe(

        comparison_df,
        use_container_width=True

    )

    # -----------------------------------
    # RAW EXTRACTED DATA
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
