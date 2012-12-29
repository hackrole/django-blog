#!/usr/bin/python2.7
#charset=utf-8

import urllib, urllib2
from xml.dom import minidom
import re

def open_sitemap(url="http://www.shell909090.com/blog/sitemap.xml"):
    sitemap = urllib.urlopen(url)
    return sitemap

def xml_handle(sitemap):
    sitemap = minidom.parse(sitemap)
    urlList = sitemap.getElementsByTagName('url')
    uList = []
    for url in urlList:
        loc = url.getElementsByTagName('loc')[0].childNodes[0]
        # print loc.toxml()
        if loc.nodeType == loc.TEXT_NODE:
            uList.append(loc.data)
        
    return uList

if __name__ == "__main__":
    print "=========================\n"
    sitemap = open_sitemap()
    uList = xml_handle(sitemap)
    # print uList
    for u in uList:
        print u
        
    

