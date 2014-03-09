import urllib2
import sys

class youtube_stats:
    
    def __init__(self,url_video):
        """ Fetch the youtube page in variable self.html """
        response = urllib2.urlopen(url_video)
        self.html = response.read()
    
    def likes(self):
        """ Find the class 'likes-count' in the self.html page  """
        index_likecnt = self.html.find("likes-count")

        """ Find the next occurance of '>' after the class """
        while self.html[index_likecnt]!='>':
	        index_likecnt+=1
	
        """ likes_str stores the number of likes as a string variable """
        likes_str = ""

        """ Find out likes """
        while True:
	        if self.html[index_likecnt]>='0' and self.html[index_likecnt]<='9':
		        likes_str+=(self.html[index_likecnt])
	        elif self.html[index_likecnt]=='<':
		        break
	        index_likecnt+=1
	
        """ likes_int stores the number of likes as integer """ 
        likes_int = int(likes_str)
        return likes_int
    
    def dislikes(self):
        """ Find the class 'dislikes-count' in the self.html page  """
        index_dislikecnt = self.html.find("dislikes-count")

        """ Find the next occurance of '>' after the class """
        while self.html[index_dislikecnt]!='>':
	        index_dislikecnt+=1

        """ Find the class 'dislikes-count' in the self.html page  """
        dislikes_str = ""


        """ Find out dislikes """
        while True:
	        if self.html[index_dislikecnt]>='0' and self.html[index_dislikecnt]<='9':
		        dislikes_str+=(self.html[index_dislikecnt])
	        elif self.html[index_dislikecnt]=='<':
		        break
	        index_dislikecnt+=1

        """ dislikes_int stores the number of likes as integer """
        dislikes_int = int(dislikes_str)
        return dislikes_int
