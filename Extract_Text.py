import io
from urllib.request import Request, urlopen
from PyPDF2 import PdfReader
from pdfminer.pdfparser import PDFParser


#Opens a PDF given a URL
def url_to_pdf(url):
    url_file = urlopen(Request(url)).read() #uses urlopen() on a request object and then reads it
    file = io.BytesIO(url_file) #stores the read file as bytes in a Python object
    pdf_file = PdfReader(file) #reads the file using a PDF reader and stores it as such

    return pdf_file

#takes in file path from computer and converts it into usable pdf python object
def file_to_pdf(filename):
    file = open(filename, 'rb')
    pdf_file = PdfReader(file)

    return pdf_file

#retrieves the page count of the pdf
def pageCount(pdf_file):
    page_count = len(pdf_file.pages)

    return page_count

#extracts the text from the pdf as a string
def extract_text(pdf_file):
    text = ''

    page_count = pageCount(pdf_file) #get page count
    for i in range(page_count): #for each page in the pdf, extract the text and add it to the string
        page = pdf_file.pages[i]
        text += page.extract_text()

    return page_count, text


def pdf_main(pdf_file):
    if pdf_file[0:4] == 'http': #checks if pdf input is a filename or a URL and calls functions accordingly
        file = url_to_pdf(pdf_file)
    else:
        file = file_to_pdf(pdf_file)
    text = extract_text(file)
    #print(text)

    return text

pdf_main('https://s29.q4cdn.com/816090369/files/doc_downloads/test.pdf')
