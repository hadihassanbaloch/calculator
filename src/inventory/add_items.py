# add items from users list

import sys
from src.exceptions import CustomException
from src.logger import logger
import pandas as pd
import os
from dataclasses import dataclass
from datetime import datetime

class InventoryManager:
    def __init__(self):
        logger.info("Starting Inventory Manager..")
        try:
        # Path for the CSV file
            self.inventory_path = os.path.join("data", "inventory.csv")
            self.columns = ["ItemNo","DateTime", "Name", "Price", "Quantity"]

            # Check if the file exists; if not, create it with the required columns
            if not os.path.exists(self.inventory_path) or os.path.getsize(self.inventory_path) == 0:
                self._initialize_inventory()
        except Exception as e:
            raise CustomException(f'Error Creating the inventory: {str(e)}') 

    def _initialize_inventory(self):
        try:
            df = pd.DataFrame(columns=self.columns)  # Create empty DataFrame with defined columns
            df.to_csv(self.inventory_path, index=False)  # Save empty DataFrame to CSV
            print(f"Created new inventory file at {self.inventory_path} with columns: {self.columns}")
        except Exception as e:
            raise CustomException("Error creating inventory file", {str(e)})
        
    def add_category(self, category_name):
        """
        Adds a new column to the inventory if it doesn't already exist.
        """
        try:
            logger.info("Adding New Category")
            # Load the current inventory file
            df = pd.read_csv(self.inventory_path)

            # Check if the column already exists
            if category_name not in df.columns:
                df[category_name] = None  # Add a new column with NaN values
                df.to_csv(self.inventory_path, index=False)
                print(f"Added new category '{category_name}' to inventory.")
                logger.info(f"New category '{category_name}' added to inventory.")
            else:
                print(f"Category '{category_name}' already exists.")
                logger.info(f"Category '{category_name}' already exists in inventory.")
                
        except Exception as e:
            raise CustomException(f"Error adding new category: {str(e)}")

    def add_item(self, name, price, quantity, expirydate):
        """
        Adds a new item entry to the inventory CSV.
        """
        try:
            # Load the current inventory
            df = pd.read_csv(self.inventory_path)

            # Create a new item dictionary
            new_item = {
                "ItemNo": len(df) + 1,
                "DateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Price": price,
                "Quantity": quantity,
                "ExpiryDate": expirydate
            }

            # Append the new item to the DataFrame and save
            df = pd.concat([df, pd.DataFrame([new_item])], ignore_index=True)
            df.to_csv(self.inventory_path, index=False)
            print(f"Added new item '{name}' to inventory.")
            logger.info(f"New item '{name}' added to inventory.")
        except Exception as e:
            raise CustomException(f"Error adding new item: {str(e)}")
     

        
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    
    inventory_manager.add_item("potatium","2.21","91","12-09-2024")
