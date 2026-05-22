def calculate_bill_estimation(
    solar_data,
    current_bill_data
):

    result = {}

    try:

        # ---------------------------------
        # INPUTS
        # ---------------------------------

        import_units = float(
            solar_data.get(
                "Import Units",
                0
            )
        )

        solar_generation = float(
            solar_data.get(
                "Solar Generation",
                0
            )
        )

        without_solar_units = (
            import_units
            + solar_generation
        )

        # ---------------------------------
        # EXISTING CHARGES
        # ---------------------------------

        current_energy = 440610
        current_fac = 26102
        current_wheeling = 42286
        current_duty = 57289
        current_grid = 46935
        current_demand = 202150

        # ---------------------------------
        # UNIT MULTIPLIER
        # ---------------------------------

        multiplier = (
            without_solar_units
            / import_units
        )

        # ---------------------------------
        # WITHOUT SOLAR CHARGES
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

        # Grid support removed
        without_grid = 0

        # Demand same
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
        # STORE RESULTS
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
            "Tariff Calculation Error"
        }

    return result
