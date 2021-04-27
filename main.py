#!/usr/bin/python3
def calc(x,y,op):
  try:
    x, y = int(x), int(y)
    return{
      '+': x + y,
      '-': x - y,
      '*': x * y,
      '/': x // y,
      '%': x % y,
    }.get(op)
  except:
    raise


print(calc(5,2,'+'))
print(calc(5,2,'-'))
print(calc(5,2,'*'))
print(calc(5,2,'/'))
print(calc(5,2,'%'))
print(calc(5,2, 'a'))
print(calc(5,2, '**'))
