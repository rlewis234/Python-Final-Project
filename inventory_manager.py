"""contains core functions for adding, editing, searching, sorting, and processing inventory and purchase orders"""

from models import Product, Vendor, PurchaseOrder
from datetime import datetime
import file_manager 

# -------------------- Product Management --------------------

def add_product():
    '''Adds products to the system'''

    # User Inputs for product atributes
    while True:
        while True:
            product_id = input("Product ID: ").strip()
            if check_product_id(product_id) == True:
                print(f"Invalid Input product with the ID {product_id} already exists")
            else:
                break
        name = input("Product Name: ").strip().title()
        category = input("Category: ").strip().title()
        while True:
            quantity_input = input("Quantity in stock: ").strip()
            try:
                quantity = int(quantity_input)
                break
            except ValueError:
                print("Invalid input, please enter a valid number")
        while True:
            reorder_input = input("Reorder level: ").strip()
            try:
                reorder_level = int(reorder_input)
                break
            except ValueError:
                print("Invalid input, please enter a valid number")
        while True:
            reorder_quantity_input = input("Reorder quantity: ").strip()
            try:
                reorder_quantity = int(reorder_quantity_input)
                break
            except ValueError:
                print("Invalid input, please enter a valid number")
        while True:
            price_input = input("Unit price: ").strip()
            try:
                price = float(price_input)
                break
            except ValueError:
                print("Invalid input, please enter a valid dollar amount")
        vendor_id = input("Vendor ID: ").strip()
        status = "Active"

        # Promots user to confirm all enterede information is correct, if not the process will repeat
        print("\nPlease confirm the product details:")
        print(f"Product ID: {product_id}")
        print(f"Name: {name}")
        print(f"Category: {category}")
        print(f"Quantity: {quantity}")
        print(f"Reorder Level: {reorder_level}")
        print(f"Reorder Quantity: {reorder_quantity}")
        print(f"Unit Price: {price}")
        print(f"Vendor ID: {vendor_id}")
        print(f"Status: {status}")

        user_confirm = input("Are all details correct? (Y/N): ").strip().lower()
        if user_confirm == "y":
            break
        else:
            print("\nPlease enter the details again.")

    # Saves the product to the products.json file
    product = Product(product_id, name, category, quantity, reorder_level, reorder_quantity, price, vendor_id, status)
    file_manager.products[product_id] = product
    file_manager.save_products()
    print(f"Product {name} added successfully.")

def edit_product():
    '''Allows the a entered product to be edited'''
    
    # Prompts the user for the Product ID for the product they wish to eidt
    product_id = input("Enter Product ID to edit: ")
    product = file_manager.products.get(product_id)

    # If their is not product with entered ID
    if not product:
        print(f"Product with ID {product_id} not found.")
        return
    
    # The editing process
    while True:
        print(f"1. Product Name (currently {product.name})")
        print(f"2. Category (currently {product.category})")
        print(f"3. Quantity in stock (currently {product.quantity})")
        print(f"4. Reorder Level (currently {product.reorder_level})")
        print(f"5. Reorder Quantity (currently {product.reorder_quantity})")
        print(f"6. Price (currently ${product.price:.2f})")
        print(f"7. Vendor ID (currently {product.vendor_id})")
        print(f"8. Status (currently {product.status})")
        print(f"9. Exit")
        
        while True:
            user_choice = input("Choose what atribute to edit: ")
            try:
                user_selection = int(user_choice)
            except ValueError:
                print("Invalid input please enter a number")
            if user_selection < 1 or user_selection > 9:
                print("Invalid Input please enter a valid number")
            else:
                break

        if user_selection == 1:
            while True:
                product_name_input = input("What is the new name of the product?: ").strip()
                user_confirm = input(f"New product name is {product_name_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.name = product_name_input
                    break
        elif user_selection == 2:
            while True:
                category_input = input("What is the new category of the product?: ").strip()
                user_confirm = input(f"New category name is {category_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.category = category_input
                    break
        elif user_selection == 3:
            while True:
                while True:
                    quantity_input = input("What is the new quantity in stock of the product?: ").strip()
                    try:
                        quantity_input_val = int(quantity_input)
                        break
                    except ValueError:
                        print("Invalid Input please enter whole number")
                user_confirm = input(f"New quantity in stock is {quantity_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.quantity = quantity_input_val
                    break
        elif user_selection == 4:
            while True:
                while True:
                    reorder_level_input = input("What is the new reorder level of the product?: ").strip()
                    try:
                        reorder_level_val = int(reorder_level_input)
                        break
                    except ValueError:
                        print("Invalid Input please enter whole number")
                user_confirm = input(f"New reorder level is {reorder_level_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.reorder_level = reorder_level_val
                    break
        elif user_selection == 5:
            while True:
                while True:
                    reorder_quantity_input = input("What is the reorder quantity of the product?: ").strip()
                    try:
                        reorder_qauntity_val = int(reorder_quantity_input)
                        break
                    except ValueError:
                        print("Invalid Input please enter whole number")
                user_confirm = input(f"New reorder quantity is {reorder_quantity_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.reorder_quantity = reorder_qauntity_val
                    break
        elif user_selection == 6:
            while True:
                while True:
                    price_input = input("What is the new price of the product?: ").strip()
                    try:
                        price_val = float(price_input)
                        break
                    except ValueError:
                        print("Invalid Input please a valid dollar amount")
                user_confirm = input(f"New price is {price_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.price = price_val
                    break
        elif user_selection == 7:
            while True:
                vendor_id_input = input("What is the new Vendor ID of the product?: ").strip()
                user_confirm = input(f"New Vendor ID is {vendor_id_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.vendor_id = vendor_id_input
                    break
        elif user_selection == 8:
            while True:
                status_input = input("What is the new status the product?: ").strip()
                user_confirm = input(f"New status is {status_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    product.status = status_input
                    break
        elif user_selection == 9:
            break
    
    # Save changes
    file_manager.save_products()
    print(f"\nProduct {product_id} updated successfully.")

def check_product_id(product_id):
    '''Checks to see if a product with inputed id already exist'''
    for product in file_manager.products:
        if product == product_id:
            return True
    return False

# -------------------- Vendor Management --------------------

def add_vendor():
    '''Adds vendors to the system'''

    # User Input for vednor atributes
    while True:
        while True:
            vendor_id = input("Vendor ID: ").strip()
            if check_vendor_id(vendor_id) == True:
                print(f"Invalid input vendor with ID {vendor_id} already exists")
            else:
                break
        vendor_name = input("Vendor Name: ").strip().title()
        contact_name = input("Vendor Contact Name: ").strip().title()
        phone = input("Vendor Phone Number: ").strip()
        email = input("Vendor Email: ").strip()
        address = input("Vendor Address: ").strip()

        # User Conformation
        print("\nPlease confirm vendor details:")
        print(f"Vendor ID: {vendor_id}")
        print(f"Vendor Name: {vendor_name}")
        print(f"Vendor Contact Name: {contact_name}")
        print(f"Vendor Phone Number: {phone}")
        print(f"Vendor Email: {email}")
        print(f"Vendor Address: {address}")

        user_confirm = input("Are all details correct? (Y/N): ").strip().lower()
        if user_confirm == "y":
            break
        else:
            print("\nPlease enter the details again.")
        
    # Saves the vendor to the vendors.json file
    vendor = Vendor(vendor_id, vendor_name, contact_name, phone, email, address)
    file_manager.vendors[vendor_id] = vendor
    file_manager.save_vendors()
    print(f"Vendor {vendor_name} added successfully.")

def edit_vendor():
    '''Allows the editing of added vendors'''

    # prompts the user of the id of vendor that needs edited
    vendor_id = input("Enter the ID of the vendor you wish to edit: ")
    vendor = file_manager.vendors.get(vendor_id)

    # If their is not a vendor with entered ID
    if not vendor:
        print(f"Vendor with ID {vendor_id} not found.")
        return

    # The editing process
    while True:
        print(f"1. Vendor Name: {vendor.vendor_name}")
        print(f"2. Vendor Contact Name: {vendor.contact_name}")
        print(f"3. Vendor Phone Number: {vendor.phone}")
        print(f"4. Vendor Email: {vendor.email}")
        print(f"5. Vendor Address: {vendor.address}")
        print(f"6. Exit")

        while True:
            user_choice = input("Choose an atribute to edit: ")
            try:
                user_selection = int(user_choice)
            except ValueError:
                print("Invalid input please enter a number")
            if user_selection < 1 or user_selection > 9:
                print("Invalid Input please enter a valid number")
            else:
                break

        if user_selection == 1:
            while True:
                vendor_name_input = input("What is the new name of the vendor?: ").strip()
                user_confirm = input(f"New vendor name is {vendor_name_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    vendor.vendor_name = vendor_name_input
                    break
        elif user_selection == 2:
            while True:
                vendor_contact_name_input = input("What is the new Vendor Contact Name: ").strip().title()
                user_confirm = input(f"New Vendor Contact name is {vendor_contact_name_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    vendor.contact_name = vendor_contact_name_input
                    break
        elif user_selection == 3:
            while True:
                vendor_email_input = input("What is the new Vendor Email?: ").strip()
                user_confirm = input(f"New Vendor Email is {vendor_email_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    vendor.email = vendor_email_input
                    break
        elif user_selection ==4:
            while True:
                phone_input = input("What is the new Vendor Phone Number?: ").strip()
                user_confirm = input(f"New Vendor Phonenumber is {phone_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    vendor.phone = phone_input
                    break
        elif user_selection == 5:
            while True:
                address_input = input("What is the new Vendor Address?: ")
                user_confirm = input(f"New vendor address is {address_input} Is this correct?(y or n): ").strip().lower()
                if user_confirm == 'y':
                    vendor.address = address_input
                    break
        elif user_selection == 6:
            break
    
    # Save changes
    file_manager.save_vendors()
    print(f"\nVendor {vendor_id} updated successfully.")

def check_vendor_id(vendor_id):
    '''Checks to see if a vendor with inputed id already exist'''
    for vendor in file_manager.vendors:
        if vendor == vendor_id:
            return True
    return False

# -------------------- Purchase Order Management --------------------

def create_order():
    '''Creates a Purchase Order based on user input'''

    ordered_items = []

    # Prompts user for input
    while True:
        while True:
            ponumber = input("PO Number: ").strip()
            if check_ponumber(ponumber) == True:
                print(f"Invalid input, PO Number {ponumber} already exist")
            else:
                break
        while True:
            vendor_id = input("Vendor ID: ").strip()
            if check_vendor_id(vendor_id) == False:
                print(f"Invalid Input, no vendor with the id {vendor_id} exists")
            else:
                break
        date_created = datetime.today().strftime('%m-%d-%Y')
        while True:
            order_item_id = input("Enter the ID of the item you wish to order: ")
            if check_product_id(order_item_id) == False:
                print(f"Invalid Input, no product with the id {order_item_id} exists")
            elif file_manager.products[order_item_id].vendor_id != vendor_id:
                print(f"Product {order_item_id} dose not belong to vendor {vendor_id}")
            elif file_manager.products[order_item_id].status == "Inactive":
                print(f"Product {order_item_id} is inactive and can not be ordered")
            else:
                ordered_items.append(order_item_id)
                user_choice = input("Order another item?(n to stop): ")
                if user_choice == 'n':
                    break
        items_ordered = sum(file_manager.products[product].reorder_quantity for product in ordered_items)
        total_cost = sum(file_manager.products[product].price for product in ordered_items)
        status = "Ordered"
        
        # Order Review and user conformation
        print(f"\nPO Number: {ponumber}")
        print(f"Vendor ID: {vendor_id}")
        print(f"Date Created: {date_created}")
        print(f"IDs of ordered Items: {ordered_items}")
        print(f"Total items ordered: {items_ordered}")
        print(f"Total Cost: ${total_cost:.2f}")

        user_confirm = input("Are order details correct?(y to confirm): ")
        if user_confirm == 'y':
            break
    
    # Saves the order to the purchaseorders.json file
    order = PurchaseOrder(ponumber, vendor_id, date_created, ordered_items, items_ordered, total_cost, status)
    file_manager.orders[ponumber] = order
    file_manager.save_orders()
    print(f"Order {ponumber} added successfully.")

def recive_order():
    '''Allows orders to be recived adding ordered items to stock'''

    order_recived = input("What is the PO number of the recived order?: ").strip()
    order = file_manager.orders.get(order_recived)
    if check_ponumber(order_recived) == True and file_manager.orders[order_recived].status != "Recived":
        for product_id in order.ids_order:
            product = file_manager.products[product_id]
            product.quantity += product.reorder_quantity
        order.status = "Recived"
        file_manager.save_orders()
        file_manager.save_products()
        print(f"Order {order_recived} successfully recived")
    elif check_ponumber(order_recived) == True and file_manager.orders[order_recived].status == "Recived":
        print(f"Order {order_recived} already Recived")
    elif check_ponumber(order_recived) == False:
        print(f"Order {order_recived} does not exists")

def check_ponumber(ponumber):
    '''Checks to see if an order with inputed po number already exist'''
    for order in file_manager.orders:
        if order == ponumber:
            return True
    return False
