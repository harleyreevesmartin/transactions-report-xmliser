"""
Main logic to convert the transactions CSV to XML, and enrich each record with additional counterparty information.
"""

import os

from pathlib import Path

from .utils import load_csv_to_dict, write_transactions_data_to_xml
from .data_enrichment import generate_enriched_transactions_data

def pipeline(input_file_path: Path, output_directory_path: Path) -> None:
    """
    The entire pipeline:
        1. Firstly load the original transactions data.
        2. Enrich the transactions data using the LEI keys with relevant information.
        3. Write the newly enriched data to an XML file.
    """
    
    output_file_name = input_file_path.name.replace(".csv", ".xml")
    transactions_data_list = load_csv_to_dict(input_file_path)
    enriched_transactions_data_list = generate_enriched_transactions_data(transactions_data_list)
    write_transactions_data_to_xml(enriched_transactions_data_list, os.path.join(output_directory_path, output_file_name))
