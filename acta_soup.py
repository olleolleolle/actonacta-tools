#!/usr/bin/env python
import urllib2
from BeautifulSoup import BeautifulSoup, HTMLParseError
import mwclient

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

print headlineText


contentBox = soup.findAll('tr', attrs={'class':'contents'})

for piece in contentBox:
#      #where, linebreak, what = incident.contents[:3]
#      # print where.strip()
#      # print what.strip()
      print unicode(piece.next).strip()
