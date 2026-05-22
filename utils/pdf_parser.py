import pdfplumber
import re


def extract_amount(pattern, text):

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:

        try:

            return float(

                match.group(1)
                .replace(",", "")
                .strip()

            )

        except:

            return 0

    return 0


def extract_bill_data(pdf_file):

    full_text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                full_text += text + "\n"

    data = {}

    # -----------------------------------
    # BASIC DETAILS
    # -----------------------------------

    data["Demand Charges"] = extract_amount(
        r"Demand Charges.*?([\d,]+\.\d+)",
        full_text
    )

    data["Wheeling Charges"] = extract_amount(
        r"Wheeling Charge.*?([\d,]+\.\d+)",
        full_text
    )

    data["Energy Charges"] = extract_amount(
        r"Energy Charges.*?([\d,]+\.\d+)",
        full_text
    )

    data["TOD Charges"] = extract_amount(
        r"TOD Tariff EC.*?([\d,]+\.\d+)",
        full_text
    )

    data["FAC Charges"] = extract_amount(
        r"FAC.*?([\d,]+\.\d+)",
        full_text
    )

    data["Electricity Duty"] = extract_amount(
        r"Electricity Duty.*?([\d,]+\.\d+)",
        full_text
    )

    data["Tax on Sale"] = extract_amount(
        r"Tax on Sale.*?([\d,]+\.\d+)",
        full_text
    )

    data["Grid Support Charge"] = extract_amount(
        r"Grid Support Charge.*?([\d,]+\.\d+)",
        full_text
    )

    data["Debit Bill Adjustment"] = extract_amount(
        r"Debit Bill Adjustment.*?([\d,]+\.\d+)",
        full_text
    )

    data["Current Bill"] = extract_amount(
        r"TOTAL CURRENT BILL AS PER TARIFF\s+([\d,]+\.\d+)",
        full_text
    )

    # -----------------------------------
    # SOLAR DETAILS
    # -----------------------------------

    solar_match = re.search(
        r"(\d+)\s+Units.*?Solar",
        full_text,
        re.IGNORECASE
    )

    if solar_match:

        data["Solar Generation"] = int(
            solar_match.group(1)
        )

    else:

        data["Solar Generation"] = 0

    return data
