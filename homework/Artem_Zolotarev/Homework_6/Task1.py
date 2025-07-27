text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,'
        ' facilisis vitae semper at, dignissim vitae libero')

text = text.split(' ')
lst = []
for x in text:
    for var in x.split(' '):
        if var.endswith('.'):
            lst.append(var[:-1] + 'ing.')
        elif var.endswith(','):
            lst.append(var[:-1] + 'ing,')
        else:
            lst.append(var[:] + 'ing')

print(' '.join(lst))
