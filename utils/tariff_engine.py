def calculate_bill_estimation(
    with_solar_bill,
    without_solar_units,
    solar_generation
):

    result = {}

    try:

        with_solar_bill = float(
            str(with_solar_bill)
            .replace(",", "")
        )

        without_solar_units = float(
            without_solar_units
        )

        energy_rate = 8.95
        wheeling_rate = 0.81
        fac_rate = 0.50
        duty_percent = 0.09

        demand_charges = 202150

        # ---------------------------------
        # CALCULATIONS
        # ---------------------------------

        energy_charges = (
            without_solar_units
            * energy_rate
        )

        wheeling_charges = (
            without_solar_units
            * wheeling_rate
        )

        fac_charges = (
            without_solar_units
            * fac_rate
        )

        electricity_duty = (
            energy_charges
            * duty_percent
        )

        grid_support_charges = 0

        total_without_solar = (

            demand_charges
            + energy_charges
            + wheeling_charges
            + fac_charges
            + electricity_duty

        )

        estimated_savings = (
            total_without_solar
            - with_solar_bill
        )

        # ---------------------------------
        # RESULTS
        # ---------------------------------

        result["Demand Charges"] = round(
            demand_charges,
            2
        )

        result["Energy Charges"] = round(
            energy_charges,
            2
        )

        result["Wheeling Charges"] = round(
            wheeling_charges,
            2
        )

        result["FAC Charges"] = round(
            fac_charges,
            2
        )

        result["Electricity Duty"] = round(
            electricity_duty,
            2
        )

        result["Grid Support Charges"] = round(
            grid_support_charges,
            2
        )

        result["Without Solar Bill"] = round(
            total_without_solar,
            2
        )

        result["Estimated Savings"] = round(
            estimated_savings,
            2
        )

    except Exception as e:

        result["Error"] = str(e)

    return result
