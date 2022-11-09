_my_f = open("user_content.txt","r",encoding="utf-8")
_content_list = _my_f.read().split("\n")
if _content_list[len(_content_list)-1]=="":
    n = len(_content_list)-1
else: n = len(_content_list)
i=0
while i < n:
    _nwords = len(_content_list[i].split())
    print(f"Строка номер {i+1} содержит {_nwords} слов")
    i=i+1

_my_f.close()