import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
names2 = []
for i in range(4):
    names2.append(random.choice(names))
    print(names2)