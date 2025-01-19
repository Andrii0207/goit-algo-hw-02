from collections import deque
import re


def add_to_deque(value):

    match value:
        case int():
            print("Ви ввели число, введіть будь ласка рядок")
        case str() if len(value) == 1:
            print("Ви ввели занад то короткий рядок, введіть будь ласка коректні дані")
        case str() if len(value) > 1:
            purified_value = re.sub(r'[^a-zA-Zа-яА-Я]', '', value.lower())

    d = deque(purified_value)

    while len(d) > 1:
        first_simbol = d.popleft()
        last_simbol = d.pop()

        if first_simbol != last_simbol:
            print(f"{value} - не паліндром")
        else:
            print(f"{value} - паліндром")


add_to_deque(" ABBA  ")
add_to_deque(" Hello world")
add_to_deque("HelloWorld")
