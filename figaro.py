import sys
import os

def remove_watermark(keyword, source, destination=None):
    f_name = source.split(".")[0]
    t1 = f_name + '_t1.pdf'
    t2 = f_name + '_t2.pdf'
    if not destination:
        destination = f_name + "_clean.pdf"
    os.system('qpdf --stream-data=uncompress ' + source + ' ' + t1)
    book = open(t1, "rb")
    book_clean = open(t2, "wb")
    book_content = book.read()
    book_lines = book_content.split('\n')
    line_count = len(book_lines)
    yes = [0] * line_count
    for i in xrange(line_count):
        if keyword in book_lines[i]: yes[i] = 3
        elif 'endstream' in book_lines[i]: yes[i] = 2
        elif 'stream' in book_lines[i]: yes[i] = 1
    for i in xrange(line_count):
        if yes[i] == 3:
            j = i - 1
            while yes[j] != 1:
                yes[j] = 4
                j -= 1
            if 'endstream' in book_lines[i]:
                yes[i] = 5
                continue
            j = i + 1
            while yes[j] != 2:
                yes[j] = 4
                j += 1
            yes[j] = 5
    byte_cnt = 0
    for i in xrange(line_count):
        if yes[i] > 2:
            byte_cnt += len(book_lines[i]) + 1
            if yes[i] == 5:
                byte_cnt -= len('\nendstream\n')
                book_clean.write(' ' * byte_cnt + '\nendstream\n')
                byte_cnt = 0
        else: book_clean.write(book_lines[i] + '\n')
    book_clean.close()
    os.system('qpdf --stream-data=compress ' + t2 + ' ' + destination)
    os.system('rm ' + t1)
    os.system('rm ' + t2)
    print 'Success! Wrote to ' + destination

if __name__ == '__main__':
    """
    Usage ./figaro.py keyword source.pdf [destination.pdf]
    """
    remove_watermark(*sys.argv[1:])
