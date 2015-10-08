from graphics import *
import random


# change seq visulize your rotations
# press space to watch next rotation

# use scramble_seq to scramble the rubik
scramble_seq = []
#scramble_seq = [random.randint(-5,6) for i in xrange(10)]
#scramble_seq = map(lambda x: x-1 if x<=0 else x,scramble_seq)
print scramble_seq

# use seq to solve the rubik, will show each step
seq = [-6,-4,2,-1,-4,-2,6,3,-4,-6]
board = [["YYY",
          "YYY",
          "YYY"],
         ["BBB",
          "BBB",
          "BBB"],
         ["GGG",
          "GGG",
          "GGG"],
         ["MMM",
          "MMM",
          "MMM"],
         ["WWW",
          "WWW",
          "WWW"],
         ["RRR",
          "RRR",
          "RRR"]]
board = [["YGB",
          "WBB",
          "OOR"],
         ["WWW",
          "WWR",
          "YWY"],
         ["OOB",
          "GGR",
          "ORR"],
         ["YYR",
          "YYO",
          "GYW"],
         ["BOO",
          "YRG",
          "RRG"],
         ["GGG",
          "BOB",
          "BBW"]]


colors = {'Y':'yellow',
          'B':'blue',
          'G':'green',
          'O':'orange',
          'R':'red',
          'W':'pink'}


def up_face(x,y,k):
  return [[[Point(x+2*j*k-i*k,y+i*k),
            Point(x+2*k+2*j*k-i*k,y+i*k),
            Point(x+k+2*j*k-i*k,y+k+i*k),
            Point(x-k+2*j*k-i*k,y+k+i*k)] for j in xrange(3)] for i in xrange(3)]

def right_face(x,y,k):
  return [[[Point(x+j*k,y+2*i*k-j*k),
            Point(x+k+j*k,y-k+2*i*k-j*k),
            Point(x+k+j*k,y+k+2*i*k-j*k),
            Point(x+j*k,y+2*k+2*i*k-j*k)] for j in xrange(3)] for i in xrange(3)]

def face(x,y,k):
  return [[[Point(x+2*j*k,y+2*i*k),
            Point(x+2*j*k+2*k,(y+2*i*k)),
            Point(x+2*j*k+2*k,(y+2*i*k+2*k)),
            Point(x+2*j*k,(y+2*i*k+2*k))] for j in xrange(3)] for i in xrange(3)]
faces = []
ox,oy,k = 200,200,10 # center, scale
for x,y,f in [(-6,0,face),(0,0,face),(6,0,right_face),(9,-3,face),(3,-3,up_face),(0,6,face),]:
  faces.append(f(x*k+ox,y*k+oy,k))



rot1 = [[(1,0,0),(1,0,1),(1,0,2),(1,1,2),(1,2,2),(1,2,1),(1,2,0),(1,1,0)],
       [(2,0,0),(2,0,1),(2,0,2),(2,1,2),(2,2,2),(2,2,1),(2,2,0),(2,1,0)],
       [(3,0,0),(3,0,1),(3,0,2),(3,1,2),(3,2,2),(3,2,1),(3,2,0),(3,1,0)],
       [(4,0,0),(4,0,1),(4,0,2),(4,1,2),(4,2,2),(4,2,1),(4,2,0),(4,1,0)],
       [(5,0,0),(5,0,1),(5,0,2),(5,1,2),(5,2,2),(5,2,1),(5,2,0),(5,1,0)],
       [(6,0,0),(6,0,1),(6,0,2),(6,1,2),(6,2,2),(6,2,1),(6,2,0),(6,1,0)]]

rot2 = [[(5,0,0),(5,1,0),(5,2,0),(2,0,0),(2,1,0),(2,2,0),(6,0,0),(6,1,0),(6,2,0),(4,2,2),(4,1,2),(4,0,2)],
        [(5,2,0),(5,2,1),(5,2,2),(3,0,0),(3,1,0),(3,2,0),(6,0,2),(6,0,1),(6,0,0),(1,2,2),(1,1,2),(1,0,2)],
        [(5,2,2),(5,1,2),(5,0,2),(4,0,0),(4,1,0),(4,2,0),(6,2,2),(6,1,2),(6,0,2),(2,2,2),(2,1,2),(2,0,2)],
        [(5,0,2),(5,0,1),(5,0,0),(1,0,0),(1,1,0),(1,2,0),(6,2,0),(6,2,1),(6,2,2),(3,2,2),(3,1,2),(3,0,2)],
        [(4,0,2),(4,0,1),(4,0,0),(3,0,2),(3,0,1),(3,0,0),(2,0,2),(2,0,1),(2,0,0),(1,0,2),(1,0,1),(1,0,0)],
        [(2,2,0),(2,2,1),(2,2,2),(3,2,0),(3,2,1),(3,2,2),(4,2,0),(4,2,1),(4,2,2),(1,2,0),(1,2,1),(1,2,2)]]

def rotate(x):
  global board, rot1, rot2
  left = (x<0)
  if x<0: x=-x
  x -= 1
  b1 = [board[f-1][i][j] for (f,i,j) in rot1[x]]
  b2 = [board[f-1][i][j] for (f,i,j) in rot2[x]]
  if left:
    b1 = b1[2:]+b1[:2]
    b2 = b2[3:]+b2[:3]
  else:
    b1 = b1[-2:]+b1[:-2]
    b2 = b2[-3:]+b2[:-3]
  for k in xrange(8):
    f,i,j = rot1[x][k]
    board[f-1][i][j] = b1[k]
  for k in xrange(12):
    f,i,j = rot2[x][k]
    board[f-1][i][j] = b2[k]

board = [[list(line) for line in f] for f in board]

def draw_rubik(win):
  global faces, board, colors
  for f in xrange(6):
    for i in xrange(3):
      for j in xrange(3):
        vs = faces[f][i][j]
        poly = Polygon(vs)
        poly.setFill(colors[board[f][i][j]])
        poly.setWidth(2)
        poly.draw(win)

def print_board():
  global board
  b = [[''.join(i) for i in f]  for f in board]
  for i in b[4]:
    print i

  for i in xrange(3):
    print b[0][i] + b[1][i] + b[2][i] + b[3][i] 
  for i in b[5]:
    print i

def main():
    global seq
    win = GraphWin('Rubik', 400,400) # give title and dimensions
    for x in scramble_seq:
      rotate(x)
    print_board()
    draw_rubik(win)
    win.getKey()
    for x in seq:
      label = Text(Point(100, 120), str(x))
      label.draw(win)
      win.getKey()
      rotate(x)
      draw_rubik(win)
      label.undraw()
      win.flush
    print_board()
    win.getMouse()
    win.close()

main()
