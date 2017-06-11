import os
import glob
import subprocess

filename = "playlist"

playlistFile = open(filename,"r")

for line in playlistFile:
  line_split = line.split()
  song = line_split[0]
  name = line_split[1]


  print "starting download for", name, song
  song_process = subprocess.Popen(("./YoutubeToClip.py f " + song + " " + name + ".mp3").split())
  song_process.wait()
  print "download for", song, "complete"

