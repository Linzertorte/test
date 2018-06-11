import sys

def remove_watermark(keyword, source, destination=None):
    if not destination:
        destination = source.split(".")[0] + "_clean.pdf"
    f = open(source, "rb")
    book_clean = open(destination,"wb")
    book_content = f.read()
    book_lines = book_content.split('\n')
    line_count = len(book_lines)
    yes = [0]*line_count
    for i in xrange(line_count):
        if ' obj' in book_lines[i]: yes[i] = 1
        elif 'endobj' in book_lines[i]: yes[i] = 2
        elif keyword in book_lines[i]: yes[i] = 3
    for i in xrange(line_count):
        if yes[i] == 3:
            j = i - 1
            while yes[j] != 1:
                yes[j] = 4
                j -= 1
            yes[j] = 4
            j = i + 1
            while yes[j] != 2:
                yes[j] = 4
                j += 1
            yes[j] = 4
    for i in xrange(line_count):
        if yes[i] < 3:
            book_clean.write(book_lines[i] + '\n')


if __name__ == '__main__':
    """
    Usage ./water.py keyword source.pdf [destination.pdf]
    """
    remove_watermark(*sys.argv[1:])
