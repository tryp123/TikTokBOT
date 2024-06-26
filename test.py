while True:
    try:
        j = int(input("> Введіть кількість бажаних коментарів: "))
        if j <= 0:
            print("+--------------------+")
            print("| Мінімум 1 коментар |")
            print("+--------------------+")
            continue
        else:
            while j != 0:
                # цикл
                print("> Жопа") 
                j -= 1

        continue_work = input("> Бажаєте продовжити? (y/n): ")
        if continue_work.lower() == 'n':
            print("+-------------------+")
            print("| Роботу завершено. |")
            print("+-------------------+")
            break
    except ValueError:
        print("+---------------------------------+")
        print("| Будь ласка, введіть ціле число. |")
        print("+---------------------------------+")
        continue
