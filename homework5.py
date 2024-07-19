# homework.py
immutable_var = 1, "one", True, 1.5 # кортеж с неизменяемыми элементами
print(immutable_var)
#immutable_var[2] = False
#print(immutable_var)
mutable_list = ([1, "one", True, 1.5]) # кортеж с изменяемыми элементами
mutable_list[2] = False
mutable_list[0] = 1.5
mutable_list[1] = 'too'
mutable_list[3] = 3.1
mutable_list = mutable_list + ['play']
mutable_list[4] = 'pause'
print(mutable_list)
