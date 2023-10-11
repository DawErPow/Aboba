#Первое задание
def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

#Второе задание
     def get_grade(s1, s2, s3):
    a = (s1 + s2 + s3) // 3
    if 90 <= a <= 100:
        return "A"
    elif 80 <= a < 90:
        return "B"
    elif 70 <= a < 80:
        return "C"
    elif 60 <= a < 70:
        return "D"
    else:
        return "F"
      
#Третие задание
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

#Четвертое задание
def sum_array(a):
    return sum(a)
      
#Пятое задание
def count_sheeps(Sheeps):
    return len([sheep for sheep in Sheeps if sheep])
      
#Шестое задание
def summation(num):
    return (num * (num + 1) /2)
      
#Седьмое задание
def past(h, m, s):
    return (h*3600000 +m*60000 +s*1000)
      
#Восьмое задание
def invert(lst):
    return [n * -1 for n in lst] if len(lst) > 0 else []
      
#Девятое задание
def double_integer(i):
    return 2 * i;

#Десятое задание
def number_to_string(num):
    return str(num)
