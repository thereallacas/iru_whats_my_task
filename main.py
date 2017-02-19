# -*- coding: utf-8 -*-
x = raw_input('Add meg a neptunod: ')
accumulated = 0
for c in x:
	accumulated+=ord(c)
task = accumulated%4
feladatok=['A','B','C','D']
print "a megoldando feladat: %c" %feladatok[task]
