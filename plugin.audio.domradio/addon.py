#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path').decode('utf-8')
icons_path = os.path.join(addon_path,'resources')
xbmcplugin.setContent(handle=int(sys.argv[1]), content='songs')
				
def add_item(url,infolabels,img=''):
    listitem = xbmcgui.ListItem(infolabels['title'],iconImage=img,thumbnailImage=img)
    listitem.setInfo('audio',infolabels)
    listitem.setProperty('IsPlayable','true')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]),url,listitem)

add_item('https://dom.audiostream.io/domradio/1000/mp3/128/domradio-rp.mp3',{'title':'Domradio.de'},os.path.join(icons_path,'icon.png'))


xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True, updateListing=False, cacheToDisc=True)