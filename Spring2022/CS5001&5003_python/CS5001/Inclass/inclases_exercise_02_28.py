"""
if we were to delete an element from a list
do we rearrage the automatically or do

"""

from curses.ascii import isdigit


word = "ABCD"

print(word.rjust(10, "*"))
print(word.rjust(5))

l1 = [1, 3.14, True, 'Hello']
l1[1] = False
for x in l1:
    print(x * 5)

l2 = (2, 4)

l2 = l2
print(l2)
l2 = l2 + l2
l3 = (3,3)

print(l2)

s = '   abcdde   '
print(s.strip())


print('12'.isdigit())


a = '  abcdef'
print(len(a))

"""fname = "myfile.txt"
f = open(fname, "a")

f.write('data')
# f.write('compute\n')
# f.write('process\n')
f = open(fname, 'r')
for line in f:
    print(line.strip())
"""

my_sentence = "The big red dog jumped over the red fox."
x = my_sentence.split()


print(" ".join(x))

word = ['a','d']

word.append('e')

print(word)

tup1 = (1, 2, 3)
tup1 = tup1 + tup1
print(tup1)
