import sys, time

class TrafficLight:
  def __init__(self, color):
    self.color = color 
  def getColor(self):
    return self.color
  def change1(self):
    if self.color =='G':
      self.color = 'Y'
  def change2(self):
    if self.color == 'Y':
      self.color = 'R'
    elif self.color == 'R':
      self.color = 'G'
    
class Timer:
  event1_callback = []
  event2_callback = []
  def __init__(self):
    self.t = 0
  def add(self):
    self.t += 1
    tt = self.t % 8
    if tt == 5:
      self.event1()
    elif tt == 0:
      self.event2()
  def event1(self):
    for e in self.event1_callback:
      e()
  def event2(self):
    for e in self.event2_callback:
      e()
  def subscribe1(self, observer):
    self.event1_callback.append(observer)
  def subscribe2(self, observer):
    self.event2_callback.append(observer)
  



def draw(l1,l2,l3,l4,t):
  print '                    |   |                  %d'%t
  print '                    | %c |'%l1
  print '--------------------    ---------------------'
  print '                    %c   %c'%(l2,l3)
  print '--------------------    ---------------------'
  print '                    | %c |'%(l4)
  print '                    |   |'

timer = Timer()

l1 = TrafficLight('R')
l2 = TrafficLight('G')
l3 = TrafficLight('G')
l4 = TrafficLight('R')
timer.subscribe1(l1.change1)
timer.subscribe1(l2.change1)
timer.subscribe1(l3.change1)
timer.subscribe1(l4.change1)

timer.subscribe2(l1.change2)                                                    
timer.subscribe2(l2.change2)                                                    
timer.subscribe2(l3.change2)                                                    
timer.subscribe2(l4.change2) 

for t in xrange(1,100):
  draw(l1.getColor(),l2.getColor(),l3.getColor(),l4.getColor(),t)
  time.sleep(1)
  timer.add()
  sys.stderr.write("\x1b[2J\x1b[H")
  sys.stdout.flush()
