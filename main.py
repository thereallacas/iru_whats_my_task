# -*- coding: utf-8 -*-
x = raw_input('Add meg a neptunod: ')
accumulated = 0
for c in x:
	accumulated+=ord(c)
task = accumulated%4
print "a megoldando feladat: %d" %task
