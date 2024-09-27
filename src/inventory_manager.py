import pandas as pd

class InventoryManager:
    def __init__(self):
        # Initialize an empty inventory with the given columns
        self.inventory = pd.DataFrame(columns=['Item_ID', 'Item_Name', 'Category', 'Stock_Quantity', 'Price'])

    def add_item(self, item_id, item_name, category, stock_quantity, price):
        """Add a new item to the inventory."""
        new_item = pd.DataFrame({
            'Item_ID': [item_id],
            'Item_Name': [item_name],
            'Category': [category],
            'Stock_Quantity': [stock_quantity],
            'Price': [price]
        })
        self.inventory = pd.concat([self.inventory, new_item], ignore_index=True)

    def remove_item(self, item_id):
        """Remove an item from the inventory by Item_ID."""
        self.inventory = self.inventory[self.inventory['Item_ID'] != item_id].reset_index(drop=True)

    def update_stock(self, item_id, new_quantity):
        """Update the stock quantity of an item."""
        self.inventory.loc[self.inventory['Item_ID'] == item_id, 'Stock_Quantity'] = new_quantity

    def generate_low_stock_report(self, threshold=10):
        """Generate a report for items with stock quantities below the threshold."""
        return self.inventory[self.inventory['Stock_Quantity'] < threshold]

