a = '32.05.2006'

d, m, y = map(int, a.split('.'))

if d > 31:
    print('Ошибка ввода')
    

print(d, m, y, int('00'))