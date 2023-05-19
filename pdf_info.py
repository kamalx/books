from pypdf import PdfFileReader as pfr

# flicked from
# http://stackoverflow.com/questions/14209214/reading-the-pdf-properties-metadata-in-python

def get_pdf_info(fn):
    fp = pfr(open(fn, 'rb'))
    file_info = fp.getDocumentInfo()

    clean_info = {}
    for di in file_info:
        try:
            clean_info[ di[1:] ] = file_info[di]
            print("[Info for %s]" % (fn))
            print(clean_info)
        except UnicodeEncodeError as e:
        ## http://docs.python.org/2/library/exceptions.html#exception-hierarchy
            print("[Error] busted -> %s \n %s" % (fn, e))
            raise


    # returns a dictionary with several key:value pairs.
    return clean_info
