#! /usr/bin/python
from list import list_all
from jinja2 import Environment, FileSystemLoader
from django.utils.encoding import smart_str

env = Environment(loader=FileSystemLoader('.'))
TEMPLATEFILE='index_t.html'
template = env.get_template( TEMPLATEFILE )
types = ['epub', 'mobi', 'pdf']
template_var = list_all( types )
OUTPUTFILENAME='index.html'

html=template.render( template_var )
print "Writing HTML to " + OUTPUTFILENAME + "..."
print "===================================================="
# print html

with open(OUTPUTFILENAME, "wb") as handle:
    ## Give the handle nice and clean string for stupid python 2.x to handle
    handle.write( smart_str( html ) )
print "Done."
print "===================================================="
