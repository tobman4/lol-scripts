from io import TextIOWrapper
from logging import getLogger

from urllib.parse import urljoin

from requests.sessions import Session

_logger = getLogger("lockfile")
_text: str | None = None
_session: Session | None = None

class ApiSession(Session):
    def __init__(self):
        super().__init__()

        self._is_ready = False
        self._base_url: str
        self._auth: str
        self.verify = False

    def load_lock(self, path: str):
        _logger.debug("Loading %s", path)

        with open(path, "r") as f:
            split = f.readline().strip().split(":")
            
            self._base_url = f"https://127.0.0.1:{split[2]}"
            self_auth = split[3]
        
        _logger.debug("URL: %s", self._base_url)
        self._is_ready = True

    def request(self, method, url, *args, **kwargs):
        if(not self._is_ready):
            raise Exception("No lockfile loaded")

        full_url = urljoin(self._base_url, url)
        return super().request(method, full_url, *args, **kwargs)
