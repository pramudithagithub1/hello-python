import requests

url = "https://raw.githubusercontent.com/pramudithagithub1/hello-python/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print("File fetched successfully:\n")
    print(response.text)
else:
    print("Failed to fetch the file")
