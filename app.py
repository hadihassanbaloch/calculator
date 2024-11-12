import streamlit as st
import pandas as pd
from src.inventory.add_items import InventoryManager

inventory_manager = InventoryManager()


df = pd.read_csv("data/inventory.csv")

st.title('Inventory Management')
st.dataframe(df, use_container_width=True)
tab1, tab2 = st.tabs(["Add Items", "Add New Category"])

with tab1:
    with st.expander("Add Item"):
            name = st.text_input('Item Name')
            price = st.number_input('Price', min_value=0.0)
            quantity = st.number_input('Quantity', min_value=0)
            expiry = st.date_input('Expiry')
            
            if st.button('Add Item'):
                if name and price > 0 and quantity > 0:
                    inventory_manager.add_item(name, price, quantity, expiry)
                    st.success(f'Item {name} added successfully!')
                else:
                    st.error("Please provide valid inputs.")
    
  
with tab2:  # Add Category Section
    with st.expander("Add Category"):
        category_name = st.text_input('Category Name')
            
        if st.button('Add Category'):
            if category_name:
                inventory_manager.add_category(category_name)
                st.success(f'Category {category_name} added successfully!')
            else:
                st.error("Please provide a category name.")
