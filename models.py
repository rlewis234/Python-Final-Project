"""contains class definitions"""

class Product:
    def __init__(self, product_id, name, category, quantity, reorder_level, reorder_quantity, price, vendor_id, status):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity
        self.price = price
        self.vendor_id = vendor_id
        self.status = status
    
    def make_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "quantity": self.quantity,
            "reorder_level": self.reorder_level,
            "reorder_quantity": self.reorder_quantity,
            "price": self.price,
            "vendor_id": self.vendor_id,
            "status": self.status
        }

class Vendor:
    def __init__(self, vendor_id, name, contact_name, phone, email, address):
        self.vendor_id = vendor_id
        self.vendor_name = name
        self.contact_name = contact_name
        self.phone = phone
        self.email = email
        self.address = address
    
    def make_dict(self):
        return {
            "vendor_id": self.vendor_id,
            "name": self.vendor_name,
            "contact_name": self.contact_name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

class PurchaseOrder:
    def __init__(self, ponumber, vendor_id, date_created, ids_ordered, items_ordered, total_cost, status):
        self.ponumber = ponumber
        self.vendor_id = vendor_id
        self.date_created = date_created
        self.ids_order = ids_ordered
        self.items_ordered = items_ordered
        self.total_cost = total_cost
        self.status = status
    
    def make_dict(self):
        return {
            "ponumber": self.ponumber,
            "vendor_id": self.vendor_id,
            "date_created": self.date_created,
            "ids_ordered": self.ids_order,
            "items_ordered": self.items_ordered,
            "total_cost": self.total_cost,
            "status": self.status
        }