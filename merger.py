#!/usr/bin/python

import sys
import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

inDir = sys.argv[1]

print "Merging PDF files in:", inDir

merger = PdfFileMerger()

for filename in glob.glob(inDir + "/*.pdf"):
    merger.append(PdfFileReader(file(filename, 'rb')))

merger.write("document-output.pdf")
