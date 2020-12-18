from final import Product
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
    
    
    
