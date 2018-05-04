# 첫번째 연습문제
temp = [(i,j) for i in range(10) for j in range(10) if i%3==0 and j%3==0]
print(temp)

# 두번째 연습문제
def test(file_name):
    temp = []
    try:
        f = open("c:\\Users\\LYJ\\Desktop\\대학\\Growth_Hackers\\GH_Quest\\" + file_name, 'r')
    except:
        print("파일 경로 및 이름을 확인해주세요")
    else:
        lines = f.readlines()
        temp = lines
        f.close()

    f = open("c:\\Users\\LYJ\\Desktop\\"+file_name+"_new.csv", 'w')

    for line in temp:
        line = line.split(',')
        line.reverse()
        line[0] = line[0].strip()
        _str = ",".join(line) + "\n"
        f.write(_str)

    print("생성 완료")
    f.close()

test("diamonds_data.csv")

