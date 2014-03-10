from youtube_likes import youtube_stats
from youtube_likes import youtube_search
import sys

""" Script should contain exactly two argument """
if len(sys.argv) != 3:
    print "Usage:\n\tpython test.py <option> <argument>"
    exit()

if sys.argv[1] == "stats":
    video_obj = youtube_stats(sys.argv[2])

    print "Title: "+video_obj.title()
    print "Views: "+str(video_obj.views())
    print "Likes: "+str(video_obj.likes())
    print "DisLikes: "+str(video_obj.dislikes())

elif sys.argv[1] == "search":
    search_obj = youtube_search(sys.argv[2])
    list_search = search_obj.get_all()
    for search_url in list_search:
        print search_url
    
else:
    print "Invalid option\nAvailable options:\n  stats <url of youtube video>\n  search <search query>"
