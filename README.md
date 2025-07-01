# bolagsfilter

Finds specific businesses in Sweden

## Purpose
Parses and filters registered businesses in Sweden. I am using it to find startups in my area and field, which I can send a job application to.

## Example
Finds all software development businesses in the city Östersund that were registered in 2025.

Outputs:
```
{'PeOrgNr': '165595174011', 'PostOrt': 'ÖSTERSUND', 'RegDatKtid': '20250131', 'Namn': 'uxare.design HT AB'}
{'PeOrgNr': '165595177162', 'PostOrt': 'ÖSTERSUND', 'RegDatKtid': '20250131', 'Namn': 'Visionite Visby AB'}
{'PeOrgNr': '165595182956', 'PostOrt': 'ÖSTERSUND', 'RegDatKtid': '20250207', 'Namn': 'GeoIntellica AB'}
{'PeOrgNr': '200610186959', 'PostOrt': 'ÖSTERSUND', 'RegDatKtid': '20250613', 'Namn': 'Algarib, Ibrahim'}
```

## Usage
Download the most recent data from https://vardefulla-datamangder.bolagsverket.se/scb/scb_bulkfil.zip
