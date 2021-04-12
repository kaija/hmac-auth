import requests
from requests_hmac import HTTPSignatureAuth

username = 'test'
secret = 'pass'
url = 'https://example.com/'

res = requests.get(url, auth=HTTPSignatureAuth(key_id=username, key=secret))
print(res.text)
