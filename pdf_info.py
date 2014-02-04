from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# flicked from 
# http://stackoverflow.com/questions/14209214/reading-the-pdf-properties-metadata-in-python

def get_pdf_info(fn):
    fp = open(fn, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    doc.initialize()
# returns a list with just one item which is a dictionary with several key:value pairs.
    return doc.info


