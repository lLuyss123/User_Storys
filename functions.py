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

# OS Es un módulo estándar de Python. Significa “sistema operativo”. Sirve para hacer cosas como leer/escribir archivos, ver carpetas, rutas, permisos, etc. Ejemplo frase: “os es la parte que me conecta con el sistema de archivos de la máquina”.

# PATH Es un submódulo dentro de os: os.path. Se usa para trabajar con rutas de archivos y carpetas (paths). Funciones comunes: join, dirname, basename, exists. Ejemplo frase: “path es la herramienta para manipular direcciones de archivos (‘la ruta’).”

# EXISTS Es una función dentro de os.path: os.path.exists(...). Devuelve True si la ruta existe, False si no. Funciona con archivo o carpeta. Ejemplo frase: “exists pregunta si la ruta existe antes de leer/escribir para que no rompa el programa.”


######


# Aquí creo el archivo csv y luego escribo en el archivo la informacion que necesito
# Verifico que el archivo exista, si no existe lo creo inicialmente con los encabezados que son una lista
def crate_csv(dic):
    archivo_existe, lista = existe_headers()
    if not archivo_existe:
        with open("inventory.csv", mode="w", newline="") as f:
            csvv = csv.writer(f)
            csvv.writerow(lista)
    write_csv(dic)


def existe_headers():
    archivo_existe = os.path.exists("inventory.csv")
    lista = ["Item Name", "Item Price", "Item Quantity", "Total Price"]
    return archivo_existe, lista


# Despues de crear el archivo csv ya que este proceso se hace a la vez que se ingresan datos para almacenarlos en este archivo lo que hago es llamar la funcion de escribir la informacion del item en el archivo, verificando que el archivo ya esté creado para que no salga ningun error
def write_csv(dic):
    archivo_existe, lista = existe_headers()
    if archivo_existe:
        with open("inventory.csv", "a", newline="") as f:
            csvv = csv.DictWriter(f, fieldnames=lista)
            csvv.writerow(dic)


# Verifico que el archivo exista luego lo abro en forma de lectura y ya que lo quiero mostrar en una sola linea lo que hago es que en una variable linea voy agregando cada clave valor para al final solo imprimir la linea


def print_csv():
    archivo_existe = existe_headers()
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


# Verifico que el archivo exista luego abro el archivo en forma de lectura, luego inicializo un booleano en false este hace referencia a que no he encontrado ese item en el inventario, luego me muevo por cada clave (Item name) y verifico si es igual a itemname sino me muevo al siguiente diccionario, si es igual simplemente guardo la informacion de ese diccionario en una variable para luego imprimirla
def search_items(itemname):
    archivo_existe = existe_headers()
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
    archivo_existe = existe_headers()
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


