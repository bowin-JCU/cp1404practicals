number_of_items = int(input("Number of items: "))
total_price = 0

for i in range(number_of_items):
    price = float(input(f"Enter the price of item {i + 1}: $"))
    total_price += price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount
    print(f"Discount is ${discount:.2f}")

print(f"Total price is ${total_price:.2f}")