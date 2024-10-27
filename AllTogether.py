### Part Four -- your code goes here.
import random

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
e = random.randint(1,100)
f = random.randint(1,100)
g = random.randint(1,100)
h = random.randint(1,100)
i = random.randint(1,100)
j = random.randint(1,100)

list = [a,b,c,d,e,f,g,h,i,j]

for number in list:
    even = number%2
    if even == 0:
        list.remove(number)
print(list)