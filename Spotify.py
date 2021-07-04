import requests
import spotipy
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
