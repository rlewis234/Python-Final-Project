"""contains all reporting functions"""

import file_manager
from operator import attrgetter
from openpyxl import Workbook

def find_low_stock():
    '''Finds products that are low on stock(below or at the reorder level)'''
    for p in file_manager.products.values():
        if p.quantity <= p.reorder_level:
            print(f"Product: {p.name}({p.product_id}) has {p.quantity} in stock (below reorder level ({p.reorder_level}))")
        else:
            print("No products low on stock")

def find_no_stock():
    '''Finds out of stock products'''
    for p in file_manager.products.values():
        if p.quantity == 0:
            print(f"Product: {p.name}({p.product_id}) is out of stock")
        else:
            print("No products out of stock")

def total_inventory_val():
    '''Calculates the total value of products in inventory'''

    products = []
    product_vals = []

    for p in file_manager.products.values():
        products.append(p)

    for prod in products:
        prod_val = prod.quantity * prod.price
        product_vals.append(prod_val)
    
    total_val = sum(product_vals)
    print(f"Total Inventory Value: ${total_val:.2f}")

def show_sorted_prodcut():
    '''Shows Information about products in a sorted layout'''

    products = []

    for p in file_manager.products.values():
        products.append(p)
    
    while True:
        print("1. Products by quantity in stock")
        print("2. Producst by price")
        print("3. Products by vendor")
        print("4. Products by category")
        print("5. Products by name")
        print("6. Exit")

        user_input = input("\nPlease select an option: ")
        try:
            user_choice = int(user_input)
        except ValueError:
            print("Invalid input please enter a number")
        if user_choice <= 0 or user_choice > 5:
            print("Invalid Input, Input must be 1-5")
        elif user_choice == 1:
            sorted_list = sorted(products, key=attrgetter('quantity'))
            for prod in sorted_list:
                print(f"Name: {prod.name} ID: {prod.product_id} Quantity in Stock: {prod.quantity}")
        elif user_choice == 2:
            sorted_list = sorted(products, key=attrgetter('price'))
            for prod in sorted_list:
                print(f"Name: {prod.name} ID: {prod.product_id} Price: {prod.price}")
        elif user_choice == 3:
            sorted_list = sorted(products, key=attrgetter('vendor_id'))
            for prod in sorted_list:
                print(f"Name: {prod.name} ID: {prod.product_id} Vendor ID: {prod.vendor_id}")
        elif user_choice == 4:
            sorted_list = sorted(products, key=attrgetter('category'))
            for prod in sorted_list:
                print(f"Name: {prod.name} ID: {prod.product_id} Category: {prod.category}")
        elif user_choice == 4:
            sorted_list = sorted(products, key=attrgetter('name'))
            for prod in sorted_list:
                print(f"Name: {prod.name} ID: {prod.product_id}")
        elif user_choice == 6:
            break

def open_orders():
    '''Displays all open orders'''
    for o in file_manager.orders.values():
        if o.status == "Ordered" :
            print(f"Order Number {o.ponumber} not recived")
        else:
            print("No open orders")

def show_sorted_order():
    '''Displays all orders sorted by date'''
    
    orders = []

    for o in file_manager.orders.values():
        orders.append(o)
    sorted_orders = sorted(orders, key=attrgetter('date_created'))

    for order in sorted_orders:
        print(f"PO number: {order.ponumber}, date created {order.date_created}")


def show_product(product_id=None):
    '''Prints all products if no product id is given, if ID is given only that product will be printed'''
    if product_id:
        product = file_manager.products.get(product_id)
        if product:
            print(f"\nProduct ID: {product.product_id}")
            print(f"Name: {product.name}")
            print(f"Category: {product.category}")
            print(f"Quantity in stock: {product.quantity}")
            print(f"Reorder level: {product.reorder_level}")
            print(f"Reorder quantity: {product.reorder_quantity}")
            print(f"Unit price: ${product.price:.2f}")
            print(f"Vendor ID: {product.vendor_id}")
            print(f"Status: {product.status}\n")
        else:
            print(f"Product with ID {product_id} not found.")
    else:
        if not file_manager.products:
            print("No products in inventory.")
            return
        for p in file_manager.products.values():
            print(f"\nProduct ID: {p.product_id}")
            print(f"Name: {p.name}")
            print(f"Category: {p.category}")
            print(f"Quantity in stock: {p.quantity}")
            print(f"Reorder level: {p.reorder_level}")
            print(f"Reorder quantity: {p.reorder_quantity}")
            print(f"Unit price: ${p.price:.2f}")
            print(f"Vendor ID: {p.vendor_id}")
            print(f"Status: {p.status}")
            print("-" * 30)

def show_vendor(vendor_id=None):
    '''Prints all vendors if no vendor id is given, if ID is given only that vendor will be printed'''
    if vendor_id:
        vendor = file_manager.vendors.get(vendor_id)
        if vendor:
            print(f"\nVendor ID: {vendor.vendor_id}")
            print(f"Name: {vendor.vendor_name}")
            print(f"Contact Name: {vendor.contact_name}")
            print(f"Phone Number: {vendor.phone}")
            print(f"Email: {vendor.email}")
            print(f"Address: {vendor.address}")
        else:
            print(f"Vendor with ID {vendor_id} not found.")
    else:
        if not file_manager.vendors:
            print("No vendors found.")
            return
        for v in file_manager.vendors.values():
            print(f"\nVendor ID: {v.vendor_id}")
            print(f"Name: {v.vendor_name}")
            print(f"Contact Name: {v.contact_name}")
            print(f"Phone Number: {v.phone}")
            print(f"Email: {v.email}")
            print(f"Address: {v.address}")
            print("-" * 30)

def show_order(po_number=None):
    '''Prints all orders if no PO number is given, if PO number is given only that order will be printed'''
    if po_number:
        order = file_manager.orders.get(po_number)
        if order:
            print(f"\nPO Number: {order.ponumber}")
            print(f"Vendor ID: {order.vendor_id}")
            print(f"Date Created: {order.date_created}")
            print(f"IDs of Products Ordered: {order.ids_order}")
            print(f"Total Items Ordered: {order.items_ordered}")
            print(f"Total Cost: {order.total_cost}")
            print(f"Status: {order.status}")
        else:
            print(f"Vendor with ID {po_number} not found.")
    else:
        if not file_manager.orders:
            print("No orders found.")
            return
        for o in file_manager.orders.values():
            print(f"\nPO Number: {o.ponumber}")
            print(f"Vendor ID: {o.vendor_id}")
            print(f"Date Created: {o.date_created}")
            print(f"IDs of Products Ordered: {o.ids_order}")
            print(f"Total Items Ordered: {o.items_ordered}")
            print(f"Total Cost: {o.total_cost}")
            print(f"Status: {o.status}")
            print("-" * 30)

def export_products_excel():
    '''Exports Product data into a excel spreadsheet'''

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Products"
    total_val = total_inventory_val()

    sheet.append(["Product Name", "Product ID", "Category", "Amount in Stock", "Reorder Level", "Reorder Quantity", "Price", "Vendor ID", "Status"])

    for product in file_manager.products.values():
        sheet.append([product.name, product.product_id, product.category, product.quantity, product.reorder_level, product.reorder_quantity, product.price, product.vendor_id, product.status])
    
    sheet.append([])
    sheet.append(["Total Inventory Val", total_val])

    workbook.save("products.xlsx")
    print("Data exported to products.xlsx")

def export_vendors_excel():
    '''Exports Vendor data into an excel spreadsheet'''

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Vendors"

    sheet.append(["Vendor Name", "Vendor ID", "Contact Name", "Phonenumber", "Email", "Address"])

    for vendor in file_manager.vendors.values():
        sheet.append([vendor.vendor_name, vendor.vendor_id, vendor.contact_name, vendor.phone, vendor.email, vendor.address])
    
    workbook.save("vendors.xlsx")
    print("Data exported to vendors.xlsx")