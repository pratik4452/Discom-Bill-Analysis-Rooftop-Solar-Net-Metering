import pdfplumber
import re


def extract_bill_data(pdf_file):

    extracted_data = {
        "Consumer Name": None,
        "Bill Amount": None,
        "Import Units": None,
        "Export Units": None,
        "Net Units": None,
    }

    full_text = ""

    # Read PDF
    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:
            text = page.extract_text()

            if text:
                full_text += text + "\n"

    # ----------------------------
    # CONSUMER NAME
    # ----------------------------

    name_match = re.search(
        r"Consumer Name[:\s]+([A-Za-z\s]+)",
        full_text
    )

    if name_match:
        extracted_data["Consumer Name"] = name_match.group(1)

    # ----------------------------
    # BILL AMOUNT
    # ----------------------------

    amount_match = re.search(
        r"Current Bill Amount[:\s₹]+([\d,\.]+)",
        full_text
    )

    if amount_match:
        extracted_data["Bill Amount"] = amount_match.group(1)

    # ----------------------------
    # IMPORT UNITS
    # ----------------------------

    import_match = re.search(
        r"Import Units[:\s]+(\d+)",
        full_text
    )

    if import_match:
        extracted_data["Import Units"] = import_match.group(1)

    # ----------------------------
    # EXPORT UNITS
    # ----------------------------

    export_match = re.search(
        r"Export Units[:\s]+(\d+)",
        full_text
    )

    if export_match:
        extracted_data["Export Units"] = export_match.group(1)

    # ----------------------------
    # NET UNITS
    # ----------------------------

    net_match = re.search(
        r"Net Units[:\s]+(\d+)",
        full_text
    )

    if net_match:
        extracted_data["Net Units"] = net_match.group(1)

    return extracted_data
