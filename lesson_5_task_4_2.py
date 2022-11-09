from requests import post
_my_f = open("translate.txt","r",encoding="utf-8")
_content_list = _my_f.read().split("\n")
i=0
while i< len(_content_list):
    _file_str = _content_list[i].split()
    f_word = _file_str[0]
    print(f_word)
    key = 'dict.1.1.20221107T141055Z.9ad9ecc4634c0ae6.4e6aa3fee959126f6a9ca9fb38d1d424f5b8da5e'
    data = {'lang': 'ru',
            'key': key,
            'text': f_word,
            'format': 'plain'
            }
    _r = post('https://translate.yandex.net/api/v1.5/tr.json/translate', data=f_word).json()
    _r['text'] = f_word
    print(_r)
    i=i+1
_translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять','six': 'шесть','seven': 'семь'}
i=0
while i<len(_content_list):
    _file_str = _content_list[i].split()
    f_word = _file_str[0]
    _new_str = _translate_dict[f_word.lower()] + " " + _file_str[1] + " "+ _file_str[2]+'\n'
    with open("result.txt","a+",encoding="utf-8") as my_f:
        my_f.write(_new_str)
    i=i+1

