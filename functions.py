

def verify_product_price():
    is_ok=True
    while is_ok:
        try:
            price=float(input("Product Price: "))
            if (price>0):
                is_ok=False
                return price
            else:
                print("Prodcut Price has to be > 0")
        except:
            print("Product Price is not Valid")
        
        
     
     
     
def verify_product_quantity():
    is_ok=True
    while is_ok:
        try:
            quantity=int(input("Product Quantity: "))
            if (quantity>0):
                is_ok=False
                return quantity
            else:
                print("Prodcut Quantity has to be > 0")
        except:
            print("Product Quantity is not Valid")
    