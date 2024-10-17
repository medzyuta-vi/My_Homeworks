my_dict = {'Vasiliy' : 1992, 'Ray' : 1930, 'Irina' : 1969}
print(my_dict)
print(my_dict['Vasiliy'])
my_dict['Yulia'] = 2003
print(my_dict)
my_dict.update({'Rimma' : 1997, 'Kseniya' : 1999})
print(my_dict)
del my_dict['Ray']
print(my_dict.get('Ray'))
print(my_dict)

my_set = {'ghost', 1, 2, 3, 'ghost', 2}
print(my_set)
print(my_set.add('Hyper'))
print(my_set)
print(my_set.remove('ghost'))
print(my_set)