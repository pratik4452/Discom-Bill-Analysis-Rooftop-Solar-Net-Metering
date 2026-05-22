def calculate_solar_analysis(data):

    result = {}

    try:

        import_units = data.get(
            "Import Units",
            0
        )

        export_units = data.get(
            "Export Units",
            0
        )

        solar_generation = data.get(
            "Solar Generation",
            0
        )

        # -----------------------------------
        # WITHOUT SOLAR UNITS
        # -----------------------------------

        without_solar_units = (

            import_units
            + solar_generation

        )

        # -----------------------------------
        # SELF CONSUMPTION
        # -----------------------------------

        self_consumption = (

            solar_generation
            - export_units

        )

        # -----------------------------------
        # SOLAR OFFSET
        # -----------------------------------

        solar_offset = (

            self_consumption
            + export_units

        )

        result["Without Solar Units"] = (
            without_solar_units
        )

        result["Self Consumption"] = (
            self_consumption
        )

        result["Solar Offset Units"] = (
            solar_offset
        )

    except:

        result["Error"] = (
            "Calculation Error"
        )

    return result
