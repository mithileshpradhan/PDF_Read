pdf_document = "demo.pdf"  
with open(pdf_document, "rb") as filehandle:  
    pdf = PdfFileReader(filehandle)
    info = pdf.getDocumentInfo()
    pages = pdf.getNumPages()

    print (info)
    print ("number of pages: %i" % pages)

    page1 = pdf.getPage(1)
    print(page1)
    print(page1.extractText())
