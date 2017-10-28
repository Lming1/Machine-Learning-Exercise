import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test_urlopen.png"

# urlopen() >> url에 있는 읽어들이고 파이썬 메모리에 저장한다, 저장후 mem 변수에 저장
mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("Saved")
