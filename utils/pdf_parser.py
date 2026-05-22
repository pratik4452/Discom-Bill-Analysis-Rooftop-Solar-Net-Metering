import pdfplumber
import re


def extract_bill_data(pdf_file):

    data = {}

    full_text = ""

    # -------------------------------------
    # READ PDF
    # -------------------------------------

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    # -------------------------------------
    # DEBUG TEXT
    # -------------------------------------

    lines = full_text.split("\n")

    # -------------------------------------
    # CONSUMER NAME
    # -------------------------------------

    for line in lines:

        if "Consumer Name" in line:

            try:
                data["Consumer Name"] = (
                    line.split(":")[1]
                    .strip()
                )

            except:
                pass

    # -------------------------------------
    # CONSUMER NUMBER
    # -------------------------------------

    for line in lines:

        if "Consumer No." in line:

            match = re.search(
                r"(\d{10,})",
                line
            )

            if match:

                data["Consumer Number"] = (
                    match.group(1)
                )

    # -------------------------------------
    # BILL AMOUNT
    # -------------------------------------

    for line in lines:

        if (
            "TOTAL CURRENT BILL"
            in line.upper()
        ):

            amount_match = re.search(
                r"([\d,]+\.\d+)",
                line
            )

            if amount_match:

                data["Bill Amount"] = (
                    amount_match.group(1)
                )

    # -------------------------------------
    # IMPORT / EXPORT
    # -------------------------------------

    for line in lines:

        if "TOTAL" in line:

            numbers = re.findall(
                r"\d+",
                line
            )

            if len(numbers) >= 2:

                try:

                    data["Import Units"] = (
                        numbers[0]
                    )

                    data["Export Units"] = (
                        numbers[1]
                    )

                except:
                    pass

    # -------------------------------------
    # SOLAR GENERATION
    # -------------------------------------

    for line in lines:

        if (
            "SOLAR GENERATION"
            in line.upper()
        ):

            numbers = re.findall(
                r"\d+",
                line
            )

            if len(numbers) > 0:

                data[
                    "Solar Generation"
                ] = numbers[-1]

    # -------------------------------------
    # DEMAND CHARGES
    # -------------------------------------

    for line in lines:

        if "Demand Charges" in line:

            numbers = re.findall(
                r"[\d,]+\.\d+",
                line
            )

            if numbers:

                data[
                    "Demand Charges"
                ] = numbers[-1]

    # -------------------------------------
    # WHEELING CHARGES
    # -------------------------------------

    for line in lines:

        if "Wheeling Charge" in line:

            numbers = re.findall(
                r"[\d,]+\.\d+",
                line
            )

            if numbers:

                data[
                    "Wheeling Charges"
                ] = numbers[-1]

    # -------------------------------------
    # ENERGY CHARGES
    # -------------------------------------

    for line in lines:

        if "Energy Charges" in line:

            numbers = re.findall(
                r"[\d,]+\.\d+",
                line
            )

            if numbers:

                data[
                    "Energy Charges"
                ] = numbers[-1]

    # -------------------------------------
    # FAC CHARGES
    # -------------------------------------

    for line in lines:

        if "FAC" in line:

            numbers = re.findall(
                r"[\d,]+\.\d+",
                line
            )

            if numbers:

                data[
                    "FAC Charges"
                ] = numbers[-1]

    # -------------------------------------
    # ELECTRICITY DUTY
    # -------------------------------------

    for line in lines:

        if "Electricity Duty" in line:

            numbers = re.findall(
                r"[\d,]+\.\d+",
                line
            )

            if numbers:

                data[
                    "Electricity Duty"
                ] = numbers[-1]

    # -------------------------------------
    # GRID SUPPORT CHARGES
    # -------------------------------------

    for line in lines:

        if "Grid Support Charge" in line:

            numbers = re.findall(
                r"[\d,]+\.\d+",
                line
            )

            if numbers:

                data[
                    "Grid Support Charges"
                ] = numbers[-1]

    return data
