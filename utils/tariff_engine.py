def estimate_without_solar_bill(data):

    result = {}

    try:

        import_units = data.get(
            "Import Units",
            0
        )

        solar_generation = data.get(
            "Solar Generation",
            0
        )

        total_units = (
            import_units
            + solar_generation
        )

        multiplier = (
            total_units
            / import_units
        )

        # ---------------------------------
        # SCALE ALL CHARGES
        # ---------------------------------

        charge_list = [

            "Demand Charges",
            "Wheeling Charges",
            "Energy Charges",
            "TOD Charges",
            "FAC Charges",
            "Electricity Duty",
            "Tax on Sale",
            "Grid Support Charge"

        ]

        total_bill = 0

        for charge in charge_list:

            current_value = data.get(
                charge,
                0
            )

            estimated_value = (
                current_value
                * multiplier
            )

            result[charge] = round(
                estimated_value,
                2
            )

            total_bill += estimated_value

        result["Without Solar Units"] = (
            round(total_units, 2)
        )

        result["Estimated Bill Without Solar"] = (
            round(total_bill, 2)
        )

    except:

        result["Error"] = (
            "Estimation Error"
        )

    return result
