This is an api for fetching the statistics of a youtube video

Test:
  Download the package as zip, extract it to a folder and type the following commands:
  
    python test.py <url to youtube video>

API:
  class youtube_stats( <url of the youtube video> )
  functions:
    likes(): returns an integer, number of likes on the youtube video
    dislikes(): returns an integer, number of dislikes on the youtube video
