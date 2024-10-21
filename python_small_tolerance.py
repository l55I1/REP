import math
import random

nb_simulation = int(math.pow(10, 2))
print("python    ", end="")

for t in range(10, 21):
    tolerance = math.pow(10, -t)
    nb_correct = 0

    for i in range(nb_simulation):
        x = random.random()
        y = random.random()
        z = random.random()
        if abs(((x + y) + z) - (x + (y + z))) < tolerance:
            nb_correct += 1

    print(f"{(nb_correct / nb_simulation * 100):.2f}%".rjust(10), end="")