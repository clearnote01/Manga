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

from sys import argv
import requests 
from bs4 import BeautifulSoup
import re


# Give url of image and image name
def saveimg(url, name):
    req = requests.get(url)#, stream=True)
    print 'Saving:{}', name
    with open(name, 'wb') as f:
        for chunk in req.iter_content(128):
            f.write(chunk)

# Creates a name based on manga name, ch and page
def makeName(manga, ch, page):
    if page =='':
        page = 1
    return '{}-{}-{}'.format(manga, ch, page)

# Main loop
def mainfunc():
    try:
        url = argv[1]
    except:
        print 'ERROR: URL not given'
        raise EnvironmentError
    try:
        pages = int(argv[2])
    except:
        pages = 20
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
    
    for i in range(pages): 
        url = '{}{}/{}/{}'.format(webp, manga, chapter, page) 
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        if soup.text == '404 Not Found':
            chapter += 1
            page = ''
        else:
            imgtags = soup.find_all("img")
            # Since my url has only one img tag, that's that
            imgsrc = imgtags[0].get("src")
            # requests object of the imgsrc url
            print 'NAME:'
            name = makeName(manga, chapter, page)
            print name
            saveimg(imgsrc, name)
            if page == '':
                page = 2
            else: page += 1
        print 'Current Status;{}/{}'.format(i+1, pages)
mainfunc()
