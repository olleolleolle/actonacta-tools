#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup, HTMLParseError
import mwclient
from StringIO import StringIO as io

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

s = u''
s += unicode(headlineText) + u"\n"
for piece in soup.find('tr', attrs={'class':'contents'}).next:
    s += unicode(piece).strip()

print s

# TODO: Encode that string, to be able to save it here.
# fd = open("/Users/olle/opensource/python/actonacta-tools/acta-out.html", "rw")
# fd.write(u)
# fd.close()
