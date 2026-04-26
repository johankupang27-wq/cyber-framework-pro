import requests

def run():
    url = input("URL: ")
    try:
        r = requests.get(url, timeout=5)
        print("STATUS:", r.status_code)
    except:
        print("DOWN / ERROR")
