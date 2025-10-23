from staff import str1
class Product:

    def __init__(self,pr_name,category,cost,all_prod):
        self.pr_name=pr_name
        self.category=category
        self.cost=cost
        self.all_prod=all_prod

    def show(self):
        return f'pr_name:{self.pr_name},category:{self.category},cost:{self.cost} quantity:{self.all_prod}'
def add_pr(s:list):
    pr_name=input("product_name: ")
    category=input("category: ")
    cost=input("cost: ")
    all_product=input("quantity of all products: ")
    p1=Product(pr_name,category,cost,all_product)
    s.append(p1)
def list_pr(s: list):
    if not s:
        print("No products found.")
        return
    for i, j in enumerate(s, start=1):
        print(f"{i}. {j.show()}")  # u
def remove_pr(s:list):
    list_pr(s)
    a=int(input("number: "))
    if a<1 or a>len(s):
        print("xatolik")
    else:
        removed=s.pop(a-1)
        return (removed)
def edit_pr(s:list):
        list_pr(s)
        a=int(input("which: "))
        pr_name = input("product_name: ")
        category = input("category: ")
        cost = input("cost: ")
        all_product = input("quantity of all products: ")
        q = Product(pr_name, category, cost, all_product)
        s[a-1]=q

def is_staff(s: list):
            while True:
                a = input("enter the pasword: ")
                for i in s:
                    if a == i.password:
                        print("welcome")
                        break
                    else:
                        print("try again")


def manager_p(s:list):

    while True:
        is_staff(str1)

        a=input(" 1.add product \n 2.list product \n 3.remove product \n 4.edit info \n 5.choose: ")
        if a=="1":
            add_pr(s)
        elif a=="2":
            list_pr(s)
        elif a=="3":
            remove_pr(s)
        elif a=="4":
            edit_pr(s)
        else:
            break
p=Product("melon","fruit",2000,120)
p2=Product("cola","beverage",15000,150)
data=[p,p2]









