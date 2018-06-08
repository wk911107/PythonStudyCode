from urllib import request
from urllib import error


url = 'http://www.douyu.com/Wang_KK.html'
req = request.Request(url)
try:
    response = request.urlopen(req)
except error.URLError as e:
    if hasattr(e, 'code'):
        print('HTTPError')
        print(e.code)
    elif hasattr(e, 'reason'):
        print('URLError')
        print(e.reason)
