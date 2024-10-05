import requests

url = 'http://0.0.0.0:8000/api/toggle_fav_photo/'
cookies = {
    # 'csrftoken': 'm2rssPJoCwV61QplnlUwB3CNIYBIu7Ny',
    'sessionid': 'p0wstk9zrqfaws080e6unag50o644a11'
}
headers = {
    'X-CSRFToken': '5syZ4SYD59tAdNxkakIRG37wcmt7lu8WhkPhmxxRxvew4tMvnvsd7Wz9KaUFFrLk'
}
data = {
    'photo_id': '1'
}
response = requests.post(
    url,
    cookies=cookies,
    # headers=headers,
    data=data
)
print(response.status_code)
print(response.json())
