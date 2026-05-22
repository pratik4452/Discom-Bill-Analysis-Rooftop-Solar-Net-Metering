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

    # ------------------------------------------------
    # CONSUMER NAME
    # ------------------------------------------------

    consumer_match = re.search(
        r"Consumer Name\s*:\s*(.*)",
        full_text
    )

    if consumer_match:

        data["Consumer Name"] = (
            consumer_match.group(1).strip()
        )

    # ------------------------------------------------
    # TOTAL BILL
    # ------------------------------------------------

    bill_match = re.search(
        r"TOTAL CURRENT BILL AS PER TARIFF\s+([\d,]+\.\d+)",
        full_text
    )

    if bill_match:

        data["Bill Amount"] = (
            bill_match.group(1)
        )

    # ------------------------------------------------
    # DEMAND CHARGES
    # ------------------------------------------------

    demand_match = re.search(
        r"Demand Charges.*?([\d,]+\.\d+)",
        full_text
    )

    if demand_match:

        data["Demand Charges"] = (
            demand_match.group(1)
        )

    # ------------------------------------------------
    # WHEELING CHARGES
    # ------------------------------------------------

    wheeling_match = re.search(
        r"Wheeling Charge.*?([\d,]+\.\d+)",
        full_text
    )

    if wheeling_match:

        data["Wheeling Charges"] = (
            wheeling_match.group(1)
        )

    # ------------------------------------------------
    # ENERGY CHARGES
    # ------------------------------------------------

    energy_match = re.search(
        r"Energy Charges\s+([\d,]+\.\d+)",
        full_text
    )

    if energy_match:

        data["Energy Charges"] = (
            energy_match.group(1)
        )

    # ------------------------------------------------
    # FAC CHARGES
    # ------------------------------------------------

    fac_match = re.search(
        r"FAC.*?([\d,]+\.\d+)",
        full_text
    )

    if fac_match:

        data["FAC Charges"] = (
            fac_match.group(1)
        )

    # ------------------------------------------------
    # ELECTRICITY DUTY
    # ------------------------------------------------

    duty_match = re.search(
        r"Electricity Duty\s+([\d,]+\.\d+)",
        full_text
    )

    if duty_match:

        data["Electricity Duty"] = (
            duty_match.group(1)
        )

    # ------------------------------------------------
    # GRID SUPPORT CHARGES
    # ------------------------------------------------

    grid_match = re.search(
        r"Grid Support Charge\s+([\d,]+\.\d+)",
        full_text
    )

    if grid_match:

        data["Grid Support Charges"] = (
            grid_match.group(1)
        )

    # ------------------------------------------------
    # IMPORT / EXPORT
    # ------------------------------------------------

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

    # ------------------------------------------------
    # SOLAR GENERATION
    # ------------------------------------------------

    solar_match = re.search(
        r"Solar Generation.*?(\d+)",
        full_text
    )

    if solar_match:

        data["Solar Generation"] = (
            solar_match.group(1)
        )

    return data
