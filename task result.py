price = 0
tickets = int(input("Введите количество билетов:"))
for age in range(tickets):
    age = int(input("Введите возраст:"))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    elif age >= 25:
        price += 1390
if tickets > 3:
    price -= price/100*10
print("Полная стоимость билетов:", price)
