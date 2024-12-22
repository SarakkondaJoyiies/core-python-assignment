def add_item(menu, item):
    if item not in menu:
        menu.append(item)
        print(f"{item} is successfully added to the menu.")
    else:
        print(f"{item} is already in the menu.")
    return menu

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        print(f"{item} has been removed from the menu.")
    else:
        print(f"{item} is not in the menu.")
    return menu

def check_item(menu, item):
    if item in menu:
        return f"{item} is available."
    else:
        return f"{item} is not available."

start_menu = ["Pizza", "Burger", "Pasta", "Salad"]
new_item = "Tacos"  
item_to_remove = "Salad"
item_to_check = "Pizza"  

updated_menu = add_item(start_menu, new_item)
updated_menu = remove_item(updated_menu, item_to_remove)
availability = check_item(updated_menu, item_to_check)

print("Updated menu:", updated_menu)
print("Availability:", availability)
