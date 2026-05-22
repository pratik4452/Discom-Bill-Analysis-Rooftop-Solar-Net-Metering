def calculate_without_solar(data):

    result = {}

    try:

        # ---------------------------------
        # SAFE VALUE CONVERSION
        # ---------------------------------

        import_units = int(

            str(
                data.get(
                    "Import Units",
                    0
                )
            )

            .replace(",", "")
            .strip()

            or 0
        )

        solar_generation = int(

            str(
                data.get(
                    "Solar Generation",
                    0
                )
            )

            .replace(",", "")
            .strip()

            or 0
        )

        export_units = int(

            str(
                data.get(
                    "Export Units",
                    0
                )
            )

            .replace(",", "")
            .strip()

            or 0
        )

        # ---------------------------------
        # TOTAL CONSUMPTION
        # ---------------------------------

        total_consumption = (
            import_units
            + solar_generation
        )

        # ---------------------------------
        # SELF CONSUMPTION
        # ---------------------------------

        self_consumption = (
            solar_generation
            - export_units
        )

        # ---------------------------------
        # SOLAR OFFSET
        # ---------------------------------

        solar_offset = (
            self_consumption
            + export_units
        )

        result["Import Units"] = (
            import_units
        )

        result["Solar Generation"] = (
            solar_generation
        )

        result["Export Units"] = (
            export_units
        )

        result["Self Consumption"] = (
            self_consumption
        )

        result["Without Solar Units"] = (
            total_consumption
        )

        result["Solar Offset Units"] = (
            solar_offset
        )

    except Exception as e:

        result["Error"] = str(e)

    return result
