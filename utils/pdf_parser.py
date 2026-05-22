import pdfplumber
import re


def clean_amount(value):

    try:

        value = (
            str(value)
            .replace(",", "")
            .replace("Rs.", "")
            .strip()
        )

        return float(value)

    except:

        return 0


def extract_charge(pattern, text):

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:

        return clean_amount(
            match.group(1)
        )

    return 0


def extract_bill_data(pdf_file):

    full_text = ""

    # -----------------------------------
    # READ PDF
    # -----------------------------------

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                full_text += text + "\n"

    # -----------------------------------
    # DATA DICTIONARY
    # -----------------------------------

    data = {}

    # -----------------------------------
    # CONSUMER DETAILS
    # -----------------------------------

    consumer_match = re.search(

        r"Consumer Name\s*:\s*(.*)",

        full_text

    )

    if consumer_match:

        data["Consumer Name"] = (
            consumer_match.group(1)
            .strip()
        )

    # -----------------------------------
    # BILL AMOUNT
    # -----------------------------------

    bill_match = re.search(

        r"TOTAL CURRENT BILL AS PER TARIFF\s+([\d,]+\.\d+)",

        full_text

    )

    if bill_match:

        data["Bill Amount"] = (
            clean_amount(
                bill_match.group(1)
            )
        )

    # -----------------------------------
    # IMPORT / EXPORT
    # -----------------------------------

    import_export_match = re.search(

        r"TOTAL\s+(\d+)\s+(\d+)",

        full_text

    )

    if import_export_match:

        data["Import Units"] = (
            int(
                import_export_match.group(1)
            )
        )

        data["Export Units"] = (
            int(
                import_export_match.group(2)
            )
        )

    # -----------------------------------
    # SOLAR GENERATION
    # -----------------------------------

    solar_match = re.search(

        r"Solar Generation.*?(\d+)",

        full_text,
        re.IGNORECASE

    )

    if solar_match:

        data["Solar Generation"] = (
            int(
                solar_match.group(1)
            )
        )

    # -----------------------------------
    # DEBIT CHARGES
    # -----------------------------------

    data["Demand Charges"] = extract_charge(

        r"Demand Charges.*?([\d,]+\.\d+)",

        full_text

    )

    data["Wheeling Charges"] = extract_charge(

        r"Wheeling Charge.*?([\d,]+\.\d+)",

        full_text

    )

    data["Energy Charges"] = extract_charge(

        r"Energy Charges.*?([\d,]+\.\d+)",

        full_text

    )

    data["TOD Tariff EC"] = extract_charge(

        r"TOD Tariff EC.*?([\d,]+\.\d+)",

        full_text

    )

    data["FAC Charges"] = extract_charge(

        r"FAC.*?([\d,]+\.\d+)",

        full_text

    )

    data["Electricity Duty"] = extract_charge(

        r"Electricity Duty.*?([\d,]+\.\d+)",

        full_text

    )

    data["Tax on Sale"] = extract_charge(

        r"Tax on Sale.*?([\d,]+\.\d+)",

        full_text

    )

    data["Grid Support Charge"] = extract_charge(

        r"Grid Support Charge.*?([\d,]+\.\d+)",

        full_text

    )

    data["Debit Bill Adjustment"] = extract_charge(

        r"Debit Bill Adjustment.*?([\d,]+\.\d+)",

        full_text

    )

    # -----------------------------------
    # CREDIT CHARGES
    # -----------------------------------

    data["Prompt Payment Discount"] = extract_charge(

        r"Prompt Payment Discount.*?(-?[\d,]+\.\d+)",

        full_text

    )

    data["Load Factor Incentive"] = extract_charge(

        r"Load Factor Incentive.*?(-?[\d,]+\.\d+)",

        full_text

    )

    data["Incremental Rebate"] = extract_charge(

        r"Incremental Consum.*?(-?[\d,]+\.\d+)",

        full_text

    )

    data["Bulk Consumption Rebate"] = extract_charge(

        r"Bulk Consumption Rebate.*?(-?[\d,]+\.\d+)",

        full_text

    )

    return data
