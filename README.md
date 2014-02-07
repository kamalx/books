books
=====

List all ebooks in current directory and subdirectories in an 
```index.html``` file that has links to download the files,
and lists meta-data from the files whenever it's available.

Currently, only PDF, EPUB and MOBI files are listed.
Meta data is parsed for only PDF and EPUB files.

Instructions
------------
To build, do:
```make html```
in the current directory to index everything below the current dir tree.

Generated html will be saved as ```index.html```


Note:
-----
This is something I made to learn a little bit of Python & using Jinja2 
templating engine to generate a static file listing all my ebooks. It is by 
no means a production-ready software and you use it at your own risk.

Tempted to send a PR or fork it? You be most welcome! ;)

