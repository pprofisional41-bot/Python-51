while True:
    numbers = input("Введите число знак число: ")
    parts = numbers
    if len(parts) != 3:
        print("Вы вввели не допустимый формат строки!")
    else:
        num_1 = int(parts[0])
        sign = (parts[1])
        num_2 = int(parts[2])
        if sign == "+":
            result = num_1 + num_2
            print(f"{num_1} + {num_2} = {result}")
        elif sign == "-":
            result = num_1 - num_2
            print(f"{num_1} - {num_2} = {result}")
        elif sign == "*":
            result = num_1 * num_2
            print(f"{num_1} * {num_2} = {result}")
        elif sign == "/":
            result = num_1 / num_2
            if num_1 == 0:
                print("Делить на 0 нельзя!")
            else:
                print(f"{num_1} / {num_2} = {result}")
        elif sign == "^":
            result = num_1 ^ num_2
            print(f"{num_1} ^ {num_2} = {result}")









