from bs4 import BeautifulSoup, NavigableString
from urllib2 import urlopen
#from textblob import TextBlob
#import plotly
#print plotly.__version__  # version >1.9.4 required
#from plotly.graph_objs import Scatter, Layout
from collections import Counter
import random

#Note: must be a public profile
print "Twitter username:" 
user = raw_input()
username=[]
temp=[]
temp2=[]
username.append(user)

endpoint = "https://twitter.com/%s"

f = urlopen(endpoint % user)
html =  f.read()
f.close()

soup =  BeautifulSoup(html, 'html.parser') 

tweets =  soup.find_all('strong', {'class': 'fullname js-action-profile-name show-popup-with-id'})

tweet_arr=[]
arr_len=[]
for i in range(0,len(tweets)):
	user = tweets[i].contents[0]

	action_tag = soup('span', {'class': 'username js-action-profile-name'})
	show_name = action_tag[i].contents[1].contents[0]

	twit_text = soup('p', {'class': 'js-tweet-text'})

	message = ""
	for nib in twit_text[i]:
		if isinstance(nib, NavigableString):
			message += nib
		else:
			message += nib.text

	print "tweet ",i+1,":\n"
	#print "twt id",len(tweets) #temp length checker
	print user, "@", show_name, message.encode("utf-8")	
#	testimonial = TextBlob(message)
#	x=testimonial.sentiment.polarity
#	x=x*100
#	temp.append(user)
#	print "Tweet polarity is:",x,"%"
#	if x < 0:
#		print"\nTweet is Negetive"
#	elif x > 0:
#		print"\nTweet is Positive"
#	else:
#		print"\nTweet is neutral"
#	print '\n'
#	tweet_arr.append(x)
#	arr_len.append(i)
	#if i == 20 :    #Remove both hashes ,
	#	break   #if code stops due to special chars
#temp2.append(collections.Counter(temp).most_common()[0])



#lst = Counter(temp).most_common()
#highest_count = max([i[1] for i in lst])
#values = [i[0] for i in lst if i[1] == highest_count]
#random.shuffle(values)
#print values[0]





