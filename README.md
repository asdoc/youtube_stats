This is an API for getting the statistics of a youtube video

<b>Test:</b>
  Download the package as zip, extract it to a folder and type the following commands:
  
    python test.py <option> <arguments>
    
    options:
        stats <urls of youtube video>
        search <search query>

<b>API:</b><br>
  <b>class</b> youtube_stats( <url of the youtube video> )<br>
  <b>functions</b><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  title(): returns a string, title of the youtube video<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  views(): returns an integer, number of views on the youtube video<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  likes(): returns an integer, number of likes on the youtube video<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  dislikes(): returns an integer, number of dislikes on the youtube video<br>
  
  <b>class</b> youtube_search( <search query> )<br>
  <b>functions</b><br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  get_result(index): returns a string, result of the index'th url of the search query <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  print_all(): returns a list containing urls of all the search results<br>
