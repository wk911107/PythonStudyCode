from urllib import request

if __name__ == "__main__":
    url = "http://www.csdn.net/"
    req = request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit\
            /537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)
