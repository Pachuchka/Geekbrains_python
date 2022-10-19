print('задача 2')
_seconds = int(input('Введите количество секунд '))
_hours = _seconds//3600
_minuts = _seconds//60
_result_minuts =(_seconds - _hours * 3600)//60
_result_seconds = _seconds - _hours * 3600 - _result_minuts*60
print(_hours)
print(_minuts)
print(_result_minuts)
print(_result_seconds)
_time = str(_hours) + ":"+str(_result_minuts)+":"+str(_result_seconds)
print(_time)