import pdfplumber
import re


# -----------------------------------
# CLEAN AMOUNT
# -----------------------------------

def clean_amount(value):

    try:

        value = str(value)

        value = value.replace(",", "")

        value = re.sub(
            r"[^\d\.-]",
            "",
            value
        )

        return float(value)

    except:

        return 0


# -----------------------------------
# EXTRACT BILL DATA
# -----------------------------------

def extract_bill_data(pdf_file):

    data = {}

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
    # CONSUMER NAME
    # -----------------------------------

    consumer_match = re.search(

        r"Consumer Name\s*:\s*(.*)",

        full_text

    )

    if consumer_match:

        data["Consumer Name"] = (
            consumer_match.group(1).strip()
        )

    # -----------------------------------
    # CONSUMER NUMBER
    # -----------------------------------

    consumer_no_match = re.search(

        r"Consumer No\.\s*:\s*(\d+)",

        full_text

    )

    if consumer_no_match:

        data["Consumer Number"] = (
            consumer_no_match.group(1)
        )

    # -----------------------------------
    # BILL MONTH
    # -----------------------------------

    month_match = re.search(

        r"Bill Month\s*:\s*([A-Z0-9\-]+)",

        full_text

    )

    if month_match:

        data["Bill Month"] = (
            month_match.group(1)
        )

    # -----------------------------------
    # IMPORT / EXPORT UNITS
    # -----------------------------------

    total_match = re.search(

        r"TOTAL\s+(\d+)\s+(\d+)",

        full_text

    )

    if total_match:

        data["Import Units"] = int(
            total_match.group(1)
        )

        data["Export Units"] = int(
            total_match.group(2)
        )

    # -----------------------------------
    # SOLAR GENERATION
    # -----------------------------------

    solar_match = re.search(

        r"Solar Generation.*?(\d+)",

        full_text

    )

    if solar_match:

        data["Solar Generation"] = int(
            solar_match.group(1)
        )

    # -----------------------------------
    # CHARGE EXTRACTION FUNCTION
    # -----------------------------------

    def extract_charge(label):

        pattern = (
            rf"{label}.*?([\d,]+\.\d+)"
        )

        match = re.search(
            pattern,
            full_text
        )

        if match:

            return clean_amount(
                match.group(1)
            )

        return 0

    # -----------------------------------
    # CHARGES
    # -----------------------------------

    data["Demand Charges"] = extract_charge(
        "Demand Charges"
    )

    data["Wheeling Charges"] = extract_charge(
        "Wheeling Charge"
    )

    data["Energy Charges"] = extract_charge(
        "Energy Charges"
    )

    data["TOD Charges"] = extract_charge(
        "TOD Tariff EC"
    )

    data["FAC Charges"] = extract_charge(
        "FAC"
    )

    data["Electricity Duty"] = extract_charge(
        "Electricity Duty"
    )

    data["Tax on Sale"] = extract_charge(
        "Tax on Sale"
    )

    data["Grid Support Charge"] = extract_charge(
        "Grid Support Charge"
    )

    data["Current Bill"] = extract_charge(
        "TOTAL CURRENT BILL AS PER TARIFF"
    )

    return data
