"""contains functions for saving and loading data"""
import json
from models import Product, Vendor, PurchaseOrder

PRODUCTS_FILE = "products.json"
products = {}

VENDORS_FILE = "vendors.json"
vendors = {}

ORDERS_FILE = "purchaseorders.json"
orders = {}

DEFAULT_PRODUCTS = [
    Product("P001", "Laptop", "Electronics", 15, 5, 10, 1200.0, "V001", "Active"),
    Product("P002", "Keyboard", "Electronics", 50, 10, 20, 25.0, "V002", "Active"),
    Product("P003", "Desk Chair", "Furniture", 20, 5, 10, 150.0, "V003", "Active"),
]

DEFAULT_VENDORS = [
    Vendor("V001", "General Electronics", "Even Electron", "217-664-9999", "generalelctronicssales@gmail.com", "4871 Eastpoint drive Fiction city"),
]

DEFAULT_ORDERS = [
    PurchaseOrder("PO001", "V001", "9/10/2026", ["P001", "P002"], 20, 2000, "Ordered")
]

# -------------------- Products --------------------

def initialize_products():
    """Load products from file, or initialize with default products if file doesn't exist."""
    global products
    try:
        with open(PRODUCTS_FILE, "r") as f:
            data = json.load(f)
            products = {pid: Product(**prod_data) for pid, prod_data in data.items()}
            print("Products loaded from file.")
    except FileNotFoundError:
        # First startup → use default products and save them
        products = {prod.product_id: prod for prod in DEFAULT_PRODUCTS}
        save_products()
        print("No product file found. Initialized with default products.")

def save_products():
    """Save all products to the JSON file."""
    with open(PRODUCTS_FILE, "w") as f:
        json.dump({pid: prod.make_dict() for pid, prod in products.items()}, f, indent=4)

# -------------------- Vendors --------------------

def initialize_vendors():
    """Load vendors from file, or initialize with default vendors if file doesn't exist."""
    global vendors
    try:
        with open(VENDORS_FILE, "r") as f:
            data = json.load(f)
            vendors = {pid: Vendor(**vendor_data) for pid, vendor_data in data.items()}
            print("Vendors loaded from file.")
    except FileNotFoundError:
        # First startup → use default vendors and save them
        vendors = {vend.vendor_id: vend for vend in DEFAULT_VENDORS}
        save_vendors()
        print("No vendor file found. Initialized with default vendors.")

def save_vendors():
    """Save all vendors to the JSON file."""
    with open(VENDORS_FILE, "w") as f:
        json.dump({pid: vend.make_dict() for pid, vend in vendors.items()}, f, indent=4)

# -------------------- Purchase Orders --------------------

def initialize_orders():
    """Load orders from file, or initialize with default orders if file doesn't exist or is invalid."""
    global orders
    try:
        with open(ORDERS_FILE, "r") as f:
            data = json.load(f)
            orders = {pid: PurchaseOrder(**order_data) for pid, order_data in data.items()}
            print("Purchase Orders loaded from file.")
    except (FileNotFoundError, json.JSONDecodeError):
        orders = {order.ponumber: order for order in DEFAULT_ORDERS}
        save_orders()
        print("No valid order file found. Initialized with default orders.")

def save_orders():
    """Save all orders to the JSON file."""
    with open(ORDERS_FILE, "w") as f:
        json.dump({pid: order.make_dict() for pid, order in orders.items()}, f, indent=4)