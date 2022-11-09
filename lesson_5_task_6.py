with open("Уроки.txt","r",encoding="utf-8") as my_f:
    _data_list = my_f.read().split('\n')
i=0
_lesson_list = []
_hours = []
_result_hours = []
while i<len(_data_list):
    _data_str = _data_list[i].split(':')
    _lesson_list.append(_data_str[0])
    _hours = _data_str[1].split()
    
    j=0
    _sum=0
    while j < len(_hours):
        try:
            _t=_hours[j].split('(')
        except:
            j=j+1
        else:
            if _t[0]!="—":
                _sum = _sum + int(_t[0])
                j = j + 1
            else:
                j=j+1

    _result_hours.append(_sum)
    #print(f"урок {_lesson_list[i]} запланировано {_sum} часов")

    i=i+1
_my_dict = dict(zip(_lesson_list,_result_hours))
print(_my_dict)