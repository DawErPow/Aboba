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
def smash(words):
    return " ".join(words) if len(words) >= 1 else ""
      
#Седьмое задание
geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}

def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
      
#Восьмое задание
def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []
      
#Девятое задание
def maps(a):
    return [2 * x for x in a]

#Десятое задание
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'
