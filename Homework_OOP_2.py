from pprint import pprint
cook_book = {}
cook_book_ingredient = {}
cook_book_list = []

# Считываю данные из файла
filename = 'recipes.txt'
with open (filename, 'r') as f:
    file_lines = f.readlines()

# Формирую список отдельных рецептов
temp_list = []
file_lines_div = []
file_lines.append('\n')
for line in file_lines:
    if line != '\n':
        temp_list.append(line)
    else:
        file_lines_div.append(list(temp_list))
        temp_list = []
    continue

# Формирую кулинарную книгу
for k in file_lines_div:
    for i in range(int(k[1].rstrip('\n'))):
        ind = i + 2
        cook_book_ingredient['ingredient_name'] = k[ind].split('|')[0].rstrip(' ')
        cook_book_ingredient['quantity'] = int(k[ind].split('|')[1])
        cook_book_ingredient['measure'] = (k[ind].split('|')[2]).rstrip('\n').lstrip(' ')
        cook_book_list.append(dict(cook_book_ingredient))

    cook_book[k[0].rstrip('\n')] = cook_book_list
    cook_book_list = []

# Вывод на печать кулинарной книги
print('Кулинарная книга:')
pprint(cook_book)

# Функция, которая принимает на вход список блюд из cook_book и количество персон
def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for dish in dishes:
        for i in dish:
            dish_temp = {}
            dish_temp['measure'] = i['measure']
            # Проверка наличия продукта в списке
            if i['ingredient_name'] in dishes_dict:
                dish_temp['quantity'] = dishes_dict[i['ingredient_name']]['quantity'] + i['quantity'] * person_count
            else:
                dish_temp['quantity'] = i['quantity'] * person_count
            dishes_dict[i['ingredient_name']] = dish_temp
    return dishes_dict

# Сформированный список ингредиентов
print('\nСформированный список ингридиентов:')
pprint(get_shop_list_by_dishes([cook_book['Омлет'], cook_book['Фахитос']], 2))

