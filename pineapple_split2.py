# -*- coding: utf-8 -*-
prefix = "あ"
i_name = "a"
start = [1]
name = []

# add ending page

name.append(prefix)
start.append()

name.append(prefix+"あ")
start.append()

name.append(prefix+"か")
start.append()

name.append(prefix+"さ")
start.append()

name.append(prefix+"た")
start.append()

name.append(prefix+"な")
start.append()

name.append(prefix+"は")
start.append()

name.append(prefix+"ま")
start.append()

name.append(prefix+"や")
start.append()

name.append(prefix+"ら")
start.append()

name.append(prefix+"わ")
start.append()

name.append(prefix+"ん")
start.append()

for i in range(1,len(start)):
  print("pdftk %s.pdf cat %d-%d output %s.pdf"%(i_name,start[i-1],start[i],name[i-1]))
