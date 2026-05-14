"""Main menu and starts program"""

import file_manager
import inventory_manager
import reports

file_manager.initialize_products()
file_manager.initialize_vendors()
file_manager.initialize_orders()

def main():
    '''Handles main system interface, user inputs number and relating process is called'''
    while True:
        print("Inventory Managent System")
        print("1. Manage Products")
        print("2. Manage Vendors")
        print("3. Manage Orders")
        print("4. Reports")
        print("5. Export Data to Spreadsheet")
        print("6. Exit")

        user_input = input("\nPlease select an option: ")
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Invalid input please enter a number")
        if user_choice <= 0 or user_choice > 6:
            print("Invalid Input, Input must be 1-6")
        elif user_choice == 1:
            manage_products()
        elif user_choice == 2:
            manage_vendors()
        elif user_choice == 3:
            manage_orders()
        elif user_choice == 4:
            manage_reports()
        elif user_choice == 5:
            manage_spreadsheets()
        elif user_choice == 6:
            break

# -------------------- Product Management --------------------
def manage_products():
    '''Product management interface, user inputs number and relating process is called'''
    while True:
        print("1. Create Product")
        print("2. Search for Product")
        print("3. View all Products")
        print("4. Edit Product")
        print("5. Exit")

        user_input = input("\nPlease select an option: ")
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Invalid input please enter a number")
        if user_choice <= 0 or user_choice > 5:
            print("Invalid Input, Input must be 1-5")
        elif user_choice == 1:
            inventory_manager.add_product()
        elif user_choice == 2:
            id_input = input("Enter Product id: ")
            reports.show_product(id_input)
        elif user_choice == 3:
            reports.show_product()
        elif user_choice == 4:
            inventory_manager.edit_product()
        elif user_choice == 5:
            break

# -------------------- Vendor Management --------------------
def manage_vendors():
    '''Vendor management interface, user inputs number and relating process is called'''
    while True:
        print("1. Create Vendor")
        print("2. Search for Vendor")
        print("3. View all Vendors")
        print("4. Edit Vendors")
        print("5. Exit")

        user_input = input("\nPlease select an option: ")
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Invalid input please enter a number")
        if user_choice <= 0 or user_choice > 5:
            print("Invalid Input, Input must be 1-5")
        elif user_choice == 1:
            inventory_manager.add_vendor()
        elif user_choice == 2:
            id_input = input("Enter Vendor id: ")
            reports.show_vendor(id_input)
        elif user_choice == 3:
            reports.show_vendor()
        elif user_choice == 4:
            inventory_manager.edit_vendor()
        elif user_choice == 5:
            break

# -------------------- Purchase Order Management --------------------
def manage_orders():
    '''Purchase Order management interface, user inputs number and relating process is called'''
    while True:
        print("\n1. Create Order")
        print("2. Search for Order")
        print("3. View all Orders")
        print("4. Recive Order")
        print("5. Exit")

        user_input = input("\nPlease select an option: ")
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Invalid input please enter a number")
        if user_choice <= 0 or user_choice > 5:
            print("Invalid Input, Input must be 1-5")
        elif user_choice == 1:
            inventory_manager.create_order()
        elif user_choice == 2:
            id_input = input("Enter Product id: ")
            reports.show_order(id_input)
        elif user_choice == 3:
            reports.show_order()
        elif user_choice == 4:
            inventory_manager.recive_order()
        elif user_choice == 5:
            break

# -------------------- Report Management --------------------
def manage_reports():
    '''Report management interface, user inputs number and relating process is called'''
    while True:
        print("\n1. Low Stock Items")
        print("2. Out of Stock Items")
        print("3. Sorted Products")
        print("4. Total Inventory Value")
        print("5. Open Orders")
        print("6. Orders sorted by date")
        print("7. Exit")

        user_input = input("\nPlease select an option: ")
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Invalid input please enter a number")
        if user_choice <= 0 or user_choice > 7:
            print("Invalid Input, Input must be 1-7")
        elif user_choice == 1:
            reports.find_low_stock()
        elif user_choice == 2:
            reports.find_no_stock()
        elif user_choice == 3:
            reports.show_sorted_prodcut()
        elif user_choice == 4:
            reports.total_inventory_val()
        elif user_choice == 5:
            reports.open_orders()
        elif user_choice == 6:
            reports.show_sorted_order()
        elif user_choice == 7:
            break

# -------------------- Spreadsheet Management --------------------
def manage_spreadsheets():
    while True:
        print("1. Export Product data to excel")
        print("2. Export Vendor data to excel")
        print("3. Exit")

        user_input = input("\nPlease select an option: ")
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Invalid input please enter a number")
        if user_choice <= 0 or user_choice > 3:
            print("Invalid Input, Input must be 1-3")
        elif user_choice == 1:
            reports.export_products_excel()
        elif user_choice == 2:
            reports.export_vendors_excel()
        elif user_choice == 3:
            break

if __name__ == '__main__':
    main()
