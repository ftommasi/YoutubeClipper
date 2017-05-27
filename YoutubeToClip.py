#! /usr/bin/env python

from glob import glob
from pydub import AudioSegment
from pytube import YouTube
from pygame import mixer

import pygame
import os
import sys

MP4_DIR = "mp4/"
MP3_DIR = "mp3/"


def print_error():
  print "usage: YoutubeClipper [d (download) | p (play)] [url]"

#start_time and end_time are in milliseconds
class YoutubeToClip():
  def __init__(self):
    pass
  
  def clipmp3(self,target_mp3,start_time,end_time,output_filename,delete_source = False):
    song = AudioSegment.from_mp3(target_mp3)
    clipped = song[start_time : end_time]
    output_filename_with_extension = output_filename.split("_")[0] 
    #write clipped mp3
    clipped.export(open(MP3_DIR + output_filename_with_extension, "wb"), format="mp3")
  
    #delete original clip if specified
    if delete_source:
      os.remove(target_mp3)
  
    return output_filename_with_extension
  
  
  def convert_mp4_to_mp3(self,video_with_directory,delete_source = False):
    video = video_with_directory.split("/")[1]
    output_filename = MP3_DIR + video.split(".")[0] + ".mp3"
    AudioSegment.from_file(video_with_directory).export(output_filename, format="mp3")
    if delete_source:
      os.remove(video_with_directory)
    return output_filename
  
  
  def download_and_clip_video(self,url, clipped_output_name, clip_start_time, clip_end_time ,delete_mp4 = False, delete_full_mp3 = False):
    yt = YouTube(url)
    ytvid = yt.filter("mp4")[-1]
    target_video = MP4_DIR + clipped_output_name.split(".")[0] + "_temp.mp4" 
    ytvid.download(target_video)
    target_video_mp3 = self.convert_mp4_to_mp3(target_video,delete_mp4)
    final_clip = self.clipmp3(target_video_mp3, clip_start_time, clip_end_time, clipped_output_name,delete_full_mp3)
    return final_clip
  
  def main(self,args):
    if args[1].startswith("i"): #interactive mode
      command = raw_input("[YT2MP3]> ")
    elif args[1].startswith("d"):
      if len(args) <  6:
        print_error()
      else:
        print MP3_DIR + self.download_and_clip_video(args[2], args[3], int(args[4]), int(args[5]), True, True)
    elif args[1].startswith("p"):
      if len(args) <  6:
        print_error()
      else:
        clipped_mp3 = MP3_DIR + self.download_and_clip_video(args[2], args[3], int(args[4]), int(args[5]), True, True)
        print "download complete. playing track"
        mixer.init()
        soundbyte = mixer.Sound(clipped_mp3)
        channel = soundbyte.play()
        pygame.time.wait(2*(int(args[5]) - int(args[4])))
        print "done."
        os.remove(clipped_mp3)




    
if __name__ == "__main__":
  Y2C = YoutubeToClip()
  Y2C.main(sys.argv)
