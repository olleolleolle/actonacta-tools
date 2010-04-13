#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup, HTMLParseError
from StringIO import StringIO as io
from wikitools import wiki
from wikitools import category

#page = urllib2.urlopen("http://www.europarl.europa.eu/sides/getDoc.do?pubRef=-//EP//TEXT+TA+P7-TA-2010-0058+0+DOC+XML+V0//EN&language=EN")
page = urllib2.urlopen("file:///Users/olle/Desktop/acta.html")
try:
    soup = BeautifulSoup(page)
except HTMLParseError, e:
    exit("Unable to fetch the thing.")
    
titleBoxes = soup.findAll('tr', attrs={'class':'doc_title'})
titleBlock = titleBoxes.pop() # The last box is the one we want
headline = titleBlock.find('td', attrs={"align":"left", "valign":"top"})
headLineText = headline.next.next.next.next
headlineText = headLineText.strip()

pageContents = u''
pageContents += unicode(headlineText) + u"\n"
for piece in soup.find('tr', attrs={'class':'contents'}).next:
    pageContents += unicode(piece).strip()

#print pageContents

# TODO: Login!
site = wiki.Wiki("http://euwiki.org/api.php")
cat = category.Category(site, "Foo") # Create object for "Category:Foo"
# iterate through all the pages in ns 0
for article in cat.getAllMembersGen(namespaces=[0]):
    article.edit(prependtext=pageContents) # edit each page

