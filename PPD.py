from C import find_c
import random


def pseudo_random(max_try, retry):
    c0 = find_c(max_try)
    print("Константа 'c' для данного шанса составляет:",c0)
    c = c0
    now_retry = 1
    success_try = 0
    for i in range(retry):
        random_number = random.uniform(0, 1)
        print("-------------------------------")
        print("YEEES or no?...")
        if random_number <= c:
            print("YEEES")
            c = c0
            now_retry = 1
            success_try += 1
            print("-------------------------------")
        else:
            print("no...")
            c += c0
            now_retry += 1
            print(f"Попыток до гаранта: {(max_try-now_retry)+1}")
            print("-------------------------------")
    win_rate = success_try / retry
    return(success_try, win_rate)
s = 1
while s == 1:
    s = 1
    n = int(input("Введите максимальное количество попыток для гарантированного срабатывания:"))
    if n <= 0:
        print("Количество попыток до гаранта должно быть больше нуля")
    retry = int(input("Введите количество повторений:"))
    if retry <= 0:
        print("Количество попыток должно быть больше нуля")
    else:
        s = pseudo_random(n, 100)
        print("Количество удачных попыток:", s[0])
        print("Средний шанс на победу:", s[1])
    s = int(input("Нажмите 1 чтобы начать заново или 0 чтобы закончить программу:"))