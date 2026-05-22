def estimate_without_solar_bill(

    data,
    solar_analysis

):

    result = {}

    try:

        current_units = data.get(
            "Import Units",
            0
        )

        without_solar_units = (
            solar_analysis.get(
                "Without Solar Units",
                0
            )
        )

        multiplier = (
            without_solar_units
            / current_units
        )

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

        total = 0

        for charge in charges:

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

            total += estimated_value

        result["Estimated Bill"] = round(
            total,
            2
        )

    except:

        result["Error"] = (
            "Bill Estimation Error"
        )

    return result
