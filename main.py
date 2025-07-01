#!/usr/bin/env python3

from typing import Generator

'''
# Purpose
Parses and filters registered businesses in Sweden.

# Example
Finds all software development businesses in the city Östersund that were registered in 2025.

# Usage
Download the most recent data from https://vardefulla-datamangder.bolagsverket.se/scb/scb_bulkfil.zip
'''

def parse_file(filepath: str) -> Generator[dict, None, None]:
    with open(filepath, "r", encoding="cp1252", errors="replace") as f:
        header = next(f).rstrip("\n").split("\t")
        columns = len(header)

        for i, line in enumerate(f, 1):
            values = line.rstrip("\n").split("\t")
            values += [""] * (columns - len(values))
            yield dict(zip(header, values))

if __name__ == "__main__":
    for business in parse_file("scb_bulkfil_JE_20250630T064723_28.txt"):
        # Only those registered in 2025
        if business.get("RegDatKtid", "").startswith("2025"):
            # Only those based in Östersund
            if business.get("PostOrt", "") == "ÖSTERSUND":
                # Only those focused on Software development
                if any(business.get(code, "").startswith("62") for code in ["Ng1", "Ng2", "Ng3", "Ng4", "Ng5"]):
                    # Create a new business dict with specified keys. Omit keys with empty values.
                    simplified_business = {k: business[k] for k in ["PeOrgNr", "PostOrt", "RegDatKtid", "Namn", "Foretagsnamn"] if business.get(k)}

                    print(simplified_business)
