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
     # Get the plugin url in plugin:// notation.
__url__ = sys.argv[0]
     # Get the plugin handle as an integer number.
__handle__ = int(sys.argv[1])

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
		



VIDEOS = {'Marvels.Jessica.Jones': [{'name': 'Marvels.Jessica.Jones.S01E04 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/517033c0?wersja=720p'},
                      {'name': 'Marvels.Jessica.Jones.S01E05 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/517965a4?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E06 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/517966be?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E07 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/521768bf?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E08 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/52177071?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E09 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/52177138?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E10 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/5217727d?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E11 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/52177313?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E12 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/521775b2?wersja=720p'},
					  {'name': 'Marvels.Jessica.Jones.S01E13 720p',
                       'thumb': 'http://i74.fastpic.ru/thumb/2015/1120/f5/4cd3058e5c48a20a9e753f86aea5eef5.jpeg',
                       'video': 'http://www.cda.pl/video/521776ad?wersja=720p'}				   					   
                      ],
			'Inne': [{'name': 'Jonah Hex (2010) / Lektor  720p',
                       'thumb': 'http://cdn1-www.superherohype.com/assets/uploads/2010/05/file_101220_1_jonahhexcharposter2.jpg',
                       'video': 'http://www.cda.pl/video/51704157?wersja=720p'}
					   ]}		  
					  
					  
					  
	
def addEpisode(category):
	#urlOrigin = url
	videos=VIDEOS[category]
	listing = []
	for video in videos:
		urlmovie = parserCDA(video['video'])
		#duration = ' ['+parserCDA_duration(video['video'])+']'
		list_item = xbmcgui.ListItem(label=video['name'], thumbnailImage=video['thumb'])
		list_item.setProperty('fanart_image', video['thumb'])
		list_item.setProperty('IsPlayable', 'true')
		#url = '{0}?action=play&video={1}'.format(__url__, urlmovie)
		url = urlmovie
		is_folder = False
		listing.append((url, list_item, is_folder))
		
	xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
	xbmcplugin.endOfDirectory(__handle__)
		#poster = "DefaultFolder.png" 
		#li = xbmcgui.ListItem(episodeTitle+" ["+duration+"]", iconImage=poster)
		#li.setArt({'thumb': 'DefaultVideo.png','poster': 'poster.jpg', 'fanart': 'fanart.jpg'})
		#xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
	return True
#wyszukanie po file:

#
def addCategories():
	categories = VIDEOS.keys()
	listing = []
	for category in categories:
		list_item = xbmcgui.ListItem(label=category, thumbnailImage=VIDEOS[category][0]['thumb'])
		list_item.setProperty('fanart_image', VIDEOS[category][0]['thumb'])
		url = '{0}?action=listing&category={1}'.format(__url__, category)
		is_folder = True
		listing.append((url, list_item, is_folder))
	xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
	xbmcplugin.endOfDirectory(__handle__)
	######
	#url=url = '{0}?action=listing&category={1}'.format(sys.argv[0], 'jessica')
	#li = xbmcgui.ListItem("Marvel Jessica Jones",iconImage="jjones.png")
	#li.setIconImage('icon.png')
	#li.setArt({'thumb': 'DefaultVideo.png','poster': 'poster.jpg', 'fanart': 'fanart.jpg'})
	#xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li,isFolder=True)
	#xbmcplugin.endOfDirectory(int(sys.argv[1]))
	return True
	
	

#print("!!! sys.argv[2]: " + sys.argv[2])
def play_video(path):
	#print("!!!!!!!!!!:"+path)
	#urlmovie = parserCDA(path)
	play_item = xbmcgui.ListItem(path=path)
	#play_item = xbmcgui.ListItem(path=path)
	xbmcplugin.setResolvedUrl(__handle__, True, listitem=play_item)

def router(paramstring):
	params = dict(parse_qsl(paramstring[1:]))
	#print(params)
	#print("router:"+params+":")
    # Check the parameters passed to the plugin
	if params:
		if params['action'] == 'listing':
			addEpisode(params['category'])
		#elif params['action']=='listing':
			
	else:
		#print("addFoldee")
		addCategories()
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



