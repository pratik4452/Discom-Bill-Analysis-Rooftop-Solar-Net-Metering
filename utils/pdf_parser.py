import pdfplumber
import pandas as pd
import re


def clean_amount(value):

    try:

        value = str(value)

        value = value.replace(",", "")

        value = re.sub(r"[^\d\.-]", "", value)

        return float(value)

    except:

        return 0


def extract_bill_data(pdf_file):

    data = {}

    full_text = ""

    # -------------------------------------
    # READ PDF TEXT
    # -------------------------------------

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                full_text += text + "\n"

    # -------------------------------------
    # CONSUMER NAME
    # -------------------------------------

    consumer_match = re.search(

        r"Consumer Name\s*:\s*(.*)",

        full_text

    )

    if consumer_match:

        data["Consumer Name"] = (
            consumer_match.group(1).strip()
        )

    # -------------------------------------
    # CONSUMER NUMBER
    # -------------------------------------

    consumer_no_match = re.search(

        r"Consumer No\.\s*:\s*(\d+)",

        full_text

    )

    if consumer_no_match:

        data["Consumer Number"] = (
            consumer_no_match.group(1)
        )

    # -------------------------------------
    # BILL MONTH
    # -------------------------------------

    month_match = re.search(

        r"Bill Month\s*:\s*([A-Z\-0-9]+)",

        full_text

    )

    if month_match:

        data["Bill Month"] = (
            month_match.group(1)
        )

    # -------------------------------------
    # IMPORT / EXPORT
    # -------------------------------------

    total_match = re.search(

        r"TOTAL\s+(\d+)\s+(\d+)",

        full_text

    )

    if total_match:

        data["Import Units"] = (
            int(total_match.group(1))
        )

        data["Export Units"] = (
            int(total_match.group(2))
        )

    # -------------------------------------
    # SOLAR GENERATION
    # -------------------------------------

    solar_match = re.search(

        r"Solar Generation.*?(\d+)",

        full_text

    )

    if solar_match:

        data["Solar Generation"] = (
            int(solar_match.group(1))
        )

    # -------------------------------------
    # DEMAND CHARGES
    # -------------------------------------

    demand_match = re.search(

        r"Demand Charges.*?([\d,]+\.\d+)",

        full_text

    )

    if demand_match:

        data["Demand Charges"] = clean_amount(
            demand_match.group(1)
        )

    # -------------------------------------
    # WHEELING CHARGES
    # -------------------------------------

    wheeling_match = re.search(

        r"Wheeling Charge.*?([\d,]+\.\d+)",

        full_text

    )

    if wheeling_match:

        data["Wheeling Charges"] = clean_amount(
            wheeling_match.group(1)
        )

    # -------------------------------------
    # ENERGY CHARGES
    # -------------------------------------

    energy_match = re.search(

        r"Energy Charges.*?([\d,]+\.\d+)",

        full_text

    )

    if energy_match:

        data["Energy Charges"] = clean_amount(
            energy_match.group(1)
        )

    # -------------------------------------
    # TOD CHARGES
    # -------------------------------------

    tod_match = re.search(

        r"TOD Tariff EC.*?([\d,]+\.\d+)",

        full_text

    )

    if tod_match:

        data["TOD Charges"] = clean_amount(
            tod_match.group(1)
        )

    # -------------------------------------
    # FAC CHARGES
    # -------------------------------------

    fac_match = re.search(

        r"FAC.*?([\d,]+\.\d+)",

        full_text

    )

    if fac_match:

        data["FAC Charges"] = clean_amount(
            fac_match.group(1)
        )

    # -------------------------------------
    # ELECTRICITY DUTY
    # -------------------------------------

    duty_match = re.search(

        r"Electricity Duty.*?([\d,]+\.\d+)",

        full_text

    )

    if duty_match:

        data["Electricity Duty"] = clean_amount(
            duty_match.group(1)
        )

    # -------------------------------------
    # TAX ON SALE
    # -------------------------------------

    tax_match = re.search(

        r"Tax on Sale.*?([\d,]+\.\d+)",

        full_text

    )

    if tax_match:

        data["Tax on Sale"] = clean_amount(
            tax_match.group(1)
        )

    # -------------------------------------
    # GRID SUPPORT
    # -------------------------------------

    grid_match = re.search(

        r"Grid Support Charge.*?([\d,]+\.\d+)",

        full_text

    )

    if grid_match:

        data["Grid Support Charge"] = clean_amount(
            grid_match.group(1)
        )

    # -------------------------------------
    # TOTAL BILL
    # -------------------------------------

    total_bill_match = re.search(

        r"TOTAL CURRENT BILL AS PER TARIFF.*?([\d,]+\.\d+)",

        full_text

    )

    if total_bill_match:

        data["Current Bill"] = clean_amount(
            total_bill_match.group(1)
        )

    return data
