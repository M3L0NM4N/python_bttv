import re

#using https://www.twitchmetrics.net/channels/viewership
streamers = re.findall("<h5 class=\"mr-2 mb-0\">(.*)</h5", open("streamerslist.txt"))
print(streamers)