from functions import *
#MAIN
# Initial Variables


inventory_list=[]

total_to_pay=0

op=options_inventory()
while op<4:
    
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
        print_inventory(inventory_list)
    elif op==3:
        print(f"Total Earned : {total_to_pay}")  
        
    op=options_inventory()
#Print inventory
print("-------*************-------")
print("END")


