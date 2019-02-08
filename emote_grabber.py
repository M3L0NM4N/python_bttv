#modified code from u/rtainc on Reddit

import urllib, urllib.request
import os
import json

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')
print('Saving emotes to folder: ' + os.path.abspath('./emotes') + '...')
print('Grabbing emote list...')
file = open(sortedstreamers.txt, "r", encoding="utf8")
for streamer in file:
    emotes = json.load(urllib.request.urlopen("https://api.betterttv.net/2/channels/" + streamer))
for edict in emotes['emotes']:
    code = edict["url"]
    print('Downloading: ' + code + '...')
    urllib.request.urlretrieve('http:' + edict['regex'].replace('{image_id}', str(code['imageType'])),'./emotes/' + code + '.png')
print('Done! Kappa')