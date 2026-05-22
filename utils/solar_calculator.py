def calculate_without_solar(data):

    result = {}

    multiplier = 1.60

    result["Demand Charges"] = (
        data.get("Demand Charges", 0)
        * multiplier
    )

    result["Wheeling Charges"] = (
        data.get("Wheeling Charges", 0)
        * multiplier
    )

    result["Energy Charges"] = (
        data.get("Energy Charges", 0)
        * multiplier
    )

    result["TOD Charges"] = (
        data.get("TOD Charges", 0)
        * multiplier
    )

    result["FAC Charges"] = (
        data.get("FAC Charges", 0)
        * multiplier
    )

    result["Electricity Duty"] = (
        data.get("Electricity Duty", 0)
        * multiplier
    )

    result["Tax on Sale"] = (
        data.get("Tax on Sale", 0)
        * multiplier
    )

    result["Grid Support Charge"] = (
        data.get("Grid Support Charge", 0)
        * multiplier
    )

    result["Debit Bill Adjustment"] = (
        data.get("Debit Bill Adjustment", 0)
    )

    total = (

        result["Demand Charges"]
        + result["Wheeling Charges"]
        + result["Energy Charges"]
        + result["TOD Charges"]
        + result["FAC Charges"]
        + result["Electricity Duty"]
        + result["Tax on Sale"]
        + result["Grid Support Charge"]
        + result["Debit Bill Adjustment"]

    )

    result["Without Solar Bill"] = total

    return result
