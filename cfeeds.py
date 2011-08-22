# script to parse Chris Coyiers favorite feeds
# makes an OPML file for importing into readers
#
# author: Hamish Macpherson
# url: http://hami.sh/
# created: 11-May-2011

import urllib2, re

OPML_TEMPLATE_TOP = """
<opml version="1.0">
    <head>
        <title>Chris Coyier's Favorite Blogs</title>
    </head>
    <body>
"""

OPML_TEMPLATE_ITEM = """<outline text="{feedtitle}" title="{feedtitle}" type="rss" xmlUrl="{feedurl}" htmlUrl="{siteurl}"/>\n"""

OPML_TEMPLATE_BOTTOM = """
    </body>
</opml>
"""

page = urllib2.urlopen("http://css-tricks.com/blogs-i-read/")
page = page.read()

# Format of each site/feed
# Will not match sites w/out a feed
rexp = re.compile("""<div
class="person"> (.*?) <a
href="(.*?)">Website</a> <a
href="(.*?)">Feed</a></div""")

feeds = re.findall(rexp, page)

opml = open("coyier-subscriptions.xml", "w")
opml.write(OPML_TEMPLATE_TOP)

try:   
   for f in feeds:
      info = {'feedtitle': f[0], 'siteurl': f[1], 'feedurl': f[2]}      
      xmldata = OPML_TEMPLATE_ITEM.format(**info)
      opml.write(xmldata)
   
except:
   print "Error in processing feeds."

opml.write(OPML_TEMPLATE_BOTTOM)
opml.close()

print "Succuessfully wrote OPML file: coyier-subscriptions.xml"
