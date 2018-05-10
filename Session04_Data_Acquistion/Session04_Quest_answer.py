import json
from urllib.request import urlopen

#ip 값은 크게 상관 없음.
#위도와 경도 값만 잘 나오면 GOOD!
html = urlopen("https://freegeoip.net/json/110.14.74.130")
json_string = html.read()
json_parced = json.loads(json_string)

print('latitude: ', json_parced['latitude'])
print('longitude: ', json_parced['longitude'])