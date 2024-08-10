# -*- coding: utf-8 -*-
start = [1,72,147,187,216, 284,435,535,584,640, 745,815,1035,1081,1156, 1204,1295,1347,1385,1438, 1519,1558,1581,1587,1602, 1619,1710,1778,1858,1885, 1939,1977,2014,2034,2057, 2087,2111,2135, 2167,2181,2210,2214,2229, 2243,2262,2263,2264]
name = []

name.append("あ")
name.append("い")
name.append("う")
name.append("え")
name.append("お")

name.append("か")
name.append("き")
name.append("く")
name.append("け")
name.append("こ")

name.append("さ")
name.append("し")
name.append("す")
name.append("せ")
name.append("そ")

name.append("た")
name.append("ち")
name.append("つ")
name.append("て")
name.append("と")

name.append("な")
name.append("に")
name.append("ぬ")
name.append("ね")
name.append("の")

name.append("は")
name.append("ひ")
name.append("ふ")
name.append("へ")
name.append("ほ")

name.append("ま")
name.append("み")
name.append("む")
name.append("め")
name.append("も")

name.append("や")
name.append("ゆ")
name.append("よ")


name.append("ら")
name.append("り")
name.append("る")
name.append("れ")
name.append("ろ")

name.append("わ")
name.append("を")
name.append("ん")

for i in range(1,len(start)):
  print "pdftk jp.pdf cat %d-%d output %s.pdf"%(start[i-1],start[i]-1,name[i-1])
