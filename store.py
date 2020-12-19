"""Script to run the program.
"""

from final import Store, Product, User, Customer, Vendor, Admin, Cart
import time

class Shopping:
    def __init__(self):
        self.users = []
        #Admin that will exist in the database
        self.users.append(Admin("Bob123","bob@gmail.com","password"))
        #Vendors that will exist in the database
        target = Vendor("Target","target@gmail.com","targetpassword")
        self.users.append(target)
        self.users.append(Customer("Kanye","ye@gmail.com","West"))
        skyfood = Vendor("Sky7Food","skyfood@gmail.com","skyfood123")
        self.users.append(skyfood)
        #Kanye
        self.users.append(Customer("Kanye","ye@gmail.com","West"))
        #Products that will exist in the inventory
        self.inventory = []
        self.inventory.append(Product('Stapler', 10.99, 100, 'Target', 'A stapler to staple papers'))
        target.add_product('Stapler', 10.99, 100, 'A stapler to staple papers')
        self.inventory.append(Product('Apple', 2501, 3, 'Sky7Food', 'A yummy fruit'))
        skyfood.add_product('Apple', 2501, 3, 'A yummy fruit')
        #Current user
        self.current_user = None
        
    def make_space(self,lines, value):
        i = 0
        if value == "line":
            while i < lines:
                print("\n*******************************")
                i += 1
        elif value == "space":
            while i < lines:
                print("\n")
                i += 1
                        
    def welcome(self):
        self.make_space(1, "line")
        print("Welcome to your online store!\nYou can either register as a vendor" +
              " to start selling clothes, or as a buyer, to start shopping clothes from vendors.")
        self.make_space(1, "space")
        print("Please select one of the options below:")
        input_choice = input("Sign-in (type 'a')\nRegister (type 'b')\nVisit as a guest (type 'c')\nAction? ")
        if input_choice == "a":
            self.sign_in()
        elif input_choice == "b":
            self.register()
        elif input_choice == "c":
            time.sleep(1)
            self.home_page_customer()
    
    def sign_in(self):
        self.make_space(1, "line")
        username_valid = False
        password_valid = False
        while username_valid == False:
            input_username = input("Please type your username: \n")
            for user in self.users:
                if user.username == input_username:
                    username_valid = True
            if username_valid == False:
                print("Username invalid.\n")
        self.make_space(1, "space")
        while password_valid == False:
            input_password = input("Please type your password: \n")
            for user in self.users:
                if user.password == input_password:
                    self.current_user = user
                    password_valid = True
            if password_valid == False:
                print("Password invalid.\n")
        self.make_space(1, "line")
        print("You have successfully signed in.")
        time.sleep(1)
        if isinstance(self.current_user,Customer):
            self.home_page_customer()
        elif isinstance(self.current_user,Vendor):
            self.home_page_vendor()
        
    def register(self):
        self.make_space(1, "line")
        input_username = input("Username? ")
        input_email = input("Email? ")
        input_password = input("Password? ")
        input_type = input("Type of User? (Customer 'c', Vendor 'v') ")
        if input_type == "c":
            new_user = Customer(input_username, input_email, input_password)
            self.current_user = new_user
            self.users.append(new_user)
            self.make_space(1, "line")
            print("You have successfully registered as a Customer.")
            print(f"Your username: {input_username}, your email: {input_email}, your password: {input_password}.")
            time.sleep(2)
            self.home_page_customer()
        elif input_type == "v":
            new_user = Vendor(input_username,input_email,input_password)
            self.current_user = new_user
            self.users.append(new_user)
            self.make_space(1, "line")
            print("You have successfully registered as a Vendor.")
            print(f"Your username: {input_username}, your email: {input_email}, your password: {input_password}.")
            time.sleep(2)
            self.home_page_vendor()
        
    def home_page_customer(self):
        self.make_space(1, "line")
        print("You are in the home page.")
        self.make_space(1, "space")
        print("Please select one of the options below:")
        input_action = input("See my balance (type 'a')\nSee inventory (type 'b')\nSee my cart (type 'c')\nSign out (type 'd')\nAction? ")
        if input_action == 'a':
            self.see_balance()
        elif input_action == 'b':
            time.sleep(1)
            self.see_inventory()
        elif input_action == 'c':
            time.sleep(1)
            self.see_cart()
        elif input_action == 'd':
            self.make_space(1, "line")
            print("You have successfully signed out.")
            time.sleep(1)
            self.current_user = None
            self.welcome()
        
    def see_balance(self):
        if self.current_user == None:
            self.make_space(1, "line")
            print("You need to sign in.")
            time.sleep(1)
            self.home_page_customer()
        input_action = None
        while input_action != 'b':
            self.make_space(1, "line")
            print(f"Your balance is ${self.current_user.my_balance}.")
            self.make_space(1, "space")
            print("Options:")
            input_action = input("Add balance (type 'a')\nGo to home page (type 'b')\nAction? ")
            if input_action == 'a':
                input_amount = input("\nAmount to add:\n")
                self.current_user.add_balance(input_amount)
                time.sleep(1)
        self.home_page_customer()
        
    def see_inventory(self):
        self.make_space(1, "line")
        for product in self.inventory:
            print(f"Name: {product.name}   Price: ${product.price}   Vendor: {product.vendor}")
        self.make_space(1, "space")
        print("Options:")
        if self.current_user != None:
            input_action = input("Add a product to cart (type 'a')\nShow more product info (type 'b')\nGo to home page (type 'c')\nAction? ")
            if input_action == 'a':
                self.make_space(1, "space")
                input_name = input("What product do you to add to your cart?\nProduct name: ")
                self.add_product_to_cart(input_name)
                time.sleep(1)
                self.make_space(1, "line")
                print("Product successfully added to your cart.")
                time.sleep(1)
                self.see_inventory()
            elif input_action == 'b':
                time.sleep(1)
                self.see_expanded_inventory()
            elif input_action == 'c':
                time.sleep(1)
                self.home_page_customer()
        elif self.current_user == None:
            input_action = input("Show more product info (type 'a')\nGo to home page (type 'b')\nAction? ")
            if input_action == 'a':
                time.sleep(1)
                self.see_expanded_inventory()
            elif input_action == 'b':
                time.sleep(1)
                self.home_page_customer()
            
    def see_expanded_inventory(self):
        self.make_space(1, "line")
        for product in self.inventory:
            print(f"Name: {product.name} Price: ${product.price} Vendor: {product.vendor} Quantity Available: {product.quantity} Description: {product.description}")
        self.make_space(1, "space")
        print("Options:")
        self.make_space(1, "space")
        print("Options:")
        if self.current_user != None:
            input_action = input("Add a product to cart (type 'a')\nShow less product info (type 'b')\nGo to home page (type 'c')\nAction? ")
            if input_action == 'a':
                self.make_space(1, "space")
                input_name = input("What product do you to add to your cart?\nProduct name: ")
                self.add_product_to_cart(input_name)
                time.sleep(1)
                self.make_space(1, "line")
                print("Product successfully added to your cart.")
                time.sleep(1)
                self.see_expanded_inventory()
            elif input_action == 'b':
                time.sleep(1)
                self.see_inventory()
            elif input_action == 'c':
                time.sleep(1)
                self.home_page_customer()
        elif self.current_user == None:
            input_action = input("Show less product info (type 'a')\nGo to home page (type 'b')\nAction? ")
            if input_action == 'a':
                time.sleep(1)
                self.see_inventory()
            elif input_action == 'b':
                time.sleep(1)
                self.home_page_customer()
            
    def add_product_to_cart(self,item_name):
        for product in self.inventory:
            if product.name == item_name:
                self.current_user.my_cart.add_product(product)
            
    def see_cart(self):
        if self.current_user == None:
            self.make_space(1, "line")
            print("You need to sign in.")
            time.sleep(1)
            self.home_page_customer()
        self.make_space(1, "line")
        print("Products in my cart:")
        for product in self.current_user.my_cart.cart:
            print(f"Name: {product.name}   Price: {product.price}   Vendor: {product.vendor}")
        self.make_space(1, "space")
        self.current_user.my_cart.show_cost()
        self.make_space(1, "space")
        print("Options:")
        input_action = input("Show total cost in Euro (type 'a')\nCheckout cart (type 'b')\nGo to home page (type 'c')\nAction? ")
        if input_action == 'a':
            self.cart_in_different_currency()
        elif input_action == 'b':
            self.make_space(1, "line")
            print("This feature has not been implemented.")
            time.sleep(1)
            self.see_cart()
        elif input_action == 'c':
            time.sleep(1)
            self.home_page_customer()
            
    def cart_in_different_currency(self):
        self.make_space(1, "line")
        print("Products in my cart:")
        for product in self.current_user.my_cart.cart:
            print(f"Name: {product.name}   Price: {product.price}   Vendor: {product.vendor}")
        self.make_space(1, "space")
        self.current_user.my_cart.show_in_different_currency("Euro")
        self.make_space(1, "space")
        print("Options:")
        input_action = input("Show total cost in USD (type 'a')\nCheckout cart (type 'b')\nGo to home page (type 'c')\nAction? ")
        if input_action == 'a':
            self.see_cart()
        elif input_action == 'b':
            self.make_space(1, "line")
            print("This feature has not been implemented.")
            time.sleep(1)
            self.see_cart()
        elif input_action == 'c':
            time.sleep(1)
            self.home_page_customer()
        
    def home_page_vendor(self):
        self.make_space(1, "line")
        print("You are in the home page.")
        self.make_space(1, "space")
        print("Please select one of the options below:")
        input_action = input("See my products (type 'a')\nSee store inventory (type 'b')\nAction? ")
        if input_action == 'a':
            time.sleep(1)
            self.see_vendor_products()
        elif input_action == 'b':
            time.sleep(1)
            self.see_store_inventory()
            
    def see_vendor_products(self):
        self.make_space(1, "line")
        self.current_user.see_my_products()
        self.make_space(1, "space")
        print("Options:")
        input_action = input("Add a product (type 'a')\nGo to home page (type 'b')\nAction? ")
        if input_action == 'a':
            self.make_space(1, "line")
            print("Give details about your product:")
            input_name = input("Product name? ")
            input_price = input("Product price? ")
            input_quantity = input("Quantity available? ")
            input_description = input("Description? ")
            self.add_product(input_name,input_price,input_quantity,input_description)
            self.make_space(1, "line")
            print("Product successfully added to store inventory.")
            time.sleep(1)
            self.see_vendor_products()
        elif input_action == 'b':
            time.sleep(1)
            self.home_page_vendor()
    
    def see_store_inventory(self):
        self.make_space(1, "line")
        for product in self.inventory:
            print(f"Name: {product.name}   Price: {product.price}   Vendor: {product.vendor}")
        self.make_space(1, "space")
        print("Options:")
        input_action = input("Show more product info (type 'a')\nGo to home page (type 'b')\nAction? ")
        if input_action == 'a':
            time.sleep(1)
            self.see_expanded_store_inventory()
        elif input_action == 'b':
            time.sleep(1)
            self.home_page_vendor()
            
    def see_expanded_store_inventory(self):
        self.make_space(1, "line")
        for product in self.inventory:
            print(f"Name: {product.name} Price: {product.price} Vendor: {product.vendor} Quantity Available: {product.quantity} Description: {product.description}")
        self.make_space(1, "space")
        print("Options:")
        input_action = input("Show less product info (type 'a')\nGo to home page (type 'b')\nAction? ")
        if input_action == 'a':
            time.sleep(1)
            self.see_store_inventory()
        elif input_action == 'b':
            time.sleep(1)
            self.home_page_vendor()
            
    def add_product(self, item_name, item_price, item_quantity, description):
        self.inventory.append(Product(item_name,item_price,item_quantity,self.current_user.username,description))
        self.current_user.add_product(item_name,item_price,item_quantity,description)
        
def main():
    shopping_simulation = Shopping()
    shopping_simulation.welcome()
    
if __name__ == "__main__":
    main()
