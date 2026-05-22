def calculate_without_solar(data):

    result = {}

    try:

        import_units = int(
            str(data.get("Import Units", 0))
            .replace(",", "")
        )

        solar_generation = int(
            str(data.get("Solar Generation", 0))
            .replace(",", "")
        )

        export_units = int(
            str(data.get("Export Units", 0))
            .replace(",", "")
        )

        # ---------------------------------
        # TOTAL CONSUMPTION
        # ---------------------------------

        total_consumption = (
            import_units + solar_generation
        )

        # ---------------------------------
        # SELF CONSUMPTION
        # ---------------------------------

        self_consumption = (
            solar_generation - export_units
        )

        # ---------------------------------
        # SOLAR SAVINGS UNITS
        # ---------------------------------

        solar_offset = (
            self_consumption + export_units
        )

        result["Import Units"] = import_units

        result["Solar Generation"] = solar_generation

        result["Export Units"] = export_units

        result["Self Consumption"] = (
            self_consumption
        )

        result["Without Solar Units"] = (
            total_consumption
        )

        result["Solar Offset Units"] = (
            solar_offset
        )

    except:

        result["Error"] = (
            "Calculation Error"
        )

    return result
