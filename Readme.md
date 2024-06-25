
# Этот код преобразует столбец DataFrame в one-hot представление без использования функции get_dummies.
Импорт библиотек:

     import pandas as pd
   
     import random
   
## Генерация исходных данных:
Создаем список lst, который содержит 10 значений 'robot' и 10 значений 'human'.
Перемешиваем список с помощью random.shuffle.
Создаем DataFrame data с одним столбцом 'whoAmI'.

     lst = ['robot'] * 10
   
     lst += ['human'] * 10
   
     random.shuffle(lst)
   
     data = pd.DataFrame({'whoAmI': lst})
   
## Получение уникальных значений:

Используем метод unique для получения уникальных значений из столбца 'whoAmI'.

     unique_values = data['whoAmI'].unique()
   
## Создание one-hot представления:

Для каждого уникального значения создаем новый столбец.

Заполняем столбец 1, если значение в исходном столбце совпадает с уникальным значением, иначе 0.

     for value in unique_values:
   
         data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)
      
## Вывод первых строк DataFrame:
Выводим первые строки DataFrame с помощью метода head.
     print(data.head())

После выполнения кода, DataFrame будет иметь следующие столбцы: 'whoAmI', 'robot', 'human', где столбцы 'robot' и 'human' будут содержать one-hot представление.
