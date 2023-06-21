"""
Module for ingesting CSV data of transactions.
"""

import csv
from pathlib import Path
from typing import Dict, List

from dict2xml import dict2xml

def load_csv_to_dict(csv_path: Path) -> List[Dict]:
    """Load the csv file to a list of dictionaries."""
    with open(csv_path, mode="r", encoding="utf-8")as file:
        csv_dict = csv.DictReader(file)
        data = [dict(row) for row in csv_dict]
    return data

def write_transactions_data_to_xml(transactions_data: Dict, output_file_path: Path):
    """Write array of transactions data to XML file."""
    xml_strs = []
    for transaction in transactions_data:
        xml_str = dict2xml(transaction, wrap="transaction", indent="  ")
        xml_strs.append("  " + xml_str.replace("\n", "\n  "))

    xml_doc = "<transactions>\n" + "\n".join(xml_strs) + "\n</transactions>"

    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(xml_doc)
