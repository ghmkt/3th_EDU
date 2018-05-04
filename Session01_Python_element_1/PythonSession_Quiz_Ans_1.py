# 백준 알고리즘 1924번
month, day = map(int, input().split(' '))

day += sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:month])
_day_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

print(_day_of_week[(day-1) % 7])

# 백준알고리즘 2839번
# gghso님 코드(from 숏코딩)
i=int(input());c=0
while i%5:i-=3;c+=1
print(-1 if i<0 else i//5+c)

# 백준알고리즘 4344번
num_of_TestCase = int(input())

for i in range(num_of_TestCase):
    _temp = [int(x) for x in list(input().split(" "))]
    _num, _list = _temp[0], _temp[1:]
    _avg = sum(_list) / _num
    a = [x for x in _list if x > _avg]
    prob = 100 * (len(a) / len(_list))
    print("{0:.3f}%".format(prob))
