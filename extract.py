import requests
from auth import APIAuthenticator


def fetch_ebay_listing(query) -> dict:
	headers = APIAuthenticator().get_ebay_requests_headers()
	params = {"q": query}
	response = requests.get(
		"https://api.ebay.com/buy/browse/v1/item_summary/search",
		headers=headers,
		params=params,
	)
	return response.json()
