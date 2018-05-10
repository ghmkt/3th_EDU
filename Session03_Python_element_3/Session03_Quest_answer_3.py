# 클래스 연습문제
class stock_analysis:
   def __init__(self, code):
       try:
           with open("c:\\Users\\LYJ\\Desktop\\파이썬세션데이터\\{0}.csv".format(code)) as f:
               self.lines = f.readlines()
       except FileNotFoundError:
           print("{0} 파일을 로드하는데 실패했습니다".format(code))
       else:
           self.len = len(self.lines)
           self.latest_close = int(self.lines[-1].split(',')[4])
           self.latest_open = int(self.lines[-1].split(',')[1])
           self.latest_low = int(self.lines[-1].split(',')[2])
           self.latest_high = int(self.lines[-1].split(',')[3])

   def close_mean(self):
       close = [int(line.split(',')[4]) for line in self.lines[1:]]
       return (sum(close) // len(close))

   def close_variance(self):
       return sum([(int(line.split(',')[4]) - self.close_mean())**2 for line in self.lines[1:]]) / len(self.lines[1:])

   def close_std(self):
           return self.close_variance()**0.5

   def volume_mean(self):
       volume = [int(line.split(',')[5].strip()) for line in self.lines[1:]]
       return (sum(volume) // len(volume))

   def MA5(self):
       MA5_dict = {}
       for i in range(5,self.len):
           MA5_dict[self.lines[i].split(',')[0]] = sum([int(self.lines[i].split(',')[4]) for i in range(i-4,i+1)]) / 5
       return MA5_dict

# 판다스 연습문제
import pandas as pd

df = pd.read_csv("c:\\Users\\LYJ\\Desktop\\파이썬세션데이터\\네이버_new.csv", engine='python')

# 1번
df["종가"] = df["종가"].apply(lambda x: x*(-1))

# 2번
df['상승폭'] = ((df['종가'] - df['시가'])/df['시가']) * 100

# 3번
# 범위에 맞게 적절히 수정
print(df['종가'][30:60])

# 4번
vol_mean = df['거래량'].mean()
print(df[df['거래량'] > vol_mean * 1.5]['종가'].mean())


