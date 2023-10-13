#Первое задание
def remove_exclamation_marks(s):
    return s.replace('!', '')
#Второе задание
def sum_mix(arr):
    return sum([int(n) for n in arr])
      
#Третие задание
def get_volume_of_cuboid(length, width, height):
    return (length*width*height)

#Четвертое задание
def simple_multiplication(number) :
    return 9*number if number % 2 > 0 else 8*number
      
#Пятое задание
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    return (l + w) * 2
      
#Шестое задание
def switch_it_up(number):
    switcher = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    return switcher.get(number)
      
#Седьмое задание
def two_sort(array):
    return "***".join(min(array))
      
#Восьмое задание
def other_angle(a, b):
    return 180 - (a + b)
      
#Девятое задание
def bool_to_word(lox):
    if lox == True:
        return "Yes"
    else:
        return "No"

#Десятое задание
def sum_array(a):
    return sum(a)
