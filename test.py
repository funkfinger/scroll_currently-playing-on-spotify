import urllib2
response = urllib2.urlopen('https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=funkfinger&api_key=f326b6a97580914d09150ce361ba66ee&limit=1')
html = response.read()

import xml.etree.ElementTree as ET
tree = ET.fromstring(html)

artist = tree.find('artist')

artist = "unknown"
track = "unknown"

for elem in tree.iter():
    if elem.tag == 'artist':
        artist = elem.text
    if elem.tag == 'name':
        track = elem.text

print(artist + " - " + track)
