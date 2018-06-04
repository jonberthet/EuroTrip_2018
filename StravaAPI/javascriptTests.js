


	var StravaApiV3 = require('strava_api_v3');
	var defaultClient = StravaApiV3.ApiClient.instance;
var strava_oauth = defaultClient.authentications['strava_oauth'];
strava_oauth.accessToken = "1ee7f7dede077324f35a07eb5beb4261b2586bf7"

var api = new StravaApiV3.AthletesApi()

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getLoggedInAthlete(callback);


