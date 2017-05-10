# Personal Notes for Use

## Installing
```
conda create --name fitbit python=3.5
source activate fitbit
conda install python-dateutil
pip install requests-oauthlib
conda install cherrypy
```
*dateutil also installed six as co-dependency*

On dev site, changed redirect_uri to:
http://127.0.0.1:8080

To collect tokens:
```
./gather_keys_oauth2.py consumer_key consumer_secret
```

Also I've placed a file called vault.py in the tethig subdirectory (with an __init__.py) for my secrets. This file looks like this:
```
# password vault

consumer_key = 'string'
consumer_secret = 'string'
expires_at = 'string'
access_token = 'string'
expires_in = 'string'
refresh_token = 'string'
token_type = 'Bearer'
scope = ['activity', 'nutrition', 'location', 'weight', 'settings', 'heartrate', 'social', 'profile', 'sleep']
user_id = 'string'
```
*obviously what these strings are is secret!*
