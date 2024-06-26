import undetected_chromedriver
import time


try:
    driver = undetected_chromedriver.Chrome()

    # Задаємо розміри вікна браузера
    driver.set_window_size(1100, 600)

    driver.get("https://www.tiktok.com/ru-RU/")

    while True:
        try:
            j = int(input("> Введіть кількість лайків: "))
            time.sleep(10)
            if j <= 0:
                print("+----------------+")
                print("| Мінімум 1 лайк |")
                print("+----------------+")
                continue
            else:
                while j != 0:
                    # цикл
                    j -= 1
                    driver.execute_script("document.querySelector('button[data-e2e=\"arrow-right\"]').click()")
                    time.sleep(8)
                    driver.execute_script("document.querySelector('button.css-xakz2y-ButtonActionItem').click()")
                    time.sleep(2)
                    print("До кінця циклу залишилось: ", j)

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

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()