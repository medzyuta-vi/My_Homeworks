immutable_var = 1, 2, 3, 'frog', True
print(immutable_var)
print(immutable_var[3])
immutable_var[3] = 'fish' #Кортеж относится к неизменяемым типам данных.
print(immutable_var)

mutable_list = ['coffe', 'tea', 'Soda']
print(mutable_list)
mutable_list[0] = 'black coffe'
print(mutable_list)