# from __future__ import print_statement
# Client ID: 25004
# Client Secret: 0e545bda8ae5acb369c5f59fac04884765daaa38
# Access Token (public): 1ee7f7dede077324f35a07eb5beb4261b2586bf7
# code = f5ba261f10d2b9268599076202d556af78d23f7a
# User ID: 29939517

#API 3 legged flow
1. User logs in
2. User authorizes, gives consent, & redirected to app URL, which will have authorization code
3. Exchange code for access token by giving client_id and client_secret & authorization code.
4. Upon success, get access token

import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
name = name_example # String | The name of the activity.
type = type_example # String | Type of activity. For example - Run, Ride etc.
startDateLocal = startDateLocal_example # grep String | ISO 8601 formatted date time.
description = description_example # String | Description of the activity. (optional)
elapsedTime = 56 # Integer | In seconds.
distance = distance_example # String | In meters. (optional)
private = 56 # Integer | set to 1 to mark the resulting activity as private, ‘view_private’ permissions will be necessary to view the activity. If not specified, set according to the athlete’s privacy setting (recommended). (optional)
trainer = 56 # Integer | Set to 1 to mark as a trainer activity. (optional)
photoIds = photoIds_example # String | List of native photo ids to attach to the activity. (optional)
commute = 56 # Integer | Set to 1 to mark as commute. (optional)

try: 
    # Create an Activity
    api_response = api_instance.createActivity(name, type, startDateLocal, elapsedTime, description=description, distance=distance, private=private, trainer=trainer, photoIds=photoIds, commute=commute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->createActivity: %s\n" % e)


