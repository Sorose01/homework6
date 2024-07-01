my_dict = {'Nastya': 2009, 'Iliya': 2012, 'Roma': 2013, 'Tanya': 2017}
print(my_dict)
print(my_dict.get('Roma'))
print(my_dict.get('Katya'))
my_dict.update({'Masha': 2015, 'Anton': 2011})
print(my_dict.pop('Nastya'))
print(my_dict)

my_set = {1,2,3,3,1,5,'я','ты','он','мы','ты','он','она'}
print(my_set)
my_set.add((4,'вы'))
my_set.discard(3)
print(my_set)


