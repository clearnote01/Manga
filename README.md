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

name                  give the manga name, from manganet [one-piece, shingeki-no-kyojin, boruto, naruto, etc]
                    [just go to manga net, find your manga, in the URL whichever name is present, use that name here]

See a list of sample manga names
  
   
```
python manga.py --list list
```

### Requirements:

1) Python requests and bs4/lxml module (install using ```pip install lxml requests bs4```)
        

### Sites used internally:

- www.mangareader.net