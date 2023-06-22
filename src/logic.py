"""
Main logic to convert the transactions CSV to XML, and enrich each record with additional counterparty information.
"""

import os

import logging
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
    logger = logging.getLogger("xmliserlogger")
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info("Beginning process")
    
    logger.info("Loading transactions data from: '%s'", input_file_path)
    transactions_data_list = load_csv_to_dict(input_file_path)

    logger.info("Enriching data with additional counterparty information.")
    enriched_transactions_data_list = generate_enriched_transactions_data(transactions_data_list)
    
    output_file_path = os.path.join(output_directory_path, input_file_path.name.replace(".csv", ".xml"))
    logger.info("Attempting to write output XML to: %s", output_file_path)
    write_transactions_data_to_xml(enriched_transactions_data_list, output_file_path)
    logger.info("Success!")
