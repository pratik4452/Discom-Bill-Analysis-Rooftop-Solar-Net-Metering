def calculate_before_after_solar(data):

    result = {}

    try:

        # -----------------------------------
        # INPUTS
        # -----------------------------------

        import_units = float(
            data.get(
                "Import Units",
                0
            )
        )

        export_units = float(
            data.get(
                "Export Units",
                0
            )
        )

        solar_generation = float(
            data.get(
                "Solar Generation",
                0
            )
        )

        # -----------------------------------
        # BEFORE SOLAR UNITS
        # -----------------------------------

        before_solar_units = (

            import_units
            + solar_generation
            - export_units

        )

        # -----------------------------------
        # UNIT FACTOR
        # -----------------------------------

        if import_units > 0:

            unit_factor = (
                before_solar_units
                / import_units
            )

        else:

            unit_factor = 1

        # -----------------------------------
        # AFTER SOLAR VALUES
        # -----------------------------------

        demand_after = data.get(
            "Demand Charges",
            0
        )

        wheeling_after = data.get(
            "Wheeling Charges",
            0
        )

        energy_after = data.get(
            "Energy Charges",
            0
        )

        tod_after = data.get(
            "TOD Charges",
            0
        )

        fac_after = data.get(
            "FAC Charges",
            0
        )

        duty_after = data.get(
            "Electricity Duty",
            0
        )

        tax_after = data.get(
            "Tax on Sale",
            0
        )

        grid_after = data.get(
            "Grid Support Charge",
            0
        )

        # -----------------------------------
        # BEFORE SOLAR CALCULATIONS
        # -----------------------------------

        # DEMAND CHARGE
        # Usually same

        demand_before = demand_after

        # WHEELING
        # Based on units

        wheeling_before = (
            wheeling_after
            * unit_factor
        )

        # ENERGY CHARGE
        # Based on total units

        energy_before = (
            energy_after
            * unit_factor
        )

        # TOD
        tod_before = (
            tod_after
            * unit_factor
        )

        # FAC
        fac_before = (
            fac_after
            * unit_factor
        )

        # DUTY
        duty_before = (
            duty_after
            * unit_factor
        )

        # TAX
        tax_before = (
            tax_after
            * unit_factor
        )

        # GRID SUPPORT
        # Remove because no solar

        grid_before = 0

        # -----------------------------------
        # TOTALS
        # -----------------------------------

        after_total = (

            demand_after
            + wheeling_after
            + energy_after
            + tod_after
            + fac_after
            + duty_after
            + tax_after
            + grid_after

        )

        before_total = (

            demand_before
            + wheeling_before
            + energy_before
            + tod_before
            + fac_before
            + duty_before
            + tax_before
            + grid_before

        )

        savings = (
            before_total
            - after_total
        )

        # -----------------------------------
        # STORE RESULTS
        # -----------------------------------

        result["Before Solar Units"] = round(
            before_solar_units,
            2
        )

        result["Demand Charges"] = {

            "After Solar": round(
                demand_after,
                2
            ),

            "Before Solar": round(
                demand_before,
                2
            )

        }

        result["Wheeling Charges"] = {

            "After Solar": round(
                wheeling_after,
                2
            ),

            "Before Solar": round(
                wheeling_before,
                2
            )

        }

        result["Energy Charges"] = {

            "After Solar": round(
                energy_after,
                2
            ),

            "Before Solar": round(
                energy_before,
                2
            )

        }

        result["TOD Charges"] = {

            "After Solar": round(
                tod_after,
                2
            ),

            "Before Solar": round(
                tod_before,
                2
            )

        }

        result["FAC Charges"] = {

            "After Solar": round(
                fac_after,
                2
            ),

            "Before Solar": round(
                fac_before,
                2
            )

        }

        result["Electricity Duty"] = {

            "After Solar": round(
                duty_after,
                2
            ),

            "Before Solar": round(
                duty_before,
                2
            )

        }

        result["Tax on Sale"] = {

            "After Solar": round(
                tax_after,
                2
            ),

            "Before Solar": round(
                tax_before,
                2
            )

        }

        result["Grid Support Charge"] = {

            "After Solar": round(
                grid_after,
                2
            ),

            "Before Solar": round(
                grid_before,
                2
            )

        }

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
            savings,
            2
        )

    except Exception as e:

        result["Error"] = str(e)

    return result
