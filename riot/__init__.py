import os

from requests.sessions import Session

__all__ = [ "foo" ]

def get_session() -> Session:
  key = os.environ.get("RIOT_KEY")
  if(key is None):
    raise Exception("No api key found")

  s = Session()
  s.headers["X-Riot-Token"] = key

  return s