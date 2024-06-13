from io import TextIOWrapper


_text: str | None = None

def load_file(file: TextIOWrapper):
  global _text
  _text = file.readline().strip()

def load_path(path):
  global _text

  try:
    file = open(path)
    _text = file.readline().strip()
  except:
    raise Exception("Failed to open lockfile")


def get_all_fields():
  global _text

  if(_text is None):
    raise Exception("No lockfile loaded")  

  return _text.split(":")

def get_proc_name():
  data = get_all_fields()
  return data[0]

def get_proc_id():
  data = get_all_fields()
  return int(data[1])

def get_port():
  data = get_all_fields()
  return int(data[2])

def get_password():
  data = get_all_fields()
  return data[3]

def get_protocl():
  data = get_all_fields()
  return data[4]

def get_url(path: str):
  return f"https://127.0.0.1:{get_port()}/{path}"

def get_auth():
  return ("riot", get_password())