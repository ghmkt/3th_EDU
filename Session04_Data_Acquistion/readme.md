Session04_Data_Acquistion

===

세션목표
---
 - 데이터 시각화의 의의를 알고 원, 막대, 산점도 등 기본적인 시각화를 배운다.
 - 데이터를 정제하고 다차원 데이터 분석을 공부한다.

담당자
---
 - 김재훈

파일소개
---
   
 - [Sesstion_PPT](./Session04_Data_Acquistion.pdf) 세션발표에서 사용된 PPT파일입니다.
 - [Quest_Answer](./Session04_Quest_answer.py) 퀘스트 정답 파일입니다.
 - [Quest csv](./Quest_csv) 퀘스트에 이용되는 csv파일입니다.
 


목차
---
   
 - 상황에 맞는 시각화
 - 파이썬 시각화의 기본(+ Tableau)
 - 1,2차원 데이터 분석
 - 척도조절 차원조절 
 
 
퀘스트
---
사용중인 IP주소의 위도와 경도를 알려주는 코드를 작성해보자.
 - https://freegeoip.net/json/[**IP주소값**]  에서 json 형식의 문자열을 스크래핑 해온다.
 - json 라이브러리를 사용하여 문자열을 dictionary 형식으로 바꾼 뒤 해당 데이터에서 위도와 경도 정보를 뽑아낸다.
 - 뽑아낸 데이터를 각자 선호하는 방식으로 출력한다. 
   print()를 해도 좋고, Pandas의 데이터프레임으로 출력하거나, SQlite3에 저장한 뒤 DB내역을 스크린샷으로 찍어도 좋다.
   단, 출력에는 입력한 IP, 위도, 경도 정보는 무조건 들어있어야 한다.


   현재 사용 중인 인터넷의 IP 주소를 아는 사이트    https://www.whatismyip.com/
