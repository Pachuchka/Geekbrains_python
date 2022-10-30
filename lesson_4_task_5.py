from functools import reduce
my_list = [n for n in range(100,1001) if n%2==0 ]
print(my_list)
_multiply = reduce(lambda x,y:x*y,my_list)
print(_multiply)