import os
import random

run = ['1','2','3','4','5','6','7','8','9','10']
inner = []
path = "//home//azim//Рабочий стол//python"
while len(inner) != 5:
    ran = random.choice(run)
    if ran not in inner:
        inner.append(ran)
        file = open(f"{path}//{inner}.py", "w")
    print(inner)