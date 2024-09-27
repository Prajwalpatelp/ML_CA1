import unittest
from src.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.manager = InventoryManager()

    def test_add_item(self):
        self.manager.add_item(1, 'Laptop', 'Electronics', 10, 1000)
        self.assertEqual(len(self.manager.inventory), 1)

    def test_remove_item(self):
        self.manager.add_item(1, 'Laptop', 'Electronics', 10, 1000)
        self.manager.remove_item(1)
        self.assertEqual(len(self.manager.inventory), 0)

    def test_update_stock(self):
        self.manager.add_item(1, 'Laptop', 'Electronics', 10, 1000)
        self.manager.update_stock(1, 20)
        self.assertEqual(self.manager.inventory.loc[0, 'Stock_Quantity'], 20)

    def test_low_stock_report(self):
        self.manager.add_item(1, 'Laptop', 'Electronics', 5, 1000)
        self.manager.add_item(2, 'Phone', 'Electronics', 15, 500)
        low_stock = self.manager.generate_low_stock_report()
        self.assertEqual(len(low_stock), 1)

if __name__ == '__main__':
    unittest.main()
