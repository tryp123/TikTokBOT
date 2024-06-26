import undetected_chromedriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import random

with open('mem.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    comment_massive = [line.strip() for line in lines]

def automate_comments(comment_massive, driver):
    try:
        # Знаходимо поле для введення коментаря
        comment_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.css-qpucp9-DivInputEditorContainer.e1rzzhjk3 div[role="textbox"]')))

        comment_text = random.choice(comment_massive)
        print("Коментар:", comment_text, "Опубліковано!\n")

        # Вставляємо текст у поле коментаря
        comment_input.send_keys(comment_text)

        # Натискаємо на кнопку "Опублікувати"
        publish_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-e2e="comment-post"]'))
        )
        publish_button.click()

        print('Коментар успішно опублікований.')
    except Exception as e:
        print(f'Виникла помилка: {e}')

try:
    driver = undetected_chromedriver.Chrome()

    # Задаємо розміри вікна браузера
    driver.set_window_size(1100, 600)

    driver.get("https://www.tiktok.com/ru-RU/")
    file_path = 'mem.txt'

    while True:
        try:
            j = int(input("> Введіть кількість бажаних коментарів: "))
            time.sleep(10)
            if j <= 0:
                print("+--------------------+")
                print("| Мінімум 1 коментар |")
                print("+--------------------+")
                continue
            else:
                while j != 0:
                    # цикл
                    j -= 1
                    driver.execute_script("document.querySelector('button[data-e2e=\"arrow-right\"]').click()")
                    time.sleep(3)
                    automate_comments(comment_massive, driver)
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