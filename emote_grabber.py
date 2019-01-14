import urllib, urllib.request
import os
import json

if not os.path.exists('./emotes'):
    os.makedirs('./emotes')
print('Saving emotes to folder: ' + os.path.abspath('./emotes') + '...')
print('Grabbing emote list...')
emotes = json.load(urllib.request.urlopen('https://nightdev.com/betterttv/faces.php'))
for code, emote in emotes['emotes'].items():
    print('Downloading: ' + code + '...')
    urllib.urlretrieve('http:' + emotes['template']['large'].replace('{image_id}', str(emote['image_id'])),
                       './emotes/' + code + '.png')
print('Done! Kappa')




#u/rtainc
