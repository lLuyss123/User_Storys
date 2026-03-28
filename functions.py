import csv, os


# OP Inventory
def options_inventory():
    is_ok = True
    print("------ Inventory ------")
    print("1. Add Product")
    print("2. Show Inventory")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Analytics")
    print("7. Save CSV")
    print("8. Upload CSV")

    print("9. Exit")
    while is_ok:
        try:
            op = int(input("Selecct an Option: "))
            if op > 0 and op < 10:
                is_ok = False
                return op
            else:
                print("OPTIONS 1 TO 9 ONLY")
        except:
            print("OPTIONS 1 TO 9 ONLY")


# Valid the user price
def verify_product_price():
    is_ok = True
    while is_ok:
        try:
            price = float(input("Product Price: "))
            if price > 0:
                is_ok = False
                return price
            else:
                print("Prodcut Price has to be > 0")
        except:
            print("Product Price is not Valid")


# Valid the user quantity
def verify_product_quantity():
    is_ok = True
    while is_ok:
        try:
            quantity = int(input("Product Quantity: "))
            if quantity > 0:
                is_ok = False
                return quantity
            else:
                print("Prodcut Quantity has to be > 0")
        except:
            print("Product Quantity is not Valid")


# Valid the user option is on the list of op
def valid_option_to_contin():
    is_ok = False
    while is_ok == False:
        value = input("Do you want to keep adding items YES/NO: ").lower()
        if value == "no":
            return False
        elif value == "yes":
            return True
        else:
            print("ONLY YES OR NO")


# Valid the user name not empty
def valid_item_name():
    is_ok = False
    while is_ok == False:
        item_name = input("Item name: ").strip()

        if len(item_name) == 0:
            print("Item name cannot be empty")
        else:
            is_ok = True
            return item_name


# Calculate the items total to pay
def total_pay(value1, value2):
    total = value1 * value2
    return total


# Show the inventory that is on a list and inside of the list has dic
def print_inventory(inventory):
    if not inventory:
        print("Inventory is EMPTY")
    else:
        for diccionario in inventory:
            print("-------------------------")
            for key, value in diccionario.items():
                print(key, value)


# ---------------------------------------------------------------------

# OS is a standard Python module. It means "operating system". It helps you do things like read/write files, view folders, paths, permissions, etc. Example phrase: "os is the part that connects me to the machine's file system".

# PATH is a submodule within os: os.path. It is used to work with file and folder paths (paths). Common functions: join, dirname, basename, exists. Example phrase: "path is the tool to manipulate file addresses ('the path')."

# EXISTS is a function within os.path: os.path.exists(...). Returns True if the path exists, False if not. It works with files or folders. Example phrase: "exists asks if the path exists before reading/writing so it doesn't break the program."


######


# Here I create the csv file and then write the information I need into the file
# I check if the file exists, if it doesn't exist I create it initially with the headers which is a list
def crate_csv(dic):
    archivo_existe, lista = existe_headers()
    if not archivo_existe:
        with open("inventory.csv", mode="w", newline="") as f:
            csvv = csv.writer(f)
            csvv.writerow(lista)
    write_csv(dic)


def existe_headers():
    archivo_existe = os.path.exists("inventory.csv")
    lista = ["Item Name", "Item Price", "Item Quantity"]
    return archivo_existe, lista


# After creating the csv file, since this process is done at the same time data is entered to store them in this file, I call the function to write the item information to the file, verifying that the file is already created so no error occurs
def write_csv(dic):
    archivo_existe, lista = existe_headers()
    if archivo_existe:
        with open("inventory.csv", "a", newline="") as f:
            csvv = csv.DictWriter(f, fieldnames=lista)
            csvv.writerow(dic)


# I check if the file exists, then I open it in read mode and since I want to display it on one line, what I do is add each key-value pair to a line variable so that at the end I only print the line


def print_csv():
    archivo_existe,l = existe_headers()
    if archivo_existe:
        with open("inventory.csv", "r") as f:
            csvv = csv.DictReader(f)
            for dic in csvv:
                line = ""
                for k, v in dic.items():
                    line += (f"{k}: {v} ")
                print(line)
    else:
        print("Inventory is Empty")


# I check if the file exists, then I open the file in read mode. Then I initialize a boolean to false which refers to the fact that I have not found that item in the inventory. Then I move through each key (Item name) and check if it equals itemname, if not I move to the next dictionary. If it equals, I simply save that dictionary's information in a variable to print it later
def search_items(itemname):
    archivo_existe,l = existe_headers()
    if archivo_existe:
        with open("inventory.csv", mode="r") as f:
            csvv = csv.DictReader(f)
            find = False
            for dic in csvv:
                line = ""
                if dic.get("Item Name") == itemname:
                    find = True
                    for k, v in dic.items():
                        line += (f"{k}: {v} ")
                    print(line)
            if find == False:
                print("The Item is NOT into the Inventory")
    else:
        print("Inventory is Empty")


def delete_item(itemname):
    find=False
    archivo_existe,l = existe_headers()
    if archivo_existe:
        lista = []
        
        with open("inventory.csv",mode="r") as f:
            csvv = csv.DictReader(f)
            header = csvv.fieldnames
            for dic in csvv:
                if dic["Item Name"]==itemname:
                    print("Item Deleted")
                    find=True
                    continue
                lista.append(dic)
            if not find:
                print("Item Not Finded")
            

            # for i, dic in enumerate(lista):
            #     if dic["Item_Name"].strip() == itemname.strip():
            #         lista.pop(i)
        with open("inventory.csv", mode="w",newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(lista)

def update_item(itemname):
    
    find=False
    archivo_existe,l = existe_headers()
    if archivo_existe:
        lista = []
        
        with open("inventory.csv",mode="r") as f:
            csvv = csv.DictReader(f)
            header = csvv.fieldnames
            for dic in csvv:
                line=""
                if dic["Item Name"]==itemname:
                    
                    for k, v in dic.items():
                        line += (f"{k}: {v} ")
                    print(f"Previews info {line}")
                    print("Updating Item Info")
                    
                    find=True
                    name=valid_item_name()
                    value1=verify_product_price()
                    value2=verify_product_quantity()
                    dic={
                        "Item Name":name,
                        "Item Price":value1,
                        "Item Quantity":value2
                    }
                    print("--- Item Updated Correctly ---")
                lista.append(dic)
            if not find:
                print("Item Not Finded")
            

            # for i, dic in enumerate(lista):
            #     if dic["Item_Name"].strip() == itemname.strip():
            #         lista.pop(i)
        with open("inventory.csv", mode="w",newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(lista)


def stats_inventory():
    total_units=0
    total_value=0.0
    list_dic=[]
    archivo_existe,l = existe_headers()
    if archivo_existe:
        with open("inventory.csv",mode="r") as f:
            csvv = csv.DictReader(f)
            for dic in csvv:
                total_units+=int((dic["Item Quantity"]))
                total_value+= int((dic["Item Quantity"])) * (float(dic["Item Price"]))
                list_dic.append(dic)
            more_expen=list_dic[0]
            more_stock=list_dic[0]
            for dic in list_dic:
                if float(dic["Item Price"]) > float(more_expen["Item Price"]):
                    more_expen = dic
                if float(dic["Item Quantity"]) > float(more_stock["Item Quantity"]):
                    more_stock= dic
                    
            print(f"The Most expencive Item: {more_expen['Item Name']} With: $ {more_expen['Item Price']} ")
            print(f"The Most Quantity Item: {more_stock['Item Name']} With: {more_stock['Item Quantity']} in stock")
     
        print(f"{total_units} is the Total units")          
        print(f"{total_value} is the Total Value")    
    else:
        print("Inventory is Empty") 


def load_csv(route):
    loaded_items = 0
    invalid_rows = 0
    loaded_list = []

    # 1. Open and validate the file
    try:
        with open(route, mode="r") as f:
            csvv = csv.DictReader(f)

            # Validate header
            valid_header = ["Item Name", "Item Price", "Item Quantity"]
            if list(csvv.fieldnames) != valid_header:
                print("Error: The file does not have the correct header.")
                return

            # Loop through each row
            for fila in csvv:

                # Validate that there are no empty cells
                if any(v.strip() == "" for v in fila.values()):
                    invalid_rows += 1
                    continue

                # Validate and convert data types
                try:
                    name   = fila["Item Name"].strip()
                    price   = float(fila["Item Price"])
                    quantity = int(fila["Item Quantity"])

                    if price < 0 or quantity < 0:
                        invalid_rows += 1
                        continue

                except ValueError:
                    invalid_rows += 1
                    continue

                loaded_list.append({
                    "Item Name":     name,
                    "Item Price":    price,
                    "Item Quantity": quantity
                })
                loaded_items += 1

    except FileNotFoundError:
        print(f"Error: The file was not found. '{route}'.")
        return
    except UnicodeDecodeError:
        print("Error: The file contains invalid characters.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    # 2. Ask the user what to do
    print(f"\n{loaded_items} products found in the archive.")
    decision = input("Overwrite current inventory? (YES/NO): ").strip().lower()
    while decision != "yes" and decision != "no":
        
        
        archivo_existe, header = existe_headers()

        if decision == "yes":
            # Delete everything and write what was loaded
            with open("inventory.csv", mode="w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                writer.writerows(loaded_list)
            print("Replaced Inventory.")

        elif decision == "no":
            print("Policy: If the product already exists, the quantity is added and the price is updated..")
        else:
            print("Invalid option, please type YES or NO.")
            decision = input("Overwrite current inventory? (YES/NO): ").strip().lower()

        # Read current inventory
        current_inventory = []
        if archivo_existe:
            with open("inventory.csv", mode="r") as f:
                csvv = csv.DictReader(f)
                for dic in csvv:
                    current_inventory.append(dic)

        # Merge
        for new_product in loaded_list:
            find = False
            for current_product in current_inventory:
                if current_product["Item Name"] == new_product["Item Name"]:
                    current_product["Item Quantity"] = int(current_product["Item Quantity"]) + new_product["Item Quantity"]
                    current_product["Item Price"]    = new_product["Item Price"]
                    find = True
                    #break
            if not find:
                current_inventory.append(new_product)

        # Save merge
        with open("inventory.csv", mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(current_inventory)
        print("Inventory merged.")

    # 3. Summary
    print(f"\n--- Summary ---")
    print(f"Loaded Items : {loaded_items}")
    print(f"Invalid Rows    : {invalid_rows}")
    print(f"Action             : {'Replaced' if decision == 'yes' else 'Merge'}")     