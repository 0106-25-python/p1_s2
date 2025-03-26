# Часть 2. Создание новой задачи

Итоговый алгоритм работы программы:
- при запуске выводим список всех задач из базы данных
- ожидаем ввода новой задачи от пользователя в формате: _Описание задачи_ [_дата выполнения задачи_]
  - дата выполнения может быть не указана
- сохраняем новую задачу в базу и выводим обновлённый список задач


## Шаг 1. Обработка ввода информации
- обрабатываем ввод информации пользователем
- (промежуточно) выводим эту информацию в консоль в формате
```
Вы ввели: Купить молоко [25.03.2025]
```

### Что нам пригодится из возможностей Python

1) Функция для обработки ввода информации из консоли [input()]()
```python
test_string = input() #ожидаем ввода пользователя и записываем строковое значение в переменную
one_more_input = input("Введите любые символы: ") #выводим фразу, предшествующую вводу (как подсказка); ожидаем ввода пользователя и записываем строковое значение в переменную
```

## Шаг 2. Разбор введённой информации о задаче
- разбираем введённую пользователем информацию согласно правилам
- (промежуточно) выводим эту информацию в консоль в формате
```
Вы создаёте задачу с параметрами:
- Описание задачи: Задача 1
- Дата выполнения: [29.03.2025] или [не задана]
```

Договоримся, что:
- сначала пользователь вводит в любом формате описание задачи
- затем он может ввести или не вводить дату планового выполнения задачи. Информацию о дате необходим записать внутри квадратных скобок []

_Пример:_
- Купить молоко <- простая задача без даты выполнения
- Заказать подушку на WB [29.03.2025] <- задача с датой выполнения

### Что нам пригодится из возможностей Python

1) Встроенная функция подсчета длины объекта [len()](https://www.w3schools.com/python/ref_func_len.asp)
```python
test_string = "Это тестовая строка [да-да, она самая]"
string_len = len(test_string) #вернёт кол-во символов в строке

test_list = [1, 23, 4, "Test"]
list_len = len(test_list) #вернёт кол-во элементов в списке
```

2) Встроенная функция замены символов в строке [replace()](https://docs.python.org/3/library/stdtypes.html#str.replace)
```python
test_string = "Это тестовая строка [да-да, она самая]"
new_string = test_string.replace("да-да", "угу-угу") #заменяем одно на другое; в результате возвращается новая строка, т.е. исходная остаётся неизменной
```

3) Встроенная функция удаления лишних пробелов [strip()](https://docs.python.org/3/library/stdtypes.html#str.strip) в начале и конце строки
```python
test_string = "  Это тестовая строка [да-да, она самая]  "
print(test_string.strip()) #выведет строку без лишних пробелов
```

## Шаг 3. Подготовка информации о задаче к сохранению
- формирование уникального идентификатора
- фиксация времени создания задачи
- объединение всей информации в единую строку для сохранения в БД

### Что нам пригодится из возможностей Python

1) Модуль для работы с уникальными идентификаторами [UUID](https://docs.python.org/3/library/uuid.html#module-uuid)
```python
import uuid #импортируем модуль

new_id = uuid.uuid4() #генерируем новый уникальный идентификатор
```

2) Модуль для работы с датой [datetime](https://docs.python.org/3/library/datetime.html#module-datetime)
```python
import datetime #импортируем модуль
date = datetime.datetime.now() #получаем текущую дату и время
print(date) #выведет что-то типа 2025-02-23 07:51:17.181652 в зависимости от вашей локализации
```

3) Возможность подключения (импортирования) модуля с помощью [import](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
```python
import random #импортируем весь модуль
number_to_guess = random.randint(1, 20) #генерируем случайное число от 1  до 20

#можно импортировать конкретный атрибут
from random import randint
number_to_guess = randint(1, 20) #генерируем случайное число от 1  до 20

#можно задавать псевдоними. Например, если у вас в коде используется такое же имя функции
from random import randint as true_rand
number_to_guess = true_rand(1, 20) #генерируем случайное число от 1  до 20
```

## Шаг 4. Записываем информацию о новой задаче в БД
- Добавить новую запись в исходный файл БД
- Вывести в консоль обновлённый список задач с предложением ввода новой

### Что нам пригодится из возможностей Python

1) Функция [open()](https://docs.python.org/3/library/functions.html#open) с добавлением контента в файл
```python
new_content = "Ещё одна строка в файл\n"
file_object = open("db.txt", "a", encoding="utf8") #открываем файл на добавление контента - append
file_object.write(new_content)
file_object.close()
```
