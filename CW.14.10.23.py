#Первое задание
def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])
#Второе задание
def min_max(lst):
    return [min(lst), max(lst)]
      
#Третие задание
def row_sum_odd_numbers(n):
    return n*n*n

#Четвертое задание
def final_grade(exam, projects):
  finalGrade = 0;
  if exam > 50 and projects >= 2:
    finalGrade = 75;
  if exam > 75 and projects >= 5:
    finalGrade = 90;
  if exam > 90 or projects > 10:
    finalGrade = 100;
  return finalGrade;
      
#Пятое задание
def double_char(s):
    return "".join([c * 2 for c in s])
      
#Шестое задание

      
#Седьмое задание

      
#Восьмое задание

      
#Девятое задание


#Десятое задание
