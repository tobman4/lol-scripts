import logging

from .lockfile import api_session

_logger = logging.getLogger("lol")

def get_friendlist():
  result = api_session.get("lol-chat/v1/friends")

  if(not result.ok):
    return []

  return result.json()
