import os
import glob
import subprocess

filename = "playlist"

playlistFile = open(filename,"r")

for line in playlistFile:
  line_split = line.split()
  song = line_split[0]
  link = line_split[1]


  print "starting download for", song
  song_process = subprocess.Popen("./Youtubeclipper f " + song + " " + name + ".mp3")
  song_process.wait()
  print "download for", song, "complete"

