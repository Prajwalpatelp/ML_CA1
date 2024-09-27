import pandas as pd

class InventoryManager:
    def _init_(self, inventory_file):
        self.inventory_file = inventory_file
        self.inventory = pd.read_csv(inventory_file)

    def add_item(self, item_id, item_name, category, stock_quantity, price):
        new_item = {
            'Item_ID': item_id,
            'Item_Name': item_name,
            'Category': category,
            'Stock_Quantity': stock_quantity,
            'Price': price
        }
        self.inventory = self.inventory.append(new_item, ignore_index=True)
        self._save_inventory()

    def remove_item(self, item_id):
        self.inventory = self.inventory[self.inventory['Item_ID'] != item_id]
        self._save_inventory()

    def update_stock(self, item_id, stock_quantity):
        self.inventory.loc[self.inventory['Item_ID'] == item_id, 'Stock_Quantity'] = stock_quantity
        self._save_inventory()

    def generate_low_stock_report(self, threshold=10):
        return self.inventory[self.inventory['Stock_Quantity'] < threshold]

    def _save_inventory(self):
        self.inventory.to_csv(self.inventory_file, index=False)