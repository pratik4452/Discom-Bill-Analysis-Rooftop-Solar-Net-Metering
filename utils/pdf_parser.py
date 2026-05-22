import pdfplumber
import re


def extract_bill_data(pdf_file):

    full_text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    data = {}

    # -----------------------------------
    # CONSUMER NAME
    # -----------------------------------

    consumer_match = re.search(
        r"Consumer Name\s*:\s*(.*)",
        full_text
    )

    if consumer_match:
        data["Consumer Name"] = consumer_match.group(1).strip()

    # -----------------------------------
    # CONSUMER NUMBER
    # -----------------------------------

    consumer_no_match = re.search(
        r"Consumer No\.\s*:\s*(\d+)",
        full_text
    )

    if consumer_no_match:
        data["Consumer Number"] = consumer_no_match.group(1)

    # -----------------------------------
    # BILL AMOUNT
    # -----------------------------------

    amount_match = re.search(
        r"Total Bill Amount.*?\s([\d,]+)",
        full_text
    )

    if amount_match:
        data["Bill Amount"] = amount_match.group(1)

    # -----------------------------------
    # IMPORT UNITS
    # -----------------------------------

    import_match = re.search(
        r"TOTAL\s+(\d+)\s+(\d+)",
        full_text
    )

    if import_match:
        data["Import Units"] = import_match.group(1)
        data["Export Units"] = import_match.group(2)

    # -----------------------------------
    # SOLAR GENERATION
    # -----------------------------------

    solar_match = re.search(
        r"Total Solar Generation Units\s*:\s*(\d+)",
        full_text
    )

    if solar_match:
        data["Solar Generation"] = solar_match.group(1)

    # -----------------------------------
    # ADJUSTED UNITS
    # -----------------------------------

    adjusted_match = re.search(
        r"Adjusted:\s*(\d+)",
        full_text
    )

    if adjusted_match:
        data["Adjusted Units"] = adjusted_match.group(1)

    # -----------------------------------
    # BANKED UNITS
    # -----------------------------------

    bank_match = re.search(
        r"Bank:\s*(\d+)",
        full_text
    )

    if bank_match:
        data["Banked Units"] = bank_match.group(1)

    return data
