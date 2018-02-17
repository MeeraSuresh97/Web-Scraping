# Web Scraping using Scrapy

Web scraping using Scrapy used to scrap web pages and extract data, and to find occurance of list of keywords.

  - Create html pages consist of list of keywords spreaded over randomly.
  - Scrap the html pages and extract the data
  - Find maximum and minimum occurance of keywords from the extracted data
  - Average keywords used and Find pages that has keywords count equivalent to average keywords

### Prerequisite

  - Python 3.6.4
  - Pip 9.0.1


### Installation

This project requires Faker and Scrapy tools.

Install the dependencies using the command,

```sh
$ pip install -r requirements.txt
```

### Execution

Execution commands for files listed below.

File : makeHtml.py
```sh
$ python makeHtml.py
```
File: scrapHtml.py

```sh
$ scrapy runspider scrapHtml.py
```

File: searchHtml.py

```sh
$ python searchHtml.py
```

