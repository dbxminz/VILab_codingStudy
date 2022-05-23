## Q2 곱하기 혹은 더하기 ##

# 처음에 문제 이해를 잘못했음
# +, * 아무거나 사용 해도 되고 입력된 문자열 왼쪽부터 봐야되므로 수정 불가능함
# 그러면 +기는 0,1일때만 쓰면 됨 나머지는 다 곱하기

data = input()

# 입력문자열의 앞에 첫 부분만 0이면 이상하게 print값이 안나옴
results = int(data[0])



for i in range(1,len(data)):
  if data[i] == 0 or data[i] == 1 or results == 0:
    results += int(data[i])
  else:
    results = results * int(data[i])

print(results)