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
    Product("P002", "Keyboard", "Electronics", 50, 10, 20, 25.0, "V001", "Active"),
    Product("P003", "Headset", "Audio", 0, 5, 25, 14.99, "V006", "Active"),
    Product("P004", "Webcam", "Electronics", 3, 5, 30, 9.99, "V001", "Active"),
    Product("P005", "Mouse", "Electronics", 0, 10, 30, 4.99, "V001", "Inactive"),
    Product("P006", "Monitor", "Electronics", 8, 2, 15, 180.0, "V001", "Active"),
    Product("P007", "Desk Chair", "Furniture", 20, 5, 10, 150.0, "V002", "Active"),
    Product("P008", "Bookshelf", "Furniture", 5, 2, 10, 120.0, "V002", "Active"),
    Product("P009", "Filing Cabinet", "Furniture", 8, 2, 10, 180.0, "V002", "Active"),
    Product("P010", "Office Desk", "Furniture", 10, 5, 5, 250.0, "V002", "Active"),
    Product("P011", "Desk Lamp", "Office Supplies", 40, 10, 60, 22.0, "V003", "Active"),
    Product("P012", "Stapler", "Office Supplies", 30, 10, 50, 8.0, "V003", "Active"),
    Product("P013", "Notebook", "Office Supplies", 100, 50, 200, 2.5, "V003", "Active"),
    Product("P014", "Pen Set", "Office Supplies", 200, 50, 500, 5.0, "V003", "Active"),
    Product("P015", "Printer Paper", "Office Supplies", 154, 50, 300, 3.0, "V003", "Active"),
    Product("P016", "Keyboard Wrist Rest", "Accessories", 20, 5, 30, 10.0, "V004", "Active"),
    Product("P017", "Mouse Pad", "Accessories", 50, 20, 100, 5.0, "V004", "Active"),
    Product("P018", "Cable Organizer", "Accessories", 25, 5, 40, 12.0, "V004", "Active"),
    Product("P019", "Headphone Stand", "Accessories", 15, 5, 20, 20.0, "V004", "Active"),
    Product("P020", "Soda", "Drinks/Snacks", 4, 5, 30, 3.99, "V005", "Active"),
    Product("P021", "Energy Drink", "Drinks/Snacks", 9, 5, 30, 4.99, "V005", "Active"),
    Product("P022", "Chips", "Drinks/Snacks", 7, 10, 45, 1.99, "V005", "Active"),
    Product("P023", "Bluetooth Speaker", "Audio", 25, 5, 50, 45.0, "V006", "Active"),
    Product("P024", "Headphones", "Audio", 10, 5, 15, 60.0, "V006", "Active"),
    Product("P025", "Microphone", "Audio", 10, 5, 15, 70.0, "V006", "Active"),

]

DEFAULT_VENDORS = [
    Vendor("V001", "General Electronics", "Even Electron", "217-664-9999", "generalelctronicssales@gmail.com", "4871 Eastpoint drive Fiction City"),
    Vendor("V002", "Ukea", "Billy Builder", "217-343-9806", "ukeacorpate@gmail.com", "3241 Wespoint Ave Fiction City"),
    Vendor("V003", "Paperclips", "Ollie Office", "363-875-6473", "paperclipssupply@gmail.com", "4675 Jackson St Fable City"),
    Vendor("V004", "Martianware", "Allie Accessory", "363-789-0231", "martianware@gmail.com", "3465 Batson Ave Fable City"),
    Vendor("V005", "Bepsi", "Sam Snackie", "217-123-9670", "bepsico@gmail.com", "4879 Eastpoint drive Fiction City"),
    Vendor("V006", "Gogitech", "Allen Smith", "665-657-7676", "gogitechsupport@gmail.com", "3451 Titan Ave Night City"),
]

DEFAULT_ORDERS = [
    PurchaseOrder("PO001", "V001", "05-10-2026", ["P001", "P002"], 20, 2000, "Ordered"),
    PurchaseOrder("PO002", "V001", "05-10-2026", ["P006"], 15, 180.0, "Ordered"),
    PurchaseOrder("PO003", "V004", "05-11-2026", ["P017", "P016", "P017", "P016"], 260, 30.0, "Ordered"),
    PurchaseOrder("PO004", "V005", "05-11-2026", ["P020", "P021", "P022"], 105, 10.97, "Ordered"),
    PurchaseOrder("PO005", "V006", "05-11-2026", ["P025"], 15, 70.0, "Ordered"),
    PurchaseOrder("PO006", "V002", "05-12-2026", ["P010", "P009"], 15, 430.0, "Ordered"),
    PurchaseOrder("PO007", "V003", "05-12-2026", ["P011"], 60, 22.0, "Ordered"),
    PurchaseOrder("PO008", "V002", "05-13-2026", ["P008", "P007"], 20, 270.0, "Ordered"),
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
            vendors = {vid: Vendor(**vendor_data) for vid, vendor_data in data.items()}
            print("Vendors loaded from file.")
    except FileNotFoundError:
        # First startup → use default vendors and save them
        vendors = {vend.vendor_id: vend for vend in DEFAULT_VENDORS}
        save_vendors()
        print("No vendor file found. Initialized with default vendors.")

def save_vendors():
    """Save all vendors to the JSON file."""
    with open(VENDORS_FILE, "w") as f:
        json.dump({vid: vend.make_dict() for vid, vend in vendors.items()}, f, indent=4)

# -------------------- Purchase Orders --------------------

def initialize_orders():
    """Load orders from file, or initialize with default orders if file doesn't exist or is invalid."""
    global orders
    try:
        with open(ORDERS_FILE, "r") as f:
            data = json.load(f)
            orders = {ponum: PurchaseOrder(**order_data) for ponum, order_data in data.items()}
            print("Purchase Orders loaded from file.")
    except (FileNotFoundError, json.JSONDecodeError):
        orders = {order.ponumber: order for order in DEFAULT_ORDERS}
        save_orders()
        print("No valid order file found. Initialized with default orders.")

def save_orders():
    """Save all orders to the JSON file."""
    with open(ORDERS_FILE, "w") as f:
        json.dump({ponum: order.make_dict() for ponum, order in orders.items()}, f, indent=4)