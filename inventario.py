from functions import *
#MAIN
# Initial Variables
inventory_list=[]

#I call the function that displays the inventory of operations 
#and validate the operations, then I perform the processes depend on the operations.
op=options_inventory()
while op<9:
    
    if op==1:
        keep_add=True
        
        while keep_add:
            print("** Adding Items **")
            name=valid_item_name()
            value1=verify_product_price()
            value2=verify_product_quantity()
            total=total_pay(value1,value2) 
            #I used the dictionary here because the reference so
            #I can change the values(dictionary) and adding to the list WITHOUT ERRORS
            inventory_dictionary={
            "Item Name":name,
            "Item Price":value1,
            "Item Quantity":value2,
            "Total Price":total
            }
            inventory_list.append(inventory_dictionary)
            keep_add=valid_option_to_contin()
            crate_csv(inventory_dictionary)
            
                    
    elif op==2:
        print_csv()
    elif op==3:
        name=input("Searching by ITEM NAME: ")
        search_items(name)
        
    elif op==4:
        name=input("Updating by ITEM NAME: ")
        update_item(name)
    
    elif op==5:
        name=input("Deleting by ITEM NAME: ")
        delete_item(name)
        
    elif op==6:
        stats_inventory() 
        
    elif op==7:
        archivo_existe = existe_headers()
        if archivo_existe==True:
            print("CSV is SAVED")  
            print(os.path.abspath("inventory.csv"))
        else:
            print("Inventory is Empty")
        
        
    elif op==8:
        print(f"not ready")
    
    #Ask for the options to the user    
    op=options_inventory()
    
print("-------*************-------")
print("END")


