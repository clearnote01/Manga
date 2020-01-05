### Download mangas from sites (like mangareader.net etc):

Cool program to download images from sites very easily, usually mangas
sites like mangareader have a specific url structure which this program
mimics to get 'pages' from the given url. It stores the downloaded pages
in a directory with the same name as the manga.


### How to use?

**Usage**:
```
python manga.py <URL> <No of Pages>
```

`<URL>` specifies the url of the page to download from

`<No of Pages>` specifies the number of pages to download

**Example**:

```
python manga.py http://mangareader.net/one-piece/400/2 10
```

This will create a directory name 'one-piece' in the current directory
and save the pages [2 to 11] of [400]th chapter of [one-piece] manga


### Requirements:

1) Python requests and bs4/lxml module (install using ```pip install lxml requests bs4```)
        

### Sites currently supported:

- www.mangareader.net