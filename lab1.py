import requests
print("requests version:", requests.__version__)

# resp = requests.get("http://www.google.com")
# print(resp.text)

script = requests.get("https://raw.githubusercontent.com/garynks/cmput404-lab1/master/lab1.py")
print(script.text)