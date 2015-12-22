# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
def daum(word):
  """ word is a utf-8 str, return a unicode string """
  html = urllib2.urlopen("http://dic.daum.net/search.do?q=%s&dic=ch"%word)
  soup = BeautifulSoup(html, 'lxml')
  output = u""+word.decode("utf-8")
  section_mean = soup.find("section",attrs={"class":"#mean"})
  for p in section_mean.find_all("div",attrs={"class":"ch_sch"}):
    output += p.find("a",attrs={"class":"link_txt"}).text+u";"
  i = 1
  for p in soup.find_all("div", attrs={"class": "desc_KOKC"}):
    sen = u" "+str(i)+u". "
    sen += p.find("div",attrs={"class":"txt"}).find("span",attrs={"class":"inner"}).text.lstrip().rstrip()
    sen +=  p.find("div",attrs={"class":"trans"}).find("span",attrs={"class":"inner"}).text.lstrip().rstrip()
    if len(output) + len(sen) <= 140:
      output+=sen
      i+=1
  return output
