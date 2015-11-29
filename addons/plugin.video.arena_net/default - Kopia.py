import xbmcaddon
import xbmcgui
import xbmcplugin
from urlparse import parse_qsl
#import cookielib, os, string, StringIO
#import os, time, base64, logging, calendar
import urllib, urllib2, re
#import xbmcaddon,  xbmcgui
import urlparse
#import httplib
import  libCommon

 
cm = libCommon.common()
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

def parserCDA(url):
    query_data = { 'url': url, 'use_host': False, 'use_cookie': False, 'use_post': False, 'return_data': True }
	
    link = cm.getURLRequestData(query_data)
    match = re.search("""file: ['"](.+?)['"],""",link)
    if match:   
		linkVideo = match.group(1) + '|Cookie="PHPSESSID=1&Referer=http://static.cda.pl/player5.9/player.swf'
		return linkVideo
    else: 
		return False
	
def parserCDA_duration(url):
    query_data = { 'url': url, 'use_host': False, 'use_cookie': False, 'use_post': False, 'return_data': True }
	
    link = cm.getURLRequestData(query_data)
    match = re.search("""duration: ['"](.+?)['"],""",link)
    if match:   
		linkVideo = match.group(1)# + '|Cookie="PHPSESSID=1&Referer=http://static.cda.pl/player5.9/player.swf'
		return linkVideo
    else: 
		return False	
def parserCDA_poster(url):
    query_data = { 'url': url, 'use_host': False, 'use_cookie': False, 'use_post': False, 'return_data': True }
	
    link = cm.getURLRequestData(query_data)
    match = re.search("""poster=['"](.+?)['"]""",link)
    if match:   
		linkVideo = match.group(1)# + '|Cookie="PHPSESSID=1&Referer=http://static.cda.pl/player5.9/player.swf'
		return linkVideo
    else: 
		return False
		
def parserCDA_title(url):
    query_data = { 'url': url, 'use_host': False, 'use_cookie': False, 'use_post': False, 'return_data': True }
	
    link = cm.getURLRequestData(query_data)
    match = re.search("""property="og:title" content=['"](.+?)['"]""",link)
    if match:   
		linkVideo = match.group(1)# + '|Cookie="PHPSESSID=1&Referer=http://static.cda.pl/player5.9/player.swf'
		return linkVideo
    else: 
		return False
		
def getSearchURL(self, key):
        url = 'http://www.cda.pl/video/show/' + urllib.quote_plus(key) +'/p1?s=best'
        #http://www.cda.pl/video/show/xxx/p2?s=best
	return url
	
def addEpisode(episodeUrl,episodeTitle):
	#urlOrigin = url
	url = parserCDA(episodeUrl)
	duration = parserCDA_duration(episodeUrl)
	#"DefaultFolder.png"
	#parserCDA_poster(urlOrigin)
	poster = "DefaultFolder.png" 
	#title = parserCDA_title(urlOrigin)
	li = xbmcgui.ListItem(episodeTitle+" ["+duration+"]", iconImage=poster)
	#li.setIconImage('icon.png')
	li.setArt({'thumb': 'DefaultVideo.png','poster': 'poster.jpg', 'fanart': 'fanart.jpg'})
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
	return True
#wyszukanie po file:

#
def addFolder():
	url=url = '{0}?action=listing&category={1}'.format(sys.argv[0], 'jessica')
	li = xbmcgui.ListItem("Marvel Jessica Jones",iconImage="jjones.png")
	li.setIconImage('icon.png')
	li.setArt({'thumb': 'DefaultVideo.png','poster': 'poster.jpg', 'fanart': 'fanart.jpg'})
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li,isFolder=True)
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
	return True
	
	

print("!!! sys.argv[2]: " + sys.argv[2])

def router(paramstring):
	params = dict(parse_qsl(paramstring[1:]))
	print(params)
	#print("router:"+params+":")
    # Check the parameters passed to the plugin
	if params:
		if params['category'] == 'jessica':
			addEpisode('http://www.cda.pl/video/517033c0?wersja=720p','Marvels.Jessica.Jones.S01E04 720p')
			xbmcplugin.endOfDirectory(int(sys.argv[1]))
	else:
		print("addFoldee")
		addFolder()
	return True

router(sys.argv[2])
#print("!!! sys.argv[2]: " + sys.argv[2])

#odcinek4
#addEpisode('http://www.cda.pl/video/517033c0?wersja=720p','Marvels.Jessica.Jones.S01E04 720p')
#odcinek5
#asd addEpisode('http://www.cda.pl/video/517965a4?wersja=720p','Marvels.Jessica.Jones.S01E05 720p')
#odcinek6
#asd addEpisode('http://www.cda.pl/video/517966be?wersja=720p','Marvels.Jessica.Jones.S01E06 720p')
#odcinek7
#asd addEpisode('http://www.cda.pl/video/521768bf?wersja=720p','Marvels.Jessica.Jones.S01E07 720p')
#odcinek8
#asd addEpisode('http://www.cda.pl/video/52177071?wersja=720p','Marvels.Jessica.Jones.S01E08 720p')
#odcinek9
#asd addEpisode('http://www.cda.pl/video/52177138?wersja=720p','Marvels.Jessica.Jones.S01E09 720p')
#odcinek10
#asd addEpisode('http://www.cda.pl/video/5217727d?wersja=720p','Marvels.Jessica.Jones.S01E10 720p')
#odcinek11
#asd addEpisode('http://www.cda.pl/video/52177313?wersja=720p','Marvels.Jessica.Jones.S01E11 720p')
#odcinek12
#asd addEpisode('http://www.cda.pl/video/521775b2?wersja=720p','Marvels.Jessica.Jones.S01E12 720p')
#odcinek13
#asd addEpisode('http://www.cda.pl/video/521776ad?wersja=720p','Marvels.Jessica.Jones.S01E13 720p')



