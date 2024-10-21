import math
import random

nb_simulation = int(math.pow(10, 6))
nb_correct = 0

for i in range(nb_simulation):
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    z = random.uniform(0, 10)
    if (x + y) + z == x + (y + z):
        nb_correct += 1

print(f'{(nb_correct / nb_simulation * 100):.2f}% accuracy for python')
