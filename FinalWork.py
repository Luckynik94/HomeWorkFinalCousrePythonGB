import pandas as pd
import random

# Исходные данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений
unique_values = data['whoAmI'].unique()

# Создание one-hot представления
for value in unique_values:
    data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)

# Вывод первых строк DataFrame
print(data.head())