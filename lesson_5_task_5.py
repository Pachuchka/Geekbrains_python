from random import randint as rnd
n = rnd(1,100)
i=0
rnd_list=[]
_sum = 0
_random_str = ""
while i < n:
    rnd_list.append(rnd(1,25))
    _random_str = _random_str + str(rnd_list[i]) + " "
    i = i + 1
with open("random.txt","x",encoding="utf-8") as my_f:
        my_f.write(_random_str)
with open("random.txt","r",encoding="utf-8") as my_f:
    _int_list = my_f.read().split()
i=0
while i < len(_int_list):
    _sum = _sum + int(_int_list[i])
    i=i+1
print (_sum)