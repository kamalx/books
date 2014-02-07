from pyPdf import PdfFileReader as pfr
from django.utils.encoding import smart_str, smart_unicode
# unicode error reference: 
#   http://www.saltycrane.com/blog/2008/11/python-unicodeencodeerror-ascii-codec-cant-encode-character/


# flicked from 
# http://stackoverflow.com/questions/14209214/reading-the-pdf-properties-metadata-in-python

def get_pdf_info(fn):
    fp = pfr(open(fn, 'rb'))
    file_info = fp.getDocumentInfo()

    clean_info = {}
    for di in file_info:
        try:
            clean_info[ smart_str( di[1:] ) ] = smart_unicode( file_info[di] )
            print "[Info for %s]" % (fn)
            print clean_info
        except strict:
            print "[Error] busted -> %s " % (fn)


# returns a dictionary with several key:value pairs.
    return clean_info
