"""INST326 Fall 2020 Team Project.
Iskander Lou, Amanda Murayama, Hudson Graves, Iman Du.
"""
class Store:
    """E-commerce store.
    Attributes:
        inventory: list of Products.
        list_of_users: list of Users, including vendors and admins.
    """
    def __init__(self):
        """Initializes the attributes, inventory and list_of_users and assigns them to empty lists.
        Args:
            self: object
        """
        self.inventory = []
        self.list_of_users = []   
        
    def find_product(self,item_name):
        for product in self.inventory:
            if product.name == item_name:
                return product
            
    def find_user(self,username):
        for user in list_of_users:
            if user.username == username:
                return user
            
class Product:
    """Creates a product  to be listed in the store with the vendor name, a description, and the price"""
    def __init__(self, name, price, quantity, vendor):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.vendor = vendor
        
    def increase_quantity(self,qt):
        self.quantity += qt
        
    def decrease_quantity(self,qt):
        self.quantity -= qt

class User:
    """Parent class for Admin, Vendor, and Customer."""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def look_at_inventory(self,store):
        for product in store.inventory:
            print(f"{product.name}: {product.price}$. {product.quantity} available in stock.\n")
        
class Customer(User):
    """Buy stuff."""
    def __init__(self):
        super().__init__(self)
        self.my_cart = Cart()
        self.my_balance = 0
        self.purchased_items = []
        
    def add_to_my_cart(self,product):
        self.my_cart.add_product(product)
        
    def remove_from_my_cart(self,product):
        self.my_cart.remove_product(product)
    
    def add_balance(self,quantity):
        self.my_balance += quantity
        
    def checkout_cart(self, store):
        self.my_cart.checkout(self)
        
    def show_my_purchased_items(self):
        for product in self.purchased_items:
            print(f"{product.name}\n")
    

class Vendor(User):
    """Sell stuff."""
    def __init__(self):
        super().__init__(self)
        self.my_products = []
        
    def add_product(self,store,item_name,item_price,item_quantity):
        product = Product(item_name,item_price,item_quantity,self)
        store.inventory.append(product)
        self.my_products.append(product)
        
    def remove_product(self,store,item_name):
        product = store.find_product(item_name)
        if product.vendor == self:
            store.inventory.remove(product)
            self.my_products.remove(product)
        else:
            print("You are not selling this product.")
            
    def see_my_products(self):
        for product in self.my_products:
            print(f"{product.name}: {product.price}$. {product.quantity} available in stock.\n")
        
class Admin(User):
    """Has the authority to edit inventory, add/remove vendors and customers, see their info."""
    def add_to_inventory(self,store,item_name,item_quantity,item_price):
        """Assuming the product is not in inventory."""
        product = Product(item_name,item_price,item_quantity,self)
        store.inventory.append(product)
            
    def take_from_inventory(self,store,item_name,quantity):
        """Assuming the product is in inventory and the requested quantity is available in stock."""
        product = store.find_product(item_name)
        product.decrease_quantity(quantity)
        
    def remove_from_inventory(self,store,item_name):
        product = store.find_product(item_name)
        store.inventory.remove(product)
            
    def add_new_user(self,store,user):
        store.list_of_users.append(user)
        
    def remove_user(self,store,user):
        store.list_of_users.remove(user)
        
    def get_list_of_users(self,store):
        for user in store.list_of_users:
            print(user.username + "\n")
            
    def get_user_info(self, board, username):
        for user in board.list_of_users:
            if user.username == username:
                print(f"Username: " + {username} + "\nEmail: " + {user.email} + "\nPassword: " + {user.password}) 
        
class Cart:
    """Calculate final checkout price of the order with the option to add or remove from cart and to add a discount code. """
    def __init__(self):
        self.cart = []
        self.discount = 0
        self.shipping = 0
        self.tax = 0
        
    def add_product(self,product):
        """"Adds products from shopping cart Returns: An updated shopping cart """
        self.cart.append(product)
    
    def remove_product(self,product):
        """"Removes products from shopping cart Returns: An updated shopping cart """
        self.cart.remove(product)
        
    def calculate_cost(self):
        """Determines the checkout price for the order by including the shipping cost and discount Args: discount codes, Shipping cost. Returns: Float of the final checkout price"""
        cost_of_products = 0
        for product in self.cart:
            cost_of_products += product.price * product.quantity
        total_cost_usd = cost_of_products + self.discount + self.shipping + self.tax
        return total_cost_usd
    
    def show_cost(self):
        cost = calculate_cost(self)
        print(f"Total checkout: ${cost}")
        
    def show_in_different_currency(self,currency):
        """Implement API here.
        Returns the final price of the item in the customer's currency. Args: Original Price, Final price in desired currency."""
        cost = calculate_cost(self)
        if currency == "Euro":
            cost = cost * 0.82
            print(f"Total checkout: €{cost}")
        else:
            print("Sorry, this currency is not available.")
            
    def checkout(self,customer, store):
        """Assuming the customer has enough balance."""
        customer.balance -= calculate_cost(self)
        for product in cart:
            customer.purchased_items.append(product)
            store.inventory.removed(product)
        self.cart = []
