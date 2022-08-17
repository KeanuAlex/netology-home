import os


def recipes(file):
    cook_book = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


def create_combined_list(directory):
    file_list = os.listdir(directory)
    combined_list = []

    for file in file_list:
        with open(directory + "/" + file, encoding='UTF8') as cur_file:
            combined_list.append([file, 0, []])
            for line in cur_file:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[2], reverse=True)


def create_file_from_directory(directory, filename):
    with open(filename + '.txt', 'w+', encoding='UTF8') as newfile:
        for file in create_combined_list(directory):
            newfile.write(f'{file[0]}\n')
            newfile.write(f'{file[1]} \n')
            for string in file[2]:
                newfile.write(string + '\n')


file = 'files/recipes.txt'
cook_book = recipes(file)
print(cook_book)
print('-' * 10)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
create_file_from_directory('files\sorted', 'files\Recipes')
