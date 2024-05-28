**PDF Merger**

This Python script merges multiple PDF files into a single PDF file using the PyPDF2 library.

### Prerequisites
- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)

### Usage
1. Make sure you have Python installed on your system.
2. Install the PyPDF2 library by running `pip install PyPDF2`.
3. Place the script in the directory containing the PDF files you want to merge.
4. Update the `pdfiles` list with the names of the PDF files you want to merge.
5. Run the script.

### Description
- The script imports the `PyPDF2` library, which is used to work with PDF files.
- It specifies a list of PDF files (`pdfiles`) that need to be merged.
- The `PdfMerger` object from PyPDF2 is created to handle the merging process.
- A loop iterates over each PDF file in the list, opens it in binary read mode, and appends it to the merger object.
- After appending all PDF files, the merged content is written to a new PDF file named 'merged.pdf'.
- Finally, the script closes all open file handles.

### Example
```python
import PyPDF2

# List of PDF files to merge
pdfiles = ["pdf1.pdf", "pdf2.pdf", "pdf3.pdf"]

# Create PdfMerger object
merger = PyPDF2.PdfMerger()

# Append each PDF file to merger
for filename in pdfiles:
    pdffile = open(filename, 'rb')
    merger.append(pdffile)
    pdffile.close()

# Write merged content to 'merged.pdf'
merger.write('merged.pdf')
```

### Notes
- Ensure that the PDF files you want to merge are located in the same directory as the script.
- The merged PDF file will be created in the same directory as the script.
- The script overwrites any existing 'merged.pdf' file without warning.
