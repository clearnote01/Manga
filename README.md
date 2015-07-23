Download mangas from sites like mangareader.net etc.

Cool program to download images from sites very easily, usually mangas
sites like mangareader have a specific url structure which this program
mimics to get 'pages' from the given url. 

First argument 'URL'

Second argument 'number of pages you want to download from that point'

For example running this script in terminal as:-

python manga.py http://mangareader/one-piece/400/2 10

This will download page 2 to 11 of 400th chapter of one-piece manga

Requirements:-
  python requests module
  python BeautifulSoup module

Sites currently supported:-
  mangareader.com
  OTHER may also WORK but not tested yet
