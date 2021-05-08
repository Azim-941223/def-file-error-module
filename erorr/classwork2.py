# 2

num = set()

for i in range(5):
    try:
        num1 = int(input("Введите число: "))
        num.add(num1)
        if num1 == 0:
            print("Введите натуральное число")
        if num1 < 0:
            print("Отрицательные числа нельзя вводить")
    except ValueError:
        print("Введите число")

print("Самое маленькое число: ", min(num))