clemet = {'city':'Москва', 'temperature':'20'}

print(clemet['city'])

clemet['temperature']=int(clemet['temperature'])
clemet['temperature']-=5
print(clemet)


print(clemet.get('counry', 'Россия'))

clemet['date'] = "27.05.2019"

print(len(clemet))


'''
Создайте словарь:
{"city": "Москва", "temperature": "20"}
Выведите на экран значение ключа city
Уменьшите значение "temperature" на 5
Выведите на экран весь словарь

Проверьте, есть ли в словаре ключ country
Выведите значение по-умолчанию "Россия" для ключа country
Добавьте в словарь элемент date со значением "27.05.2019"
Выведите на экран длину словаря
'''