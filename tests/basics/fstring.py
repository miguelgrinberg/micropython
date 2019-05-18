# functionality test for PEP-498 f-strings

name = 'foo'
name2 = 'bar'
number = 123
number2 = 123.45

print(f'{name}')
print(f'{number}')
print(f'{number2}')
print(f'abc{name}')
print(f'{name}abc')
print(f'abc {name}')
print(f'{name} abc')
print(f'1{name}2{number}3{number2}4')
print(f' 1 {name} 2{number} 3{number2}4 ')
print(f'{name}{number}{number2}')
print(f'{name}' f'{number}' f'{number2}')
print('1' f'{name}' '2' f'{number}' '3' f'{number2}' '4')

print(f'{name }')
print(f'{ name}')
print(f'{ name }')
print(f'{   name   }')
print(f'{name + name2}')

# more tests needed!