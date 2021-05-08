values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
a = []
for i in values:
    try:
        if set(i):
            a.append(True)
    except Exception:
        a.append(False)

b = all(a)
if b:
    print("Можно")
else:
    print("Нельзя")