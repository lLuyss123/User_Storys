# User_Storys

### Project description
There are two main files:
- `inventario.py`: controls the menu and user interaction.
- `functions.py`: contains actions and validations (add, show, search, update, delete, stats, CSV).

### What the code does
1. Shows a menu with inventory options.
2. Adds products with name, price, and quantity.
3. Validates:
   - name is not empty
   - price is a number and > 0
   - quantity is an integer and > 0
4. Saves and reads data in `inventory.csv`.
5. Searches a product by name and shows its data.
6. Updates a product by name (changes name, price, quantity).
7. Deletes a product by name.
8. Shows stats (total units, total value, most expensive item, item with most stock).
9. Loads an external CSV and handles invalid rows, with overwrite or merge options.

### Specific validations
- `verify_product_price()`: requires float > 0.
- `verify_product_quantity()`: requires int > 0.
- `valid_item_name()`: does not allow empty string.
- `valid_option_to_contin()`: asks YES/NO to continue adding.

### Files
- `inventory.csv`: file used as the database. It is created automatically if it does not exist.
- `functions.py`: operations logic.
- `inventario.py`: menu interface.
