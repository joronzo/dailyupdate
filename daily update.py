import praw
import time
import pyowm
from yahoo_fin import stock_info as si

#Market stats using yahoo_fin module
def financials():
    silverprice = round(si.get_live_price("SI=F"),2)
    goldprice = round(si.get_live_price("GC=F"),2)
    sp500 = round(si.get_live_price("^GSPC"),2)
    vix = round(si.get_live_price("^VIX"),2)

    print("Gold price: \t$" + str(goldprice))
    time.sleep(.5)
    print("Silver price: \t$" + str(silverprice))
    time.sleep(.5)
    print("S&P 500: \t" + "{:,}".format(sp500))
    time.sleep(.5)
    print("VIX: \t\t" + str(vix) + "\n")

#News returns a composite of various subreddit headlines
def news():
    #reddit = praw.Reddit(client_id='my_client_id', client_secret='my_client_secret', user_agent='my_user_agent')

    hot_postsNEWS = reddit.subreddit('Worldnews').hot(limit=7)
    top_postsEcon = reddit.subreddit('Economy').top(limit=5)
    top_postsTR = reddit.subreddit('Truereddit').top(limit=3)
    
    for post in hot_postsNEWS:
        print('News: \t\t' + post.title)
        time.sleep(1.25)

    for post in top_postsTR:
        print('Truereddit: \t' + post.title)
        time.sleep(1.25)

    for post in top_postsEcon:
        print('Economy: \t' + post.title)
        time.sleep(1.25)

#using openweathermaps' API (you'll need an account to access via key)
#note weather is an object and temp is a dictionary value
def weather():
    #owm = pyowm.OWM('API Key here')

    obs = owm.weather_at_place('Boston, US')
    w = obs.get_weather()
    w2 = w.get_detailed_status()
    t = w.get_temperature('fahrenheit')
    print('\nThere are ' + str(w2) + ' in Boston and the temperature is ' + str(round(t['temp'])) + ' degrees')


financials()
news()
weather()





