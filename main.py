import requests, json, os
from requests.auth import HTTPBasicAuth

clientID = os.environ['CLIENT_ID']
clientSecret = os.environ['CLIENT_SECRET']

url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(url, data=data, auth=auth)

#print(response.ok)
#print(response.json())
#print(response.status_code)

accessToken = response.json()["access_token"]
artist = input("Artist: ").lower()
artist = artist.replace(" ", "%20")

f = open("accessToken.txt","w")
f.write(accessToken)
f.close()

url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search = f"?q=artist%3A{artist}&type=track&limit=5"
fullURL = f"{url}{search}"

response = requests.get(fullURL, headers=headers)
data = response.json()
#print(data)

for track in data["tracks"]["items"]:
  print(track["name"])
  print(track["preview_url"])