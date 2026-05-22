import plotly.express as px
import pandas as pd


# -------------------------------------
# PIE CHART
# -------------------------------------

def create_energy_pie_chart(
    import_units,
    solar_generation,
    export_units
):

    self_consumption = (
        solar_generation - export_units
    )

    df = pd.DataFrame({

        "Category": [

            "Import Units",
            "Self Consumption",
            "Export Units"

        ],

        "Units": [

            import_units,
            self_consumption,
            export_units

        ]

    })

    fig = px.pie(

        df,
        names="Category",
        values="Units",
        title="Energy Distribution"

    )

    return fig


# -------------------------------------
# BAR CHART
# -------------------------------------

def create_bill_comparison_chart(
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
        title="Bill Comparison"

    )

    return fig
