my_dict = {"tuple": (1, 2, 3, 4, 5), "list": [1, 2, 3, 4, 5],
           "dict": {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'},
           "set": {1, 2, 3, 4, 5}}

print(my_dict["tuple"][-1])
my_dict["list"].append(6)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = (1,)
del my_dict['dict'][2]
my_dict['set'].add(17)
my_dict['set'].remove(17)
print(my_dict)
