# requires pip install PyPDF2
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
import csv

#reader = PyPDF2.PdfFileReader('./files/Prueba.pdf')

def main(argv):
    pdf_file = argv[0]
    register_file = argv[1]
    if len(list(argv)) == 2:
        # 5 because goes for the common structure
        field = 5
    else:
        field = argv[2]

    print('File to be analyzed: '+pdf_file)
    print('File for register: '+register_file)

    data = ""
    lines = 0

    with open(register_file,"r", encoding='utf-8') as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        lines = len(data)

    print('Number of files to be produced:'+str(lines))

    if lines != 0:
        with open(pdf_file, 'rb') as infile:
            reader = PdfFileReader(infile)
            print(reader.numPages)
            for i in range(0, reader.numPages, 2):
                writer = PdfFileWriter()
                writer.addPage(reader.getPage(i))
                writer.addPage(reader.getPage(i+1))
                with open('./output/'+str(data[int(i/2) + 1][field])+'.pdf', 'wb') as outfile:
                    print('./output/'+str(data[int(i/2) + 1][field])+'.pdf')
                    writer.write(outfile)

    else:
        print('The CSV file was not uploaded correctly.')

if __name__ == "__main__":
    main(sys.argv[1:])
