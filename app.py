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

from utils.charts import (

    create_energy_pie_chart,
    create_bill_comparison_chart

)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(

    page_title="DISCOM Bill Analysis",
    layout="wide"

)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title(
    "⚡ DISCOM Bill Analysis Dashboard"
)

st.markdown(
    "### AI-Based Rooftop Solar Savings Intelligence"
)

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(

    "Upload MSEDCL Solar Bill",
    type=["pdf"]

)

# ---------------------------------------------------
# PROCESS FILE
# ---------------------------------------------------

if uploaded_file:

    # ---------------------------------------------------
    # EXTRACT BILL DATA
    # ---------------------------------------------------

    bill_data = extract_bill_data(
        uploaded_file
    )

    # ---------------------------------------------------
    # SOLAR CALCULATIONS
    # ---------------------------------------------------

    solar_results = (
        calculate_without_solar(
            bill_data
        )
    )

    # ---------------------------------------------------
    # BILL ESTIMATION
    # ---------------------------------------------------

    estimated_bill = (
        calculate_bill_estimation(
            solar_results,
            bill_data
        )
    )

    # ---------------------------------------------------
    # TOTALS
    # ---------------------------------------------------

    try:

        with_solar_bill = (
            estimated_bill["TOTAL BILL"]
            ["With Solar"]
        )

        without_solar_bill = (
            estimated_bill["TOTAL BILL"]
            ["Without Solar"]
        )

        savings = (
            without_solar_bill
            - with_solar_bill
        )

    except:

        with_solar_bill = 0
        without_solar_bill = 0
        savings = 0

    # ---------------------------------------------------
    # KPI CARDS
    # ---------------------------------------------------

    st.subheader(
        "Key Financial Insights"
    )

    col1, col2, col3 = (
        st.columns(3)
    )

    col1.metric(

        "Current Bill",
        f"₹ {with_solar_bill:,.0f}"

    )

    col2.metric(

        "Without Solar Bill",
        f"₹ {without_solar_bill:,.0f}"

    )

    col3.metric(

        "Estimated Savings",
        f"₹ {savings:,.0f}"

    )

    # ---------------------------------------------------
    # ENERGY KPI
    # ---------------------------------------------------

    st.subheader(
        "Energy Analytics"
    )

    col4, col5, col6 = (
        st.columns(3)
    )

    col4.metric(

        "Import Units",

        solar_results.get(
            "Import Units",
            0
        )

    )

    col5.metric(

        "Solar Generation",

        solar_results.get(
            "Solar Generation",
            0
        )

    )

    col6.metric(

        "Self Consumption",

        solar_results.get(
            "Self Consumption",
            0
        )

    )

    # ---------------------------------------------------
    # CHARTS
    # ---------------------------------------------------

    st.subheader(
        "Visual Analytics"
    )

    import_units = (
        solar_results.get(
            "Import Units",
            0
        )
    )

    solar_generation = (
        solar_results.get(
            "Solar Generation",
            0
        )
    )

    export_units = (
        solar_results.get(
            "Export Units",
            0
        )
    )

    pie_chart = (
        create_energy_pie_chart(

            import_units,
            solar_generation,
            export_units

        )
    )

    bar_chart = (
        create_bill_comparison_chart(

            with_solar_bill,
            without_solar_bill

        )
    )

    col7, col8 = st.columns(2)

    with col7:

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    with col8:

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    # ---------------------------------------------------
    # SIDE-BY-SIDE BILL COMPARISON
    # ---------------------------------------------------

    st.subheader(
        "With Solar vs Without Solar"
    )

    comparison_rows = []

    for charge, values in (
        estimated_bill.items()
    ):

        if isinstance(values, dict):

            comparison_rows.append({

                "Charges": charge,

                "With Solar":
                values.get(
                    "With Solar",
                    "-"
                ),

                "Without Solar":
                values.get(
                    "Without Solar",
                    "-"
                )

            })

    comparison_df = pd.DataFrame(
        comparison_rows
    )

    st.dataframe(

        comparison_df,

        use_container_width=True

    )

    # ---------------------------------------------------
    # RAW DATA TABLES
    # ---------------------------------------------------

    st.subheader(
        "Extracted Bill Details"
    )

    bill_df = pd.DataFrame(

        bill_data.items(),
        columns=["Parameter", "Value"]

    )

    st.dataframe(
        bill_df,
        use_container_width=True
    )

    st.subheader(
        "Solar Calculation Details"
    )

    solar_df = pd.DataFrame(

        solar_results.items(),
        columns=["Parameter", "Value"]

    )

    st.dataframe(
        solar_df,
        use_container_width=True
    )
