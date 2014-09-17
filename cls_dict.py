dict = {'jack':[15,'blonde'], 'bob':[22,'brown'], 'alice':[12,'black'],
'kevin':[17,'red']}
print(dict['jack'][1])
print(dict)
print(dict['jack'])
dict['tim'] = 14
print(dict)
dict['tim'] = 15
print(dict)
del dict['tim']
print(dict)

