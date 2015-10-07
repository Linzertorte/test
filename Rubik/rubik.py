from graphics import *

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

def main():
    win = GraphWin('Face', 400,400) # give title and dimensions
    colors = {'Y':'yellow',
              'B':'blue',
              'G':'green',
              'M':'orange',
              'R':'red',
              'W':'pink'} 
    global faces,board
    board = [[list(line) for line in f] for f in board]
    for x in [5,-1,2,1,-1,-2,1,-5,1]:
      for f in xrange(6):
        for i in xrange(3):
          for j in xrange(3):
            vs = faces[f][i][j]
            poly = Polygon(vs)
            poly.setFill(colors[board[f][i][j]])
            poly.setWidth(2)
            poly.draw(win)
      win.getKey()
      rotate(x)
      win.flush
    win.getMouse()
    win.close()

main()