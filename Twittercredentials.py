import tweepy

consumer_key = "XhhfGX50cZ03gZVB2XdbCSrRw";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "4366LGocmEDQiWTlxvg8Eq2Pad6hEuz7WhH66VE0cEsq8z3Eem";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "757198652645314561-l9JZE6VdGvATVpV6kD2IOa9k8yaAQgn";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "1UZ7i4cHhTxfJcKpvdsWq4WZsZJX2GZyXjbIP8OolRPfA";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



