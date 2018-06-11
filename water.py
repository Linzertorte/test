import sys

def remove_watermark(keyword, source, destination=None):
    if not destination:
        destination = source.split(".")[0] + "_clean.pdf"
    book = open(source, "rb")
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

if __name__ == '__main__':
    """
    Usage ./water.py keyword source.pdf [destination.pdf]
    run qpdf --stream-data=uncompress input.pdf output.pdf
    """
    remove_watermark(*sys.argv[1:])
