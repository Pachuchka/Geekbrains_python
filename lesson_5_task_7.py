from json import dump

with open("Фирмы.txt","r",encoding="utf-8") as my_f:
    _data_list = my_f.read().split('\n')
_result_list = []
_firm_list=[]
_value_list = []

i=0
while i<len(_data_list):
    _data_str = _data_list[i].split()
    _n = len(_data_str)
    _expenses = float(_data_str[_n-1])
    _income = float(_data_str[_n-2])
    _orgform = _data_str[_n-3]
    j=0
    _org_name = ""
    while j< len(_data_str)-3:
        _org_name = _org_name + _data_str[j] + " "
        j=j+1
    _value = _income-_expenses
    _firm_list.append(_org_name)
    _value_list.append(_value)
    i=i+1
k = 0
_n=0
_sum_value =0
while k<len(_value_list):
    if _value_list[k]>0:
        _sum_value = _sum_value + float(_value_list[k])
        _n=_n+1
        k=k+1
    else:
        k=k+1
_average_prof = _sum_value/_n
_result = dict(zip(_firm_list,_value_list))
_result_list.append(_result)
_d = {'average_profit':_average_prof}
_result_list.append(_d)
print(_result_list)
with open("json.txt","a+",encoding="utf-8") as my_f:
    dump(_result_list[0], my_f, indent=2, ensure_ascii=False)
    dump(_result_list[1], my_f, indent=2, ensure_ascii=False)