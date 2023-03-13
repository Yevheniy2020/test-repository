#Дано масив словників.
#Реалізувати пошук по ключах кожного словника і вивести кількість знайдених результатів на екран.

arr = [{'First': 'Apple', 'Second': True}, {2: "Third", 'First': 100}, {'First': False, 2: 'SSS'}]
print('Enter str')
str = input()
counter = 0
for element in   arr:
   if element.get(str):
       counter += 1
       print(element)

print(counter)