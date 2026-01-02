import urllib.request
import json

def get_external_ip():
    with urllib.request.urlopen("https://api.ipify.org?format=json") as response:
        data = json.load(response)
    return data["ip"]