import numpy as np
import xlrd
import sys
import getopt

def read_file_data(filename):
    book = xlrd.open_workbook(filename, encoding_override = 'utf-8')
    sheet = book.sheet_by_index(0)
    x_data = np.asarray([sheet.cell(i, 0).value for i in range(1, sheet.nrows)])
    y_data = np.asarray([sheet.cell(i, 1).value for i in range(1, sheet.nrows)])
    
    return x_data, y_data

def generate_rewrite_file(x_data, y_data, outputfile, host):
    f = open(outputfile, 'w')
    for i in range(0, x_data.size):
        x = x_data[i]
        y = y_data[i]
        f.write(create_rewrite(x, y, host) + "\n")
    

def create_rewrite(x, y, host):
    x = x.replace(host, '')
    return 'rewrite ^{0}?$ {1}{2} permanent;'.format(x, host, y)

def main(argv):
    inputfile = ''
    outputfile = ''
    host = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:o:d:', ['ifile=', 'ofile=', 'host='])
    except getopt.GetoptError:
        print('redirects.py -i <inputfile> -o <outputfile> -d <host>')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('redirects.py -i <inputfile> -o <outputfile> -d <host>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-d", "--host"):
            host = arg

    x_data, y_data = read_file_data(inputfile)
    generate_rewrite_file(x_data, y_data, outputfile, host)
    

if __name__ == "__main__":
   main(sys.argv[1:])
