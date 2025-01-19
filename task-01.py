from queue import Queue
import random
import time

queue = Queue()


def generate_request():
    order_number = random.randint(1, 200)
    message = f"Ваша позиція у черзі {order_number}"
    queue.put(order_number)
    print(f"Створена заявка №{order_number}")
    # Створити нову заявку
    # Додати заявку до черги


def process_request():
    if not queue.empty():
        current_client = queue.get()
        print(f"Обслуговується клієнт з номером {current_client}")
    else:
        print("Черга пуста")
        # Якщо черга не пуста:
        #     Видалити заявку з черги
        #     Обробити заявку
        # Інакше:
        #     Вивести повідомлення, що черга пуста


def main():
    print("Запущена обробка заявок, для завершення натисність \"ctrl+c\"")
    try:
        while True:
            generate_request()
            time.sleep(1)
            process_request()
    except KeyboardInterrupt:
        print("\nОбробка заявок зупинена")
    # Головний цикл програми:
    #     Поки користувач не вийде з програми:
    #         Виконати generate_request() для створення нових заявок
    #         Виконати process_request() для обробки заявок


if __name__ == "__main__":
    main()
