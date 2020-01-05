### Download mangas from sites (like mangareader.net etc):

Cool program to download images from sites very easily, usually mangas
sites like mangareader have a specific url structure which this program
mimics to get 'pages' from the given url. It stores the downloaded pages
in a directory with the same name as the manga.


### How to use?

**Usage**:
```
python manga.py <MANGA-NAME>
```

**Example**:

```
python manga.py one-piece
```

This will create a directory name 'one-piece' in the current directory
and start the download.
  

See all the options with : 

```
python manga.py --help
```

```
usage: manga.py [-h] [--ch CH] [--page PAGE] [--max-pages MAX_PAGES]
                [--resume RESUME] [--list]
                name

Cool manga downloader

positional arguments:
  name                  give the manga name, taken from manganet URL name for
                        the manga , eg: one-piece, naruto, shingeki-no-kyojin
                        browse http://mangareader.net/ to find the names

optional arguments:
  -h, --help            show this help message and exit
  --ch CH               give the chapter number (default: 1)
  --page PAGE           give the page number in that chapter for offset
                        (default: 1)
  --max-pages MAX_PAGES
                        give the pages count, (default: -1) disabled
  --resume RESUME       resume from last downloaded chapter and page (default:
                        True)
  --list                list some sample manga names
  ```

### What name to give for manga?

Give the manga name, from manganet [one-piece, shingeki-no-kyojin, boruto, naruto, etc]
Just go to https://www.mangareader.net, find your manga, in the URL whichever name is present, use that name here.

See a list of sample manga names
   
```
python manga.py --list list
```

### Requirements:

1) Python requests and bs4/lxml module (install using ```pip install lxml requests bs4```)
        

### Sites used internally:

- www.mangareader.net
