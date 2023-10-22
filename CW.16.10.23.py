#Первое задание
def to_alternating_case(string):
    return "".join([c.swapcase() for c in string])
#Второе задание
def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30
      
#Третие задание
def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"

#Четвертое задание
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0
      
#Пятое задание
def correct(string):
    return string.translate(str.maketrans("501", "SOI"))
      
#Шестое задание
def hero(bullets, dragons):
    return bullets >= dragons * 2
      
#Седьмое задание
def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2
      
#Восьмое задание
      def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
#Девятое задание
def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')

#Десятое задание
def DNAtoRNA(dna):
    return dna.replace('T', 'U')
