import requests

print(requests.__version__)

resp = requests.get("http://www.google.com")

print(resp.text)

