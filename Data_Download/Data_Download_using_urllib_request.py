# 라이브러리 읽어들이기
import urllib.request # urllib 패키지 내부에 있는 request 모듈을 읽어 들인다.

# URL과 저장 경로 설정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드를 요청하는 코드
urllib.request.urlretrieve(url, savename)

print("Saved")