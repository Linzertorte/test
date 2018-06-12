import sys
import os

def remove_watermark(keyword, source, destination=None):
    f_name = source.split(".")[0]
    t = f_name + '_t.pdf'
    if not destination:
        destination = f_name + "_clean.pdf"
    os.system('qpdf --stream-data=uncompress ' + source + ' ' + t)
    book = open(t, "rb")
    book_clean = open(destination,"wb")
    keep, obj = True, ''
    for line in book:
        if ' obj' in line:
            if keep: book_clean.write(obj)
            keep, obj = True, ''
        elif keyword in line:
            keep = False
        obj += line
    if keep: book_clean.write(obj)
    os.system('rm ' + t)
    print 'Success! Wrote to ' + destination + '.'

if __name__ == '__main__':
    """
    Usage ./water.py keyword source.pdf [destination.pdf]
    """
    remove_watermark(*sys.argv[1:])
