# Cool program to download images from sites very easily, usually mangas
# sites like mangareader have a specific url structure which this program
# mimics to get 'pages' from the given url.
# First argument 'URL'
# Second argument 'number of pages you want to download from that point'
# For example running this script in terminal as:-
# python manga.py http://mangareader/one-piece/400/2 10
# This will download page 2 to 11 of 400th chapter of one-piece manga
# Requirements:-
#   python requests module
#   python BeautifulSoup module
# Sites currently supported:-
#   mangareader.com
#   OTHER may also WORK but not tested yet

## Imports

import requests
from bs4 import BeautifulSoup
import re
import sys
import os

# Give url of image and image name
def saveimg(url, name):
    req = requests.get(url)#, stream=True)
    with open(name, 'wb') as f:
        for chunk in req.iter_content(128):
            f.write(chunk)

# Creates a name based on manga name, ch and page
def makeName(manga, ch, page):
    if page =='':
        page = 1
    return '{}-{}-{}'.format(manga, ch, page)

# Give current status of download
def statusDownload(i, pages, name):
    if i == 0:
        print '\nStarting download from: {}'.format(name)
        sys.stdout.write('['+' '*100+']\n[')
    frac = 100/pages
    frac = int(round(frac))
    opline  = '='*frac
    sys.stdout.write(opline)
    sys.stdout.flush()

# Main loop
def mainfunc():
    try:
        url = sys.argv[1]
    except:
        print 'ERROR: URL not given'
        raise EnvironmentError
    try:
        pages = int(sys.argv[2])
    except:
        pages = -1 #if number of pages is not given download all remaining pages instead of fixing it to 20
    pattern = re.compile(r'^(\w+://\w+.\w+.\w+/)(.*?)/(.*?)(/(.*?))?$')
    mo = pattern.search(url)
    try:
        webp = mo.group(1)
        manga = mo.group(2)
        chapter = int(mo.group(3))
        if mo.group(5) == None:
            page = ''
        else: page = int(mo.group(5))
    except:
        print 'ERROR: Regex of URL not matched'
        raise EnvironmentError

    i = 0
    try:
        if (os.path.exists(manga)):
            os.chdir(manga)
        else:
            os.makedirs(manga)
            os.chdir(manga)
    except:
        print("Seperate directory for the manga can't be created.\nDo you want to download in the current directory(y/n)")
        ans=raw_input()
        if (ans=='y'):
            pass
        else:
            sys.exit("Download cancelled")

    while True:
        url = '{}{}/{}/{}'.format(webp, manga, chapter, page)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        if soup.text == '404 Not Found':
            chapter += 1
            page = ''
        else:
            if(pages==-1):
                #initialise number of pages if not given
                opt=soup.find_all("option")
                for x in range(0,len(opt)):
                    if(opt[x].get("selected")=="selected"):
                        pages=len(opt)-x
                        break
            imgtags = soup.find_all("img")
            # Since my url has only one img tag, that's that
            imgsrc = imgtags[0].get("src")
            # requests object of the imgsrc url
            name = makeName(manga, chapter, page)
            saveimg(imgsrc, name)
            statusDownload(i, pages, name)
            if page == '':
                page = 2
            else: page += 1
            i += 1
            if i == pages:
                sys.stdout.write(']\nDownload finished at:{}\n\n'.format(name))
                break

mainfunc()
