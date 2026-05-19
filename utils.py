import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_ebay_requests_headers():
    """
    Took me like, 3 days to figure out how to do this
    Their docs don't have no code snippet and shits all over the place, so I had to piece it together from like 5 different sources
    """
    app_id = os.getenv("EBAY_APP_ID")
    cert_id = os.getenv("EBAY_CERT_ID")

    auth_str = f"{app_id}:{cert_id}"
    encoded_auth = base64.b64encode(auth_str.encode()).decode()

    token_url = "https://api.ebay.com/identity/v1/oauth2/token"

    auth_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_auth}"
    }

    payload = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }

    response = requests.post(token_url, headers=auth_headers, data=payload)
    token = response.json().get('access_token')
    
    return {
        "Authorization": f"Bearer {token}",
        "X-EBAY-C-MARKETPLACE-ID": "EBAY_US",
        "Accept": "application/json"
    }
