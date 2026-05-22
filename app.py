import streamlit as st
import pandas as pd

from utils.pdf_parser import (
    extract_bill_data
)

from utils.solar_calculator import (
    calculate_without_solar
)

from utils.charts import (
    create_bill_chart
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
    "### Rooftop Solar With vs Without Analysis"
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

    without_solar = (
        calculate_without_solar(
            bill_data
        )
    )

    # -----------------------------------
    # KPI
    # -----------------------------------

    current_bill = bill_data.get(
        "Current Bill",
        0
    )

    without_solar_bill = (
        without_solar.get(
            "Without Solar Bill",
            0
        )
    )

    savings = (
        without_solar_bill
        - current_bill
    )

    st.subheader(
        "Financial Summary"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "With Solar Bill",
        f"₹ {current_bill:,.0f}"
    )

    c2.metric(
        "Without Solar Bill",
        f"₹ {without_solar_bill:,.0f}"
    )

    c3.metric(
        "Estimated Savings",
        f"₹ {savings:,.0f}"
    )

    # -----------------------------------
    # SIDE BY SIDE COMPARISON
    # -----------------------------------

    st.subheader(
        "With Solar vs Without Solar"
    )

    comparison_df = pd.DataFrame({

        "Parameter": [

            "Demand Charges",
            "Wheeling Charges",
            "Energy Charges",
            "TOD Charges",
            "FAC Charges",
            "Electricity Duty",
            "Tax on Sale",
            "Grid Support Charge",
            "Debit Bill Adjustment"

        ],

        "With Solar": [

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
                "TOD Charges",
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

        ],

        "Without Solar": [

            without_solar.get(
                "Demand Charges",
                0
            ),

            without_solar.get(
                "Wheeling Charges",
                0
            ),

            without_solar.get(
                "Energy Charges",
                0
            ),

            without_solar.get(
                "TOD Charges",
                0
            ),

            without_solar.get(
                "FAC Charges",
                0
            ),

            without_solar.get(
                "Electricity Duty",
                0
            ),

            without_solar.get(
                "Tax on Sale",
                0
            ),

            without_solar.get(
                "Grid Support Charge",
                0
            ),

            without_solar.get(
                "Debit Bill Adjustment",
                0
            )

        ]

    })

    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    # -----------------------------------
    # CHART
    # -----------------------------------

    chart = create_bill_chart(

        current_bill,
        without_solar_bill

    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )
