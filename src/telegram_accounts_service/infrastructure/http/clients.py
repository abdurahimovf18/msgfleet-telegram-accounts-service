from src.users_service.utils.http.http_client import HTTPClient
from src.users_service.config.settings import AUTH_SERVICE_URL


class AuthHTTPClient(HTTPClient):
    def __init__(self, **kw):
        self.kw = {}
        super().__init__(base_url=AUTH_SERVICE_URL, **(self.kw | kw))
