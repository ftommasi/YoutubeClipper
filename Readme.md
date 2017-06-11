DEPENDENCY:
  pip install pydub pytube pygame
  sudo apt-get install ffmpeg

USAGE:
  #download or play part of a video (as mp3)
  python YoutubeClipper [d (download) | p (play)] [url] [outputfilename] [start_time] [end_time]
  
  #download full video as mp3
  python YoutubeClipper [p (full)] [url] [outputfilename] 
