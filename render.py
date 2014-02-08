#! /usr/bin/python
from list import list_all
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
TEMPLATEFILE='index_t.html'
template = env.get_template( TEMPLATEFILE )
types = ['epub', 'pdf', 'mobi']
template_var = list_all( types )
OUTPUTFILENAME='index.html'

html=template.render( template_var )
print "Writing HTML to " + OUTPUTFILENAME + "..."
print "===================================================="
# print html

with open(OUTPUTFILENAME, "wb") as handle:
    ## All we needed was .encode('utf-8')
    ## <http://stackoverflow.com/a/18268929/699556>
    handle.write( html.encode('utf-8') )
print "Done."
print "===================================================="
