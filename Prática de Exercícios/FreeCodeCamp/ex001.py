my_str = 'hello'
my_str2 = 'WORLD'
my_str3 = 'Hello World'
my_str_plus = my_str + ' ' + my_str2
age = 25
print((my_str_plus + ' ' + str(age) + ' ') * 3)
print(len(str(age)))
print(len(my_str_plus))
print(f'My name is {my_str} and my last name is {my_str2}. I am {age} years old')
print(my_str[::-1])
print(my_str.upper())
print(my_str2.lower())
print(my_str.strip())
print(my_str.replace('h', 'H'))
print(my_str3.split())
print(' '.join(['ant' + 'ônio' + ' '] * 5))
print(my_str.startswith('world'))
print(my_str3.isupper())
print(my_str[-3:])