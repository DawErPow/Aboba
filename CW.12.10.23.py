#Первое задание
def remove_char(str):
    return str[1: - 1]

#Второе задание
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
      
#Третие задание
def set_alarm(employed, vacation):
  alarm = False;
  if employed is True and vacation is False:
    alarm = True;
  return alarm;

#Четвертое задание
def greet(name):
    return "Hello, " + name + " how are you doing today?"
      
#Пятое задание
def make_upper_case(s):
    return s.upper()
      
#Шестое задание
def fake_bin(x):
    return ''.join(('1', '0')[i < '5'] for i in x)
      
#Седьмое задание
def opposite(number):
    return number*(-1)
      
#Восьмое задание
def remove_every_other(my_list):
    return my_list[::2]
      
#Девятое задание
def century(year):
    return (year + 99) // 100

#Десятое задание
def double_char(s):
    return "".join([c * 2 for c in s])
