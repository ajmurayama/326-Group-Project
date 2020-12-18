

"""INST326 Fall 2020 Team Project.
Iskander Lou, Amanda Murayama, Hudson Graves, Iman Durrani.
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
        """Finds the specific item in the inventory of products
        Args:
            self: object
            item_name : name of the item that is trying to be found.
        Returns:
            the product that is being looked for
        """
        for product in self.inventory:
            if product.name == item_name:
                return product
            
    def find_user(self,username):
        """Searches for the usernames in the list
        Args:
            self: object
            username: the name of the user
        Returns:
            the username of the user
        """
        for user in self.ist_of_users:
            if user.username == username:
                return user
            
class Product:
    """Creates a product  to be listed in the store with the vendor name, a description, and the price"""
    def __init__(self, name, price, quantity, vendor, description):
        """Initializes attributes which are name, price, quantity, and vendor
        Args:
            self: object
            name: name of the product
            price: price of the product
            quantity: quantity of the product
            vendor: vendor name
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.vendor = vendor
        self.description = description
        
    def change_quantity(self, val=positive, qt):
        """Adds or removes to the amount of products to the cart, with the default being set to positive. 
        Args:
            qt: current quantity of the products
        """
        if val == "negative":
            self.quantity -= qt
        else:
            self.quantity += qt

class User:
    """Parent class for Admin, Vendor, and Customer.
    Attributes:
        username(str): username of the user.
        email(str): email of the user.
        password(str): password of the user.
    """
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def look_at_inventory(self,store):
        """Searches through the inventory of products to determine the price and quantity
        and to determine whether the product is in stock or not.
        Args:
            store(Store object): the name of store that contains the products.
        Returns:
            the product name, price, quantity and whether it's in stock or not.
        """
        for product in store.inventory:
            print(f"{product.name}: {product.price}$. {product.quantity}
            available in stock.\n")
        
class Customer(User):
    """Subclass of User. Buys products in this store.
    Attributes:
        my_cart(Cart object): personal shopping cart of the customer.
        my_balance(int): customer's balance with which they pay for products.
        purchased_items(list of Product objects): a list of products that have been purchased by the customer.
    """
    def __init__(self):
        super().__init__(self)
        self.my_cart = Cart()
        self.my_balance = 0
        self.purchased_items = []
    
    def add_balance(self,quantity):
        """Add balance from credit card.
        Args:
            quantity(int): amount that is being transferred from credit card to customer's store balance.
        Returns:
            Takes money from credit card and updates the balance.
        """
        self.my_balance += quantity
        
    def show_my_purchased_items(self):
        """Print customer's list of purchased items."""
        for product in self.purchased_items:
            print(f"{product.name}\n")
    

class Vendor(User):
    """Subclass of User. Sells products in this store.
    Attribute:
        my_products(list of Product objects): list of products that vendor is selling.
    """
    def __init__(self):
        super().__init__(self)
        self.my_products = []
        
    def add_product(self,store,item_name,item_price,item_quantity):
        """Add product to the store's inventory.
        Args:
            store(Store object): this store.
            item_name(str): name of the product.
            item_price(int): price of the product in USD.
            item_quantity(int): quantity of the product.
        Returns:
            Updates the store's inventory and the vendor's my_products list.
        """
        product = Product(item_name,item_price,item_quantity,self)
        store.inventory.append(product)
        self.my_products.append(product)
        
    def remove_product(self,store,item_name):
        """Remove product from the store's inventory. Only if this product is being sold by this vendor.
        Args:
            store(Store object): this store.
            item_name(str): name of the product.
        Returns:
            Updates the store's inventory and the vendor's my_products list.
            If the product doesn't belong to this vendor, prints a message.
        """
        product = store.find_product(item_name)
        if product.vendor == self:
            store.inventory.remove(product)
            self.my_products.remove(product)
        else:
            print("You are not selling this product.")
    def get_product_information(self,name):
        """returns the current product information.
        Args:
            qt: current quantity of the products
        """
        return f("{product.name}: {product.price}$. {product.quantity}")
            
    def see_my_products(self):
        """Prints the vendor's my_products list."""
        for product in self.my_products:
            print(f"{product.name}: {product.price}$. {product.quantity} available in stock.\n")
        
class Admin(User):
    """Subclass of User. Has the authority to edit inventory, 
    add/remove vendors and customers, see their info."""
    def add_to_inventory(self,store,item_name,item_quantity,item_price):
        """Assuming the product is not in inventory, adds a new product to the inventory.
        Args:
            store(Store object): this store.
            item_name(str): name of the product.
            item_quantity(int): quantity of the product.
            item_price(int): price of the product.
        Returns:
            Updates the store's inventory with a new product. Admin is the vendor of this product.
        """
        product = Product(item_name,item_price,item_quantity,self)
        store.inventory.append(product)
            
    def take_from_inventory(self,store,item_name,quantity):
        """Assuming the product is in inventory and the requested quantity is available in stock,
        takes some amount of the product from the store's inventory.
        Args:
            store(Store object): this store.
            item_name(str): name of the product.
            quantity(int): quantity of the product being taken.
        Returns:
            Updates the store's inventory.
        """
        product = store.find_product(item_name)
        product.decrease_quantity(quantity)
        
    def remove_from_inventory(self,store,item_name):
        """Assuming the product is in inventory and the requested quantity is available in stock,
        removes the product completely from the store's inventory.
        Args:
            store(Store object): this store.
            item_name(str): name of the product.
        Returns:
            Updates the store's inventory.
        """
        product = store.find_product(item_name)
        store.inventory.remove(product)
            
    def add_new_user(self,store,user):
        """Adds a new user.
        Args:
            store(Store object): this store.
            user(User object): a new user.
        Returns:
            Updates the store's list of users.
        """
        store.list_of_users.append(user)
        
    def remove_user(self,store,user):
        """Removes a user.
        Args:
            store(Store object): this store.
            user(User object): a user that is being removed.
        Returns:
            Updates the store's list of users.
        """
        store.list_of_users.remove(user)
        
    def get_list_of_users(self,store):
        """Prints the store's list of users.
        Args:
            store(Store object): this store."""
        for user in store.list_of_users:
            print(user.username + "\n")
            
    def get_user_info(self, store, username):
        """Prints user's info.
        Args:
            store(Store object): this store.
            username(str): username of the user.
        Returns:
            Prints user's username, email, and password.
        """
        for user in store.list_of_users:
            if user.username == username:
                print(f"Username: " + {username} + "\nEmail: " + {user.email} + "\nPassword: " + {user.password}) 
        
class Cart:
    """Calculate final checkout price of the order with the option to add
    or remove from cart and to add a discount code. """
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
        """Determines the checkout price for the order by including the shipping cost and discount 
        Args: 
            discount codes, Shipping cost. 
       Returns: Float of the final checkout price"""
        cost_of_products = 0
        for product in self.cart:
            cost_of_products += product.price * product.quantity
        total_cost_usd = cost_of_products + self.discount + self.shipping + self.tax
        return total_cost_usd
    
    def show_cost(self):
        """Shows the final price of the products along with the addition of any discounts"""

        cost = self.calculate_cost(self)
        if self.discount != 0: 
            cost = self.apply_discount(self)
        print(f"Total checkout: ${cost}")
        
    def apply_discount(self):

        '''
        Applies a discount to the cart 
        '''
        
        cost = self.calculate_cost()
        new_price = cost * (1 - (self.discount/100))
        
        return new_price
    
    def show_amount_saved(self):
        """Shows the user the amount of money they saved.
        Returns:
            The total money they saved.
        """
        saved = self.apply_discount(self)
        print(f"Total saved: ${saved}")
              
    def show_in_different_currency(self, currency):
        """Implement API here. 
        Args: 
            Original Price, Final price in desired currency.
        Returns the final price of the item in the customer's currency."""
        cost = self.calculate_cost(self)
        if currency == "Euro":
            cost = cost * 0.82
            print(f"Total checkout: €{cost}")
        if currency == "USD":
            cost = cost * 1
        if currency == "GBP":
            cost = cost * 1.5
        else:
            print("Sorry, this currency is not available.")
            
    def checkout(self,customer, store):
        """Assuming the customer has enough balance."""
        customer.balance -= self.calculate_cost(self)
        for product in self.cart:
            customer.purchased_items.append(product)
            store.inventory.removed(product)
        self.cart = []
        
    def change_cart(self,change_type="remove", product):
        """Add or remove a product to the cart.
        Args:
            product(Product object): a product that customer wants to add to their shopping cart.
        Returns:
            Updates the shopping cart.
        """
        if change_type == "add":
            self.add_product(product)
        else:
            self.remove_product(product)
        
    def checkout_cart(self, store):
        """Checkout the cart.
        Args:
            store(Store object): this store.
        Returns:
            Checkout the cart.
        """
        self.checkout(self)
