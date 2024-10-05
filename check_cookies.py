import requests

url = 'http://0.0.0.0/api/'

session = requests.Session()

response = session.get(url)

cookies = session.cookies

print("Cookies received:")
for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")
