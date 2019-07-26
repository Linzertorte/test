# -*- coding: utf-8 -*-
import os
with open("naruto.txt") as f:
  for line in f.readlines():
    line = line.strip()
    url,name = line.split('|')
    cmd = 'ffmpeg -user_agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7" -i "%s" -bsf:a aac_adtstoasc -c copy "%s"'%(url,name)
    print 'Downloading',name,'...'
    os.system(cmd)
