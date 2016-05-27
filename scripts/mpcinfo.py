#!/usr/bin/env python
import mpd

## Connect to mpd client ###
client = mpd.MPDClient()
client.connect("localhost", 6600)

## Get current song info ###
curSongInfo = client.currentsong()
print "Content-type: text/html\n\n"
print curSongInfo['file']
