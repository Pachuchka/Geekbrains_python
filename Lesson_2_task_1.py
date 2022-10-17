_user_list =['1',2,[3,4],"5",False, -1, 1.2]
_user_type=[]
n=0
while n <len(_user_list):
    print(type(_user_list[n]))
    _user_type.append(type(_user_list[n]))
    n=n+1
print(_user_type)

