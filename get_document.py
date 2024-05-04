import requests

url = 'http://188.34.149.219/apirest.php/Document/10/'
headers = {
    'Content-Type': 'application/json',
    'Session-Token': 'ds74kjg97bdu6uppus8f6huu67',
    'Accept': 'application/octet-stream'
}
output_file = '/home/airguy/PycharmProjects/sandbox1/file.txt'

response = requests.get(url, headers=headers)

print(response.content)

# if response.status_code == 200:
#     with open(output_file, 'wb') as f:
#         f.write(response.content)
#     print(f'File saved to {output_file}')
# else:
#     print(f'Failed to download file: {response.status_code}')
