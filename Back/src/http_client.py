from aiohttp import ClientSession
from Back.src.config import settings


class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={'X-CMC_PRO_API_KEY': settings.CMC_API_KEY})