'''Usage
   python mynuid.py username password
'''

import requests
import re
import sys

def get_nuid(user,pwd):
  s = requests.Session()
  r = s.get('http://myneu.neu.edu/cp/home/displaylogin')
  uuid = re.findall('uuid.value="(.*)"',r.text)[0]
  data = {'user':user,'pass':pwd,'uuid':uuid}
  r = s.post('https://myneu.neu.edu/cp/home/login', data=data)
  r = s.get('http://myneu.neu.edu/cps/welcome/loginok.html')
  r = s.get('http://myneu.neu.edu/cp/home/next')
  r = s.get('http://myneu.neu.edu/render.userLayoutRootNode.uP?uP_root=root')
  r = s.get('http://myneu.neu.edu/tag.6397fbedd29686d.render.userLayoutRootNode.uP?uP_root=root&uP_sparam=activeTab&activeTab=u117660l1s42&uP_tparam=frm&frm=')
  nuid = re.findall('Your NUID is (\d+)', r.text)[0]
  return nuid

if __name__ == '__main__':
  print 'Your NUID is', get_nuid(sys.argv[1],sys.argv[2])
