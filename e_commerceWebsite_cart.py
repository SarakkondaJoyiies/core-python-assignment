def total_price_calculation(cart):
    if not cart:
        return 0
    
    total_price = sum(cart.values())
    if len(cart) > 5:
        total_price *= 0.9  
    return total_price

cart = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
price=total_price_calculation(cart)
if price==0:
    print("Cart is empty")
else:
    print(f"Total price: ${price:.2f}")
