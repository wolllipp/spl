store = {
    "Кольцо": ["Золото 585", 5000, 10],
    "Серьги": ["Серебро 925", 2500, 15],
    "Браслет": ["Золото 750", 12000, 5],
    "Цепочка": ["Платина", 20000, 3]
}

cart = []

while True:
    print("\n--- Ювелирный магазин ---")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню (1-6): ")

    if choice == "1":
        print("=== ОПИСАНИЕ ===")
        for item, data in store.items():
            print(f"{item} - {data[0]}")

    elif choice == "2":
        print("=== ЦЕНА ===")
        for item, data in store.items():
            print(f"{item} – {data[1]} руб.")

    elif choice == "3":
        print("=== КОЛИЧЕСТВО ===")
        for item, data in store.items():
            print(f"{item} – {data[2]} шт.")

    elif choice == "4":
        print("=== ВСЯ ИНФОРМАЦИЯ ===")
        for item, data in store.items():
             print(f"{item}: состав – {data[0]}, цена – {data[1]} руб., количество – {data[2]} шт.")

    elif choice == "5":
        while True:
            name = input("\nВведите название изделия (или 'n' для выхода): ")
            if name.lower() == "n":
                break
            if name not in store:
                print("Такого изделия нет в магазине.")
                continue

            qty = int(input("Введите количество: "))

            if qty > store[name][2]:
                print("Столько нет в наличии!")
                continue

            store[name][2] -= qty

            cart.append((name, qty, store[name][1] * qty))
            print(f"Вы купили {qty} шт. '{name}' на сумму {store[name][1] * qty} руб.")

            if cart:
                print("\n--- Чек ---")
                total = 0
                for item, qty, cost in cart:
                    print(f"{item} – {qty} шт. – {cost} руб.")

                    total += cost


                print(f"Итого к оплате: {total} руб.")
                print("--- Спасибо за покупку! ---")

    elif choice == "6":
        print("До свидания!")
        break

    else:
        print("Неверный пункт меню, попробуйте снова.")
