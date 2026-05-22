import requests

from auth import APIAuthenticator


def get_browse_results(query):
	headers = APIAuthenticator().get_ebay_requests_headers()
	params = {"q": query}
	response = requests.get(
		"https://api.ebay.com/buy/browse/v1/item_summary/search",
		headers=headers,
		params=params,
	)
	return response.json()


query = "laptop"


results = get_browse_results(query)
print(results.prettify())