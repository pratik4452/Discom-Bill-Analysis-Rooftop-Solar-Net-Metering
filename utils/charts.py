import plotly.express as px
import pandas as pd


def create_bill_chart(
    current_bill,
    without_solar_bill
):

    df = pd.DataFrame({

        "Scenario": [

            "With Solar",
            "Without Solar"

        ],

        "Bill Amount": [

            current_bill,
            without_solar_bill

        ]

    })

    fig = px.bar(

        df,
        x="Scenario",
        y="Bill Amount",
        title="Solar Savings Comparison"

    )

    return fig
