Download mangas from sites like mangareader.net etc.

Cool program to download images from sites very easily, usually mangas
sites like mangareader have a specific url structure which this program
mimics to get 'pages' from the given url. It stores the downloaded pages
in a directory with the same name as the manga.


--> How to use?

First argument 'URL'
Second argument 'number of pages you want to download from that point'


Example:-
>   python manga.py http://mangareader.net/one-piece/400/2 10

This will create a directory name 'one-piece' in the current directory
and save the pages [2 to 11] of [400]th chapter of [one-piece] manga


Requirements:-
  1) python 2.6 or higher
     Install by :-
        >   sudo apt-get install python
  2) python requests module
        a) Using pip
        >   sudo apt-get install python-pip
        >   sudo pip install requests
  3) python BeautifulSoup module
	>   sudo pip install bs4

        

Sites currently supported:-
  www.mangareader.com
  OTHER sites may also WORK but not tested yet
