# Работа со словарями:
my_dict = {'Anton': 1992, 'Max': 1985, 'Alex': 1982, 'Anna': 1993}
print('Dict:', my_dict)
print('Existing value:', my_dict['Anton'])
my_dict['Lili'] = 1970
print('Not existing value:', my_dict['Lili'])
my_dict.update({'Nastya': 1989,
                'Vlad':  2010})
print('Deleted value:', my_dict['Max'] )
del(my_dict['Max'])
print('Modified dictionary:', my_dict)

# Работа с множествами:
my_set = {1, 2, 3, 'dog', 2, 3, 'cat', 1}
print('Set:', my_set)
my_set.add(5)
my_set.discard(1)
print('Modified set:', my_set)