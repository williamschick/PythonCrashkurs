import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=album&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))

o = response.json()
for r in o["results"]:
    print(r["collectionName"])