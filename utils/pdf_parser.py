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
        data["Consumer Name"] = (
            consumer_match.group(1).strip()
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
            bill_match.group(1)
        )

    # -----------------------------------
    # IMPORT EXPORT
    # -----------------------------------

    total_match = re.search(
        r"TOTAL\s+(\d+)\s+(\d+)",
        full_text
    )

    if total_match:

        data["Import Units"] = (
            total_match.group(1)
        )

        data["Export Units"] = (
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

        data["Solar Generation"] = (
            solar_match.group(1)
        )

    return data
