colors = ['g','b','r']
try:
  color = input('color? ')
  print(colors.index(color))
# python2 ... except Exception, e:
except Exception as e:
  print(e)

if color in colors:
  print('color found')
else:
  print('color not found')
