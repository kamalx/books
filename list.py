#! /usr/bin/python

import os
from collections import OrderedDict
from pdf_info import get_pdf_info
from epub_info import get_epub_info

def list_all( types ):
    '''
    Lists all the directory names in the current directory tree
    syntax: list_all(['type1', 'type2', ...])
    returns dict with lists corresponding to each of the types
    '''
    
    the_list = OrderedDict.fromkeys( types )

    for t in types:
        x = []
        for root, dirs, files in os.walk('./'):
            for name in files:
                if( name.endswith( t ) ):
                    url = os.path.join( root, name )
                    print "[ %s ]: Attempting to collect metadata..." % (name)
                    ## XXX: Yet to figure out reading .mobi metadata...
                    ## XXX: PDF metadata is a mess. :/
                    if t == 'pdf':
                        try:
                        # Some nasty Unicode decode error occuring at this point.
                        # Not exactly sure, why
                            info = get_pdf_info(url)
                            # print info[0]
                        except:
                            print " Failed to get the meta info for this PDF file. :("
                    elif t == 'epub':
                        try:
                            info = get_epub_info(url)
                        except: 
                            print " Failed to get the meta info for this EPUB file. :("
                    else:
                        info = {'Name': name, 'meta': 'unkown'}
                    x.append( {'url':url, 'name':name, 'info':info} )
        the_list[t] = x

    title = "Books on my box"
    return { 'list': the_list, 'title': title }
