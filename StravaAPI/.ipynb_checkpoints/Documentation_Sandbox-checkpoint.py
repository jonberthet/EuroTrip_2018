# from __future__ import print_statement


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
startDateLocal = startDateLocal_example # String | ISO 8601 formatted date time.
elapsedTime = 56 # Integer | In seconds.
description = description_example # String | Description of the activity. (optional)
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