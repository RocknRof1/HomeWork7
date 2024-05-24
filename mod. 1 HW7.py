my_dict = ({'Andrey': 1990, 'Sofa': 2017, 'Anna': 1991, 'Sveta': 1967})
my_dict['Alena'] = 2001
print(my_dict['Sofa'])
print(my_dict['Alena'])
my_dict['Anton'] = 1986
my_dict['Max'] = 2006
del my_dict['Anna']
print(my_dict)

my_set = {12, True, 'Sofa', 5.5, 12, True, 'Sofa', 5.5}
print(my_set)
list_ = [1, 1, 5, 7, 7, 4, 2, 3, 4]
list_ = set(list_)
print(list_)
print(list_.add('Andrey'))
print(list_.add(9))
print(list_.remove(3))
print(list_)



