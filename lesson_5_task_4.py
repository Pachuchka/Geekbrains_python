from googletrans import Translator

translator = Translator()
_my_f = open("translate.txt","r",encoding="utf-8")
_content_list = _my_f.read().split("\n")
i=0
print(_content_list)
while i< len(_content_list):
    _file_str = _content_list[i].split("-")
    f_word = _file_str[0]
    text = translator.translate(f_word, src='en', dest='ru')
    print(text)
    i=i+1