import re

patter = re.compile("this")
string = 'search inside of this text please'

a = patter.search(string)
print(a.group())

