# homework.py
my_dict = {'Vadim':1987, 'Kirill':1998, 'Zahar':2005}
print('Dict:',my_dict)
print('Existing value:',my_dict['Vadim'])
print('Not existing value:',my_dict.get('Ivan'))
my_dict.update({'Irina':1997,'Dasha':2005})
my_dict.pop('Zahar')
print('Modified dictionary:',my_dict)
my_set = {1, 2, 1, 2, 5, 3, 4, 6, 6, 5, 'apple', 'apple'}
print('Set:',my_set)
my_set.update({(1, 2, 3), 4.5})
my_set.discard('apple')
print('Modified set:',my_set)