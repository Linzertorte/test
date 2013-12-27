def ordc(c):
    return ord(c)-ord('0')

def get(i,j,field):
    if i in range(0,9) and j in range(0,9) and field[i][j]=='M':
        return 1
    else:
        return 0

def fillnum(i,j,field):
    if field[i][j]=='M':
        return 'M'
    cnt = 0
    cnt += get(i-1,j-1,field)+get(i-1,j,field)+get(i-1,j+1,field)+get(i,j-1,field)
    cnt += get(i,j+1,field)+get(i+1,j-1,field)+get(i+1,j,field)+get(i+1,j+1,field)
    return chr(cnt+ord('0'))
    
class MineField:
    def getMineField(self,mines):
        #parse mines to a list of tuples
        #set M to the locations
        #iterate to get the number
        locations = []
        i = 0
        while i<len(mines):
            locations.append((ordc(mines[i+1]),ordc(mines[i+3])))
            i += 5
        #print locations
        
        field=[]
        for i in xrange(0,9):
            field.append(['0' for x in xrange(0,9)])
        #print field
        for mine in locations:
            field[mine[0]][mine[1]] = 'M'
        
        i,j=0,0
        for i in xrange(0,9):
            for j in xrange(0,9):
                field[i][j]=fillnum(i,j,field)

        ret=()
        for line in field:
            ret += (''.join(line),)
        return ret

        
