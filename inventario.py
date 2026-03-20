from functions import *
#MAIN
# Initial Variables

inventory_dictionary={
    "items_name":[],
    "prices_by_1":[],
    "quantitys":[],
    "total_price":[]
}

total_to_pay=0


#I use functions to valid the user input
print("------ Inventory ------")
op=options_inventory()
if op==1:
    keep_add=True
    keep="yes"
    while keep_add:
        print("** Adding Items **")
        name=valid_item_name()
        add_to_inventory(name,inventory_dictionary["items_name"])
        
        value1=verify_product_price()
        add_to_inventory(value1,inventory_dictionary["prices_by_1"])
        
        value2=verify_product_quantity()
        add_to_inventory(value2,inventory_dictionary["quantitys"])
        
        total=total_pay(value1,value2)
        total_to_pay=total_to_pay+total            
        add_to_inventory(total,inventory_dictionary["total_price"])  
        
        keep_add=valid_option_to_contin()
                
elif op==2:
    print()
elif op==3:
    print()
else:
    print()

#Print inventory
print("------------------")