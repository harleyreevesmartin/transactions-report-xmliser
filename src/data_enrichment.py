import requests

from typing import Dict, List

def get_counterparties_info(leis: List[str]) -> Dict[str, Dict]:
    """
    Generate a dictionary of all counterparties information fetched from the GLEIF database.
    """
    counterparties_info = {}
    for lei in leis:
        if lei not in counterparties_info:
            counterparties_info[lei] = fetch_and_extract_counterparty_info(lei)

    return counterparties_info

def fetch_and_extract_counterparty_info(lei: str) -> Dict:
    """
    Fetch and extract relevant information of a counterparty from the GLEIF database.
    """
    base_url = "https://api.gleif.org/api/v1/lei-records"
    response = requests.get(f"{base_url}/{lei}", timeout=10)
    if response.status_code == 200:
        counterparty_info = response.json()
        extracted_data = {
            "LEI": lei,
            "LegalName": counterparty_info.get("data", {}).get("attributes", {}).get("entity", {}).get("legalName", {}).get("name"),
            "RegistrationDate": counterparty_info.get("data", {}).get("attributes", {}).get("registration", {}).get("initialRegistrationDate"),
            "LastUpdatedDate": counterparty_info.get("data", {}).get("attributes", {}).get("registration", {}).get("lastUpdateDate")
        }
        return extracted_data
    else:
        print(f"Could not retrieve info for LEI {lei}")

def generate_enriched_transactions_data(transactions_data: List[Dict]) -> List[Dict]:
    """Generate a list of enriched transactions data from a list of transactions data."""
    enriched_transactions_data = []

    leis = set()
    for transaction in transactions_data:
        leis.add(transaction["BuyerLEI"])
        leis.add(transaction["SellerLEI"])

    counterparties_info = get_counterparties_info(leis)

    for transaction in transactions_data:
        enriched_transaction_data = transaction.copy()

        enriched_transaction_data["Buyer"] = counterparties_info[transaction["BuyerLEI"]]
        enriched_transaction_data.pop("BuyerLEI")

        enriched_transaction_data["Seller"] = counterparties_info[transaction["SellerLEI"]]
        enriched_transaction_data.pop("SellerLEI")

        enriched_transactions_data.append(enriched_transaction_data)

    return enriched_transactions_data
