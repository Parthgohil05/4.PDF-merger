import PyPDF2
pdfiles = ["pdf1.pdf","pdf2.pdf","pdf3.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdffile=open(filename,'rb')
    pdreader=PyPDF2.PdfReader(pdffile)
    merger.append(pdffile)
pdffile.close()
merger.write('merged.pdf')
