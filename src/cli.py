import argparse
import logging
from pathlib import Path

from .logic import pipeline

def main():
    
    parser = argparse.ArgumentParser(
        description="Converts regulatory report from CSV format to XML format, and enriches the report with further counter-party information."
    )

    parser.add_argument(
        "--input-file-path",
        dest="input_file_path",
        type=str,
        help="Relative path to the CSV file."
    )

    parser.add_argument(
        "--output-directory-path",
        dest="output_directory_path",
        type=str,
        help="Relative path to directory to output converted XML file."
    )

    args = parser.parse_args()

    # Call the core logic function to perform the conversion and enrichment
    pipeline(Path(args.input_file_path), Path(args.output_directory_path))

if __name__ == "__main__":
    main()
