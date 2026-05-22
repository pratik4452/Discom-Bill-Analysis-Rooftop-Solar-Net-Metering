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
    "⚡ DISCOM Bill Analysis Dashboard"
)

st.markdown(
    "### AI-Based Rooftop Solar Savings Intelligence"
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

    bill_data = extract_bill_data(
        uploaded_file
    )

    solar_results = (
        calculate_without_solar(
            bill_data
        )
    )

    # -----------------------------------
    # FINANCIAL SUMMARY
    # -----------------------------------

    current_bill = (
        bill_data.get(
            "Bill Amount",
            0
        )
    )

    without_solar_units = (
        solar_results.get(
            "Without Solar Units",
            0
        )
    )

    estimated_bill = (
        calculate_bill_estimation(
            without_solar_units
        )
    )

    estimated_total = (
        estimated_bill.get(
            "Estimated Bill",
            0
        )
    )

    savings = (
        estimated_total
        - current_bill
    )

    # -----------------------------------
    # KPI
    # -----------------------------------

    st.subheader(
        "Financial Summary"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Current Bill",
        f"₹ {current_bill:,.0f}"
    )

    c2.metric(
        "Without Solar Bill",
        f"₹ {estimated_total:,.0f}"
    )

    c3.metric(
        "Estimated Savings",
        f"₹ {savings:,.0f}"
    )

    # -----------------------------------
    # CHARGE BREAKDOWN
    # -----------------------------------

    st.subheader(
        "Tariff Breakdown"
    )

    debit_data = {

        "Parameter": [

            "Demand Charges",
            "Wheeling Charges",
            "Energy Charges",
            "TOD Tariff EC",
            "FAC Charges",
            "Electricity Duty",
            "Tax on Sale",
            "Grid Support Charge",
            "Debit Bill Adjustment"

        ],

        "Amount": [

            bill_data.get(
                "Demand Charges",
                0
            ),

            bill_data.get(
                "Wheeling Charges",
                0
            ),

            bill_data.get(
                "Energy Charges",
                0
            ),

            bill_data.get(
                "TOD Tariff EC",
                0
            ),

            bill_data.get(
                "FAC Charges",
                0
            ),

            bill_data.get(
                "Electricity Duty",
                0
            ),

            bill_data.get(
                "Tax on Sale",
                0
            ),

            bill_data.get(
                "Grid Support Charge",
                0
            ),

            bill_data.get(
                "Debit Bill Adjustment",
                0
            )

        ]

    }

    credit_data = {

        "Parameter": [

            "Prompt Payment Discount",
            "Load Factor Incentive",
            "Incremental Rebate",
            "Bulk Consumption Rebate"

        ],

        "Amount": [

            bill_data.get(
                "Prompt Payment Discount",
                0
            ),

            bill_data.get(
                "Load Factor Incentive",
                0
            ),

            bill_data.get(
                "Incremental Rebate",
                0
            ),

            bill_data.get(
                "Bulk Consumption Rebate",
                0
            )

        ]

    }

    d1, d2 = st.columns(2)

    with d1:

        st.markdown(
            "### Debit Charges"
        )

        st.dataframe(
            pd.DataFrame(debit_data),
            use_container_width=True
        )

    with d2:

        st.markdown(
            "### Credit Adjustments"
        )

        st.dataframe(
            pd.DataFrame(credit_data),
            use_container_width=True
        )

    # -----------------------------------
    # CHARTS
    # -----------------------------------

    st.subheader(
        "Visual Analytics"
    )

    pie_chart = (
        create_energy_pie_chart(

            solar_results.get(
                "Import Units",
                0
            ),

            solar_results.get(
                "Solar Generation",
                0
            ),

            solar_results.get(
                "Export Units",
                0
            )

        )
    )

    bar_chart = (
        create_bill_comparison_chart(

            current_bill,
            estimated_total

        )
    )

    p1, p2 = st.columns(2)

    with p1:

        st.plotly_chart(
            pie_chart,
            use_container_width=True
        )

    with p2:

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )
