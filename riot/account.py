from . import get_session

def get_by_name(name: str, tag: str):
  session = get_session()
  res = session.get(f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}")

  if(not res.ok):
    print(res)
    raise Exception()
  
  print(res.json())