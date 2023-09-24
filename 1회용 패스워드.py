import random

q = int(input('몇 자리의 비밀번호를 원하십니까? '))
result = ''
a = [('A', 25), ('a', 25), ('0', 9)]

for i in range(q):
    ran = random.choice(a)
    result += chr(ord(ran[0]) + random.randint(0, ran[1]))

print(result)
