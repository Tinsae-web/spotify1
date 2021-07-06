import requests
import spotipy
import json
CLIENT_ID = 'a5cbd7b7e02d417092d22de329849615'
CLIENT_SECRET = '58e8d91d7efa4c0fbe43aef36520ccf2'
AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
print(auth_response.status_code)
auth_response_data = auth_response.json()
auth_response_data
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'
track_id = '6CTWathupIiDs7U4InHnDA'
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers)
r = r.json()
r
<<<<<<< HEAD

print("Json file reading started")
with open("user.json", "r") as read_file:
  print("Let's parse this JSON file to python dic.")
  data = json.load(read_file)
  print("Decoded Json Data")
  for key, value in data.items():
    print(key, ":", value)
  print("Done with the json file")
print("JSON Values using Key")
print(data["name"])
print(data["member"])
print(data["playlist"])
print("Printing key and value")

  
     



=======
>>>>>>> 20ce50967ee80567c34cc5d5c8bb09f40637964f
