def pirate_ship(capacity, items):
    items.sort(key=lambda x: x[2] / x[1], reverse=True)

    total_value = 0
    loaded_items = []

    for name, weight, value in items:
        if weight <= capacity:
            total_value += value
            capacity -= weight
            loaded_items.append((name, weight, value))
        else:
            fraction = capacity / weight
            total_value += fraction * value
            loaded_items.append((name, round(fraction * weight, 2), round(fraction * value, 2)))
            break
    print("Общая стоимость загруженных грузов:", total_value)
    print("Список загруженных грузов:")
    for item in loaded_items:
        print(f"{item[0]} {item[1]} {item[2]}")

