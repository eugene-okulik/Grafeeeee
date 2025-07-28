person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
data = ['name', 'last_name', 'city', 'phone', 'country']
dictionary = dict(zip(person, data))
for key, value in dictionary.items():
    print(f'{key} = {value}')


# если же нужна была обычная распаковка, то код этот :
name, last_name, city, phone, country = person
print(name)
