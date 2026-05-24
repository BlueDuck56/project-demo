import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app_id = os.getenv("EBAY_APP_ID")
cert_id = os.getenv("EBAY_CERT_ID")

class APIAuthenticator:
    TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"
    SCOPE = "https://api.ebay.com/oauth/api_scope"
    MARKETPLACE_ID = "EBAY_US"

    def __init__(self, app_id=None, cert_id=None, session=None):
        self.app_id = app_id or os.getenv("EBAY_APP_ID")
        self.cert_id = cert_id or os.getenv("EBAY_CERT_ID")
        self.session = session or requests

    def _get_access_token(self):
        auth_str = f"{self.app_id}:{self.cert_id}"
        encoded_auth = base64.b64encode(auth_str.encode()).decode()

        auth_headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_auth}",
        }

        payload = {
            "grant_type": "client_credentials",
            "scope": self.SCOPE,
        }

        response = self.session.post(self.TOKEN_URL, headers=auth_headers, data=payload)
        return response.json().get("access_token")

    def get_ebay_requests_headers(self):
        token = self._get_access_token()

        return {
            "Authorization": f"Bearer {token}",
            "X-EBAY-C-MARKETPLACE-ID": self.MARKETPLACE_ID,
            "Accept": "application/json",
        }
