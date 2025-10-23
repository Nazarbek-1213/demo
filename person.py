from product import list_pr



class Customer:
    def __init__(self, name, age, id, card):
        self.name = name
        self.age = age
        self.id = id
        self.basket = []
        self.card = card

    def show(self):
        return f'name:{self.name}, age:{self.age}, id:{self.id}, card balance:{self.card}'


def purchase(products: list):
    list_pr(products)
    a = int(input("Choose to buy (number): "))
    if a < 1 or a > len(products):
        print(" No such product.")
        return
    quantity = int(input("Quantity: "))
    product = products[a - 1]
    if product.all_prod < quantity:
        print(" Not enough in stock.")
        return
    product.all_prod -= quantity
    print(f" You added {quantity} x {product.pr_name} to basket.")
    return (product.pr_name, quantity, product.cost)


def view_basket(basket: list):
    if not basket:
        print("🛒 Basket is empty.")
        return
    print("Your basket:")
    for j, i in enumerate(basket, start=1):
        print(f"{j}. {i[0]} - {i[1]} pcs - {i[2]} sum each")


def delete_basket(basket: list):
    if not basket:
        print("🛒 Basket is empty.")
        return
    view_basket(basket)
    a = int(input("Which item to delete: "))
    if 1 <= a <= len(basket):
        removed = basket.pop(a - 1)
        print(f"🗑 Removed {removed[0]} from basket.")
    else:
        print(" Invalid number.")


def edit_basket(basket: list):
    if not basket:
        print(" Basket is empty.")
        return
    view_basket(basket)
    a = int(input("Which item to edit: "))
    if 1 <= a <= len(basket):
        new_quantity = int(input("New quantity: "))
        product_name, _, cost = basket[a - 1]
        basket[a - 1] = (product_name, new_quantity, cost)
        print("️ Basket updated.")
    else:
        print(" Invalid choice.")


def pay(basket: list, customer: Customer):
    if not basket:
        print(" Basket is empty.")
        return
    total = sum(q * c for _, q, c in basket)
    print(f" Total to pay: {total} sum")
    if customer.card < total:
        print(" Insufficient funds.")
    else:
        customer.card -= total
        basket.clear()
        print(f" Payment successful! Remaining balance: {customer.card} sum")


def manager_d(customers: list, products: list):
    while True:
        print("\n Customers list:")
        for c in customers:
            print(f"{c.id}. {c.name} (Balance: {c.card} sum)")
        print("0. Exit")
        choice = int(input("\nSelect customer by ID: "))

        if choice == 0:
            print(" Exiting program...")
            break

        found = None
        for c in customers:
            if c.id == choice:
                found = c
                break

        if not found:
            print(" No customer with that ID.")
            continue

        print(f"\n Welcome, {found.name}!")
        while True:
            print("\n1. Purchase\n2. View basket\n3. Delete basket\n4. Edit basket\n5. Payment\n6. Back to customers menu")
            a = input("Choose: ")
            if a == "1":
                item = purchase(products)
                if item:
                    found.basket.append(item)
            elif a == "2":
                view_basket(found.basket)
            elif a == "3":
                delete_basket(found.basket)
            elif a == "4":
                edit_basket(found.basket)
            elif a == "5":
                pay(found.basket, found)
            elif a == "6":
                print(f" Returning to customer list...")
                break
            else:
                print("Invalid input.")


# Example customers
person1 = Customer("Ahmad", 32, 1, 1_000_000)
person2 = Customer("Ahad", 28, 2, 50_000)
person3 = Customer("Dildora", 25, 3, 250_000)

persons = [person1, person2, person3]



