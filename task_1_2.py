def nice_cook_book(recipies):
    with open(recipies, encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
        return (cook_book)


nice_cook_book('recipies.txt')


def get_shop_list_by_dishes(dishes, persons):
    menu = nice_cook_book('recipies.txt')
    print('Наше меню выглядит вот так:')
    print(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'],\
                                    {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list.update(items_list)
        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        print(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос'], 1)