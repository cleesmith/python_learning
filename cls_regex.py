import re

# see:
# http://pythonprogramming.net/regular-expressions-regex-tutorial-python-3/

xs = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather Oscar, is 102.
'''
ages = re.findall(r'\d{1,3}', xs)
names = re.findall(r'[A-Z][a-z]*', xs)
print(ages)
print(names)

