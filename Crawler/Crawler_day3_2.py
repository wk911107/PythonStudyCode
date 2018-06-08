"""
HTTPError的演示
"""
from urllib import request
from urllib import error


url = 'http://douyu.com/WangKE.c.html'
try:
    req = request.urlopen(url)
except error.HTTPError as e:
    print(e.code)
