from youtube_likes import youtube_stats
import sys

""" Script should contain exactly one argument """
if len(sys.argv) != 2:
    print "Usage:\n\tpython youtube-likes.py <url of video>"
    exit()

video_obj = youtube_stats(sys.argv[1])

print "Views: "+str(video_obj.views())
print "Likes: "+str(video_obj.likes())
print "DisLikes: "+str(video_obj.dislikes())

