#Задание 1 
print (type(15 * 3))
print (type(15 / 3))
print (type(15 // 2))
print (type(15 ** 2))

#Задание 2
weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
weather_obr = []

for i in weather:
  if i.isdigit() and i != '17':
    i = '0' + i
    weather_obr.append(i)
    
  elif '+' in i:
    for s in i:
      if s.isdigit():
        s = '+' + '0' + s
        weather_obr.append(s)
 
  else:
    weather_obr.append(i)




print (' '.join(weather_obr))

#Задание 4
empl = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in empl:
  i = i.split(' ')
  print (f'Привет, {i[-1].capitalize()}!')



#Задание 5
price = [56.05, 67.4, 22.50, 103.94, 265.30, 67.08, 27.56, 76.30, 100.01, 1000.5, 13.95 ]
price_list = [] #Сформированный пакет цен
price_rating = []#Обработанные цены

for i in price:
  b = 0
  i=str(i).split('.')
  if len(i[-1]) < 2:
    i[-1] = i[-1] + '0'
    price_rating.append('.'.join(i))
  else:
    i[-1] = i[-1]
    price_rating.append('.'.join(i))
  
for c in price_rating:
  c = str(c).split('.')
  c[0] += ' руб'
  c[-1] += ' коп' 
  c = ' '.join(c)
  price_list.append(c)

print ('Актуальные цены: ' + ', '. join(price_list))


print ('\n')
print(f'Оргинальный список: {price}')
print (f'ID оригинального списка: {id(price)}')

price.sort()
print(f'Отсортированный список (по возрастанию): {price}')
print (f'ID отсортированного списка: {id(price)}\n')

price = [56.05, 67.4, 22.50, 103.94, 265.30, 67.08, 27.56, 76.30, 100.0, 1000.5, 13.95 ]

print ('\n')
print(f'Оргинальный список (не отсортированный): {price}')
print (f'ID оригинального списка: {id(price)}')

price_s = sorted(price, reverse = True)
print(f'Отсортированный список (по убыванию): {price_s}')
print (f'ID отсортированного списка: {id(price_s)}')
print ('\n')

print (f'Самые дорогие товары: {price_s[0:4]} ')
