import json
import os
import re
import sys
from contextlib import suppress
import requests
from bs4 import BeautifulSoup
from names import FOUND_NAMES, FOUND_NAMES_DOC
from sys import exit
from pprint import pprint

MANGA_NET_URL = 'http://mangareader.net/'



def saveimg(url, name):
    req = requests.get(url)  # , stream=True)
    # print('hitting url: ' + url)
    with open(name, 'wb') as f:
        for chunk in req.iter_content(128):
            f.write(chunk)

# Creates a name based on manga name, ch and page


def makeName(manga, ch, page):
    if page == '':
        page = 1
    return '{}-{}-{}.jpg'.format(manga, ch, page)

# Give current status of download


def statusDownload(i, current_page_count, name):
    if current_page_count == 1:
        print('\nStarting download for: {}'.format(name))
        sys.stdout.write('['+' '*20+']\n[')
    frac = 20/current_page_count
    frac = int(round(frac))
    opline = '='*frac
    sys.stdout.write(opline)
    sys.stdout.flush()

# Main loop


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Cool manga downloader')

    parser.add_argument('name', help=f'give the manga name, taken from manganet URL name for the manga\
        , eg: one-piece, naruto, shingeki-no-kyojin\nbrowse {MANGA_NET_URL} to find the names')
    parser.add_argument('--ch', default=1, type=int, help='give the chapter number (default: %(default)s)')
    parser.add_argument('--page', default=1, type=int, help='give the page number in that chapter for offset (default: %(default)s)')
    parser.add_argument('--max-pages', default=-1, type=int,
                        help='give the pages count, (default: %(default)s) disabled')
    parser.add_argument('--resume', default=True, type=bool, help='resume from last downloaded chapter and page (default: %(default)s)')
    parser.add_argument('--list', action='store_true', help='list some sample manga names', default=False)
    args = parser.parse_args()

    if args.list:
        print(FOUND_NAMES_DOC)
        print('#'*20)
        print('\n')
        for index, name in enumerate(FOUND_NAMES):
            print(f'{index+1}: ', name, end='\n')
        print('\n')
        exit(0)

    name = args.name
    chapter = args.ch
    page = args.page
    max_pages = args.max_pages
    os.makedirs(name, exist_ok=True)
    os.chdir(name)
    if args.resume:
        with suppress(FileNotFoundError):
            with open('.current', 'r') as f:
                print('Resuming state for manga: ', name, '\n')
                state = json.load(f)
                page = state['page']
                chapter = state['chapter']
                max_pages = state['max_pages']
    while True:
        if page == 1:
            page_str = ''
        else:
            page_str = str(page)
        url = '{}{}/{}/{}'.format(MANGA_NET_URL, name, chapter, page_str)
        with open('.current', 'w') as f:
            json.dump({ 'chapter': chapter, 'page': page, 'max_pages': max_pages}, f)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")
        if soup.text == '':
            raise ValueError('Check the manga name again from manga net or else it\'s no use! noooooo...')
        if soup.text == '404 Not Found':
            chapter += 1  # next chapter
            page = 1  # first page of chapter
            max_pages = -1
        else:
            # if(max_pages == -1):
            #     # initialise number of pages if not given
            #     opt = soup.find_all("option")
            #     for x in range(0, len(opt)):
            #         if(opt[x].get("selected") == "selected"):
            #             pages = len(opt)-x
            #             break
            imgtags = soup.find_all("img")
            # Since my url has only one img tag, that's that
            imgsrc = imgtags[0].get("src")
            # requests object of the imgsrc url
            file_name = makeName(name, chapter, page)
            if not os.path.exists(file_name):
                saveimg(imgsrc, file_name)
            statusDownload(page, max_pages, file_name)
            print(f'Downloading ch: {chapter} with page: {page}', end='\r')
            page += 1
            if page == max_pages:
                sys.stdout.write(']\nDownload finished at:{}\n\n'.format(file_name))
                break


with suppress(KeyboardInterrupt):
    main()

print('Thank you for using manga downloader!')