from final import Product
from final import Vendor
from final import Cart
import pytest

def test_product():
    product = Product('Stapler', 10.99, 100, 'Office Depot', 'A stapler to staple papers')
    
    assert product is Product
    
    product.increase_quantity(10)
    
    assert product.quantity == 110 
    
    product.decrease_quantity(20)
    
    assert product.quantity == 90
    
    assert product.name == 'Stapler'
    assert product.price == 10.99
    assert product.vendor == 'Office Depot'
    assert product.description == 'A stapler to staple papers'
    
def test_cart():
    
    cart = Cart()
    
    product = Product('Apple', 2501, 3, 'Sky7Food', 'A yummy fruit')
    assert product is Product

    cart.add_product(product)
    cart.add_product(product)
    cart.add_product(product)


    assert cart.cart == ['Apple', 'Apple', 'Apple']
    assert cart.remove(product) == ['Apple', 'Apple']
    assert cart.show_cost() == 5002
    assert cart.show_in_different_currency('Euro') == 4101.64
    
def test_vendor():
    
    vendor = Vendor('OD', 'office_depot@office.com')
    store = Store() 
    
    vendor.add_product(store, 'Stapler', 10.99, 100, 'Office Depot', 'A stapler to staple papers')
    vendor.add_product(store, 'Paper', 3.99, 1000, 'Office Depot', 'Paper')
    
    assert len(vendor.my_products) == 2
    
    assert vendor.get_product_information('Stapler') == 'Stapler: $10.99 100'
    
    vendor.remove_product('Paper')
    
    assert len(vendor.my_products) == 1
    
    assert vendor.see_my_products() == 'Stapler: $10.99. 100 available in stock.'
    


    
    
