import re
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import requests
import json
AWS_KEY = 'AKIAIX5U3UWPZMIVRUBA'
AWS_SECRET = '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'
s3_conn = S3Connection(AWS_KEY, AWS_SECRET)
POST_URL = 'http://jlusv-jlusv.rhcloud.com/zmsWJoP9BGSf3xGDRvq9yEKF'
ID_URL = 'http://jlusv-jlusv.rhcloud.com/0n5hq1wo6B4f'


req = requests.get(ID_URL)
pid = int(req.text)

f = open('article.txt')
content = f.read()
raw_images = re.findall(r'\[\[[^\]]*\]\]',content)
images = []
for img in raw_images:
  images.append(img[2:-2])

content = re.sub(r'\[\[([^\]]*)\]\]',r'[[%d_\1]]'%pid,content)

article = {}
article['id'] = pid
article['content']= content
article['title'] = raw_input('title: ')
article['date'] = raw_input('date: ')
article['author'] = raw_input('author: ')

bucket = s3_conn.get_bucket('jlusv')
cnt = len(images)
for i in xrange(cnt):
  img = images[i]
  print '[%d/%d]%s'%(i+1,cnt, str(pid)+'_'+img)
  k = Key(bucket)
  k.key='web/'+str(pid)+'_'+img
  k.set_contents_from_filename(img)
  k.make_public()

req = requests.post(POST_URL, json = article)
print req.text
print 'New article available at http://www.jlu-sv.org/p/'+str(pid)  
