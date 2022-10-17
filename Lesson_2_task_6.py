n = True
_param_List = ['name', 'price', 'num', 'units']
_param_dict ={'name':'', 'price':'', 'num':'', 'units':''}

_new_param = []
_objects_list=[]
cn=0
while n == True:
    cn=cn+1
    _user_element = input('введите номер нового товара, или если вы закончили, введите "-" : ')

    if _user_element != '-':

        k=0
        while k < len(_param_List):
            #_new_param.append[input(f'введите значение параметра  {_param_List[k]}')]
            _param_dict[_param_List[k]] = input(f'введите значение параметра  {_param_List[k]}')
            k=k+1

        else:

            _objects_list.append([_user_element,_param_dict])
            print(_objects_list)

    else:
        #shet=0
       #while shet< len(list[_param_dict.keys()])-1:
            #spisok = ''
           # l=0
              # while l < cn-1:
                    #spisok = spisok + ' ' + _objects_list[l][]
        #analize_dict = {_param_List[1]:str()}
        n=False