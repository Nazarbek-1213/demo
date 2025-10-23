class Supermarket:
    def __init__(self, manzil, nom, tip, close_time, open_time):
        self.manzil = manzil
        self.nom = nom
        self.tip = tip
        self.close_time = close_time
        self.open_time = open_time

    def show(self):
        return f'manzil:{self.manzil}, name:{self.nom}, type:{self.tip}, close time:{self.close_time}, open time:{self.open_time}'


class Product:
    def __init__(self, pr_name, category, cost, all_prod):
        self.pr_name = pr_name
        self.category = category
        self.cost = int(cost)
        self.all_prod = int(all_prod)

    def show(self):
        return f'pr_name:{self.pr_name}, category:{self.category}, cost:{self.cost}, quantity:{self.all_prod}'


def add_pr(s: list):
    pr_name = input("product_name: ")
    category = input("category: ")
    cost = int(input("cost: "))
    all_product = int(input("quantity of all products: "))
    p1 = Product(pr_name, category, cost, all_product)
    s.append(p1)


def list_pr(s: list):
    if not s:
        print("No products found.")
        return
    for i, j in enumerate(s, start=1):
        print(f"{i}. {j.show()}")


def remove_pr(s: list):
    list_pr(s)
    a = int(input("number: "))
    if 1 <= a <= len(s):
        removed = s.pop(a - 1)
        print(f"Removed: {removed.pr_name}")
    else:
        print("xatolik")


def edit_pr(s: list):
    list_pr(s)
    a = int(input("which: "))
    if 1 <= a <= len(s):
        pr_name = input("new product_name: ")
        category = input("new category: ")
        cost = int(input("new cost: "))
        all_product = int(input("new quantity: "))
        s[a - 1] = Product(pr_name, category, cost, all_product)
        print("Product info updated!")
    else:
        print("Invalid number")


class Staff:
    def __init__(self, name, age, position, location, id, salary, password):
        self.name = name
        self.age = age
        self.position = position
        self.location = location
        self.id = id
        self.salary = salary
        self.password = password

    def show(self):
        return f'name:{self.name}, age:{self.age}, id:{self.id}, position:{self.position}, salary:{self.salary}, location:{self.location}'


def is_staff(staffs: list):
    while True:
        a = input("Enter the password: ")
        for i in staffs:
            if a == i.password:
                print(" Welcome, staff!")
                return True
        print(" Wrong password, try again!")


def manager_p(products: list, staffs: list):
    if not is_staff(staffs):
        return
    while True:
        a = input("\n1. Add product\n2. List products\n3. Remove product\n4. Edit info\n5. Exit\nChoose: ")
        if a == "1":
            add_pr(products)
        elif a == "2":
            list_pr(products)
        elif a == "3":
            remove_pr(products)
        elif a == "4":
            edit_pr(products)
        elif a == "5":
            break
        else:
            print("Invalid choice.")


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
        print("Basket is empty.")
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

        found = next((c for c in customers if c.id == choice), None)
        if not found:
            print(" No customer with that ID.")
            continue

        print(f"\n Welcome, {found.name}!")
        while True:
            print("\n1. Purchase\n2. View basket\n3. Delete basket\n4. Edit basket\n5. Payment\n6. Back")
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
                break
            else:
                print("Invalid input.")


# Example data
p = Product("melon", "fruit", 2000, 120)
p2 = Product("cola", "beverage", 15000, 150)
data = [p, p2]

person1 = Customer("Ahmad", 32, 1, 1_000_000)
person2 = Customer("Ahad", 28, 2, 50_000)
person3 = Customer("Dildora", 25, 3, 250_000)
persons = [person1, person2, person3]

staff1 = Staff("Ahad", 21, "seller", "Novza", 1, 20000000, "1234")
staffs = [staff1]


def main():
    while True:
        a = input("\n1. Staff mode\n2. Customer mode\n3. Exit\nChoose: ")
        if a == "1":
            manager_p(data, staffs)
        elif a == "2":
            manager_d(persons, data)
        elif a == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


main()
