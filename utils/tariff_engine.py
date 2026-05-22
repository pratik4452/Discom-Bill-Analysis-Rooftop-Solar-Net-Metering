def safe_float(value):

    try:

        return float(
            str(value)
            .replace(",", "")
        )

    except:

        return 0


def calculate_bill_estimation(
    solar_data,
    current_bill_data
):

    result = {}

    try:

        # ---------------------------------
        # UNITS
        # ---------------------------------

        import_units = safe_float(
            solar_data.get(
                "Import Units",
                0
            )
        )

        solar_generation = safe_float(
            solar_data.get(
                "Solar Generation",
                0
            )
        )

        without_solar_units = (
            import_units
            + solar_generation
        )

        multiplier = 1

        if import_units > 0:

            multiplier = (
                without_solar_units
                / import_units
            )

        # ---------------------------------
        # EXTRACT ACTUAL CHARGES
        # ---------------------------------

        current_energy = safe_float(
            current_bill_data.get(
                "Energy Charges",
                0
            )
        )

        current_fac = safe_float(
            current_bill_data.get(
                "FAC Charges",
                0
            )
        )

        current_wheeling = safe_float(
            current_bill_data.get(
                "Wheeling Charges",
                0
            )
        )

        current_duty = safe_float(
            current_bill_data.get(
                "Electricity Duty",
                0
            )
        )

        current_grid = safe_float(
            current_bill_data.get(
                "Grid Support Charges",
                0
            )
        )

        current_demand = safe_float(
            current_bill_data.get(
                "Demand Charges",
                0
            )
        )

        # ---------------------------------
        # WITHOUT SOLAR
        # ---------------------------------

        without_energy = (
            current_energy
            * multiplier
        )

        without_fac = (
            current_fac
            * multiplier
        )

        without_wheeling = (
            current_wheeling
            * multiplier
        )

        without_duty = (
            current_duty
            * multiplier
        )

        without_grid = 0

        without_demand = (
            current_demand
        )

        # ---------------------------------
        # TOTALS
        # ---------------------------------

        with_solar_total = (

            current_energy
            + current_fac
            + current_wheeling
            + current_duty
            + current_grid
            + current_demand

        )

        without_solar_total = (

            without_energy
            + without_fac
            + without_wheeling
            + without_duty
            + without_grid
            + without_demand

        )

        savings = (
            without_solar_total
            - with_solar_total
        )

        # ---------------------------------
        # RESULT TABLE
        # ---------------------------------

        result = {

            "Demand Charges": {

                "With Solar":
                round(current_demand, 2),

                "Without Solar":
                round(without_demand, 2)

            },

            "Wheeling Charges": {

                "With Solar":
                round(current_wheeling, 2),

                "Without Solar":
                round(without_wheeling, 2)

            },

            "Energy Charges": {

                "With Solar":
                round(current_energy, 2),

                "Without Solar":
                round(without_energy, 2)

            },

            "FAC Charges": {

                "With Solar":
                round(current_fac, 2),

                "Without Solar":
                round(without_fac, 2)

            },

            "Electricity Duty": {

                "With Solar":
                round(current_duty, 2),

                "Without Solar":
                round(without_duty, 2)

            },

            "Grid Support Charges": {

                "With Solar":
                round(current_grid, 2),

                "Without Solar":
                round(without_grid, 2)

            },

            "TOTAL BILL": {

                "With Solar":
                round(with_solar_total, 2),

                "Without Solar":
                round(without_solar_total, 2)

            },

            "TOTAL SAVINGS": {

                "With Solar": "-",

                "Without Solar":
                round(savings, 2)

            }

        }

    except:

        result = {
            "Error":
            "Calculation Error"
        }

    return result
