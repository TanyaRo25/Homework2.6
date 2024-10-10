my_dict = {'Николай': 1937, 'Галина': 1974,
           'Владимир': 1971, 'Ангелина': 2002, 'Татьяна': 1998}
print('Dictionary:', my_dict)
print('Existing value:', my_dict['Галина'])
print('Not existing value:', my_dict.get('Виктория'))
my_dict.update({'Сергей': 1995, 'Валерий': 2005})
removed_year = my_dict.pop('Валерий')
print('Deleted value:', removed_year)
print('Modified dictionary:', my_dict)

my_set = {32, 'avocado', 32, 'kiwi', False, 1, 98, False, 'avocado',
          'whiskey'}
print('Set:', my_set)
my_set1 = {32, 'avocado', 32, 'kiwi', False, 1, 98, False, 'avocado',
           'whiskey'}
my_set1.add(650.5)
my_set1.add('cheese')
my_set1.remove("avocado")
print('Modified set:', my_set1)
