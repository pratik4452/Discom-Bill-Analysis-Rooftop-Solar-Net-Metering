def calculate_before_after_solar(data):

    result = {}

    try:

        # -----------------------------------
        # CURRENT VALUES
        # -----------------------------------

        import_units = data.get(
            "Import Units",
            0
        )

        solar_generation = data.get(
            "Solar Generation",
            0
        )

        export_units = data.get(
            "Export Units",
            0
        )

        # -----------------------------------
        # BEFORE SOLAR UNITS
        # -----------------------------------

        before_solar_units = (

            import_units
            + solar_generation

        )

        # -----------------------------------
        # MULTIPLIER
        # -----------------------------------

        if import_units > 0:

            multiplier = (
                before_solar_units
                / import_units
            )

        else:

            multiplier = 1

        # -----------------------------------
        # CHARGE LIST
        # -----------------------------------

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

        before_total = 0
        after_total = 0

        # -----------------------------------
        # CALCULATE BEFORE & AFTER
        # -----------------------------------

        for charge in charges:

            after_value = data.get(
                charge,
                0
            )

            before_value = (
                after_value
                * multiplier
            )

            result[charge] = {

                "After Solar": round(
                    after_value,
                    2
                ),

                "Before Solar": round(
                    before_value,
                    2
                )

            }

            after_total += after_value
            before_total += before_value

        # -----------------------------------
        # TOTALS
        # -----------------------------------

        result["Total Bill"] = {

            "After Solar": round(
                after_total,
                2
            ),

            "Before Solar": round(
                before_total,
                2
            )

        }

        result["Savings"] = round(

            before_total
            - after_total,

            2

        )

        result["Before Solar Units"] = (
            before_solar_units
        )

    except:

        result["Error"] = (
            "Calculation Error"
        )

    return result
