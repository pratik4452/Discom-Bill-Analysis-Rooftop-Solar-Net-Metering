def calculate_bill_estimation(units):

    result = {}

    try:

        # ---------------------------------
        # SAFE VALUE CONVERSION
        # ---------------------------------

        if units is None:
            units = 0

        units = (
            str(units)
            .replace(",", "")
            .strip()
        )

        if units == "":
            units = 0

        units = float(units)

        # ---------------------------------
        # ENERGY CHARGES
        # ---------------------------------

        energy_rate = 8.50

        energy_charges = (
            units * energy_rate
        )

        # ---------------------------------
        # FAC CHARGES
        # ---------------------------------

        fac_rate = 1.00

        fac_charges = (
            units * fac_rate
        )

        # ---------------------------------
        # WHEELING CHARGES
        # ---------------------------------

        wheeling_rate = 0.75

        wheeling_charges = (
            units * wheeling_rate
        )

        # ---------------------------------
        # ELECTRICITY DUTY
        # ---------------------------------

        duty_rate = 0.075

        electricity_duty = (
            energy_charges * duty_rate
        )

        # ---------------------------------
        # FIXED CHARGES
        # ---------------------------------

        fixed_charges = 5000

        # ---------------------------------
        # TOTAL BILL
        # ---------------------------------

        total_bill = (

            energy_charges
            + fac_charges
            + wheeling_charges
            + electricity_duty
            + fixed_charges

        )

        # ---------------------------------
        # STORE RESULTS
        # ---------------------------------

        result["Units"] = round(
            units,
            2
        )

        result["Energy Charges"] = round(
            energy_charges,
            2
        )

        result["FAC Charges"] = round(
            fac_charges,
            2
        )

        result["Wheeling Charges"] = round(
            wheeling_charges,
            2
        )

        result["Electricity Duty"] = round(
            electricity_duty,
            2
        )

        result["Fixed Charges"] = round(
            fixed_charges,
            2
        )

        result["Estimated Bill"] = round(
            total_bill,
            2
        )

    except Exception as e:

        result["Error"] = str(e)

    return result
