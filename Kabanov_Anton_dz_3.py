from random import randrange
#Задание 1
def num_translate(a):
  dict_splin = {'zero': 'ноль',
         'one': 'один',
         'two': 'два',
         'three': 'три',
         'four': 'четыре',
         'five': 'пять',
         'six': 'шесть',
         'seven': 'семь',
         'eight': 'восемь',
         'nine': 'девять',
         'ten': 'десять'
        }
  print (dict_splin.get(a))


num_translate(a = input('Введи цифру:\n'))


#Задание 3 
names = {}
def thesaurus(*args):
  """Создает и добавляет новые имена в словарь names, принтует отсортированный список"""
  for i in args:
    if names.get(i[0].upper()) is None:
      names.setdefault(i[0].upper(), [i.title()])
    else:
      names[i[0].upper()].append(i.title())
  print (f'{names} \n')
  

def sort_names():
  """Сортирует список names"""
  print('Отсортированный список имен:')
  for k in sorted(names):
    print (f'{k}: {names[k]}')
  


#Вызываем функию пуляем в неё данные:
thesaurus("Иван", "Мария", "Петр", "Илья", "Игнатий", "Гендальф", "Фродо", "Арагорн", "арагог", "феофан", "Гертруда", "Геродот")

#Сортируем список
sort_names()


#Задание 5

def get_jokes(x, b):
  """Принимает 2 параметра: кол-во шуток/с повторами/без повторов"""
    if x > 125:
        return print('Слишком много шуток! Давай поменьше!')
    elif x <= 0:
        return print('Слишком мало шуток! Давай побольше!')
    # Шутки без повторов
    elif b == 'y':                  
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]  # что
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]  # Когда
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]  # Какой
        # собираем первую шутку
        jokes_sq = []
        x -= 1

        while x >= 0:
            a = len(nouns)
            if a > 1:
                #
                joke = [nouns[randrange(0, a)], adverbs[randrange(0, a)], adjectives[randrange(0, a)]]
                jokes_sq.append(joke)

                nouns.remove(joke[0])
                adverbs.remove(joke[1])
                adjectives.remove(joke[2])
                x -= 1

            elif a == 1:

                joke = [nouns[0], adverbs[0], adjectives[0]]
                jokes_sq.append(joke)

                nouns.remove(joke[0])
                adverbs.remove(joke[1])
                adjectives.remove(joke[2])

                x -= 1
            else:
                break

        mappet_joke = list(map(lambda j: ' '.join(j), jokes_sq))
        return print(mappet_joke)
    # Шутки с повторами
    elif b == 'n': 

        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]  # что
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]  # Когда
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]  # Какой

        jokes_sq = []
        x -= 1
        while x >= 0:
            joke = [nouns[randrange(0, 5)], adverbs[randrange(0, 5)], adjectives[randrange(0, 5)]]
            jokes_sq.append(joke)
            x -= 1

        mappet_joke = list(map(lambda j: ' '.join(j), jokes_sq))
        return print(mappet_joke)# # Tc#




get_jokes(x=10, b='y')  # x = колво шуток// b - (y - шутки без повторов n - шутки с повторами)
