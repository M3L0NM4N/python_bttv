import re

#using https://www.twitchmetrics.net/channels/viewership

#gets list of top 250 viewed streamers on Twitch
streamerslist = open("streamerslist.txt","r", encoding="utf8")
streamerslist = streamerslist.read()
streamerslist = re.findall("<h5 class=\"mr-2 mb-0\">(.*)</h5", streamerslist)

sortedstreamers = open("sortedstreamers.txt", "w", encoding="utf8")
for x in streamerslist:
    sortedstreamers.write(x + "\n")