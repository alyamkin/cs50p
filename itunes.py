import sys
import requests
import json

if len(sys.argv) != 2:
  sys.exit()

url = f"https://itunes.apple.com/search?entity=song&term={sys.argv[1]}"
response = requests.get(url)

album = response.json()

for track in album["results"]:
  print(track["trackName"])