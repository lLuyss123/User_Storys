from functions import *
#MAIN
# Initial Variables


inventory_list=[]

total_to_pay=0



print("------ Inventory ------")
op=options_inventory()
if op==1:
    keep_add=True
    while keep_add:
        print("** Adding Items **")
        name=valid_item_name()
        value1=verify_product_price()
        value2=verify_product_quantity()
        total=total_pay(value1,value2)
        total_to_pay=total_to_pay+total  
    
        inventory_dictionary={
        "Name":name,
        "Price":value1,
        "Quantity":value2,
        "Total Price":total
        }
        inventory_list.append(inventory_dictionary)
        keep_add=valid_option_to_contin()
                
elif op==2:
    print()
elif op==3:
    print()
else:
    print()

#Print inventory
print("------------------")
print(f"Total Earned : {total_to_pay}")  

print_inventory(inventory_list)