word = input("Введите первое слово ")
word_2 = input("Введите второе слово ")


if len(word) == len(word_2):
    flag = True
    for char in word:
        if char not in word_2:
            flag = False
            break
    if flag:
        print(True)
    else:
        print(False)
else:
    print(False)