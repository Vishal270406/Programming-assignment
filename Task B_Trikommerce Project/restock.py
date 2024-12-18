def restock_inventory(available_items, inventory_records, current_day):

    max_stock = 2000 # Max t-shirt stock of 2000

    if current_day == 0:
        inventory_records.append([current_day, 0, 2000, 2000])
    else:
    # restocks after every 7 days
        if current_day % 7 == 0:

            # Calculates the amount needed to reach the max stock
            restock_items = max_stock - available_items
            
            # Adds on the amount needed to restock to the current stock
            available_items = 2000
            
            # Logs the amount of t-shirts getting restocked and available t-shirts for each day
            inventory_records.append([current_day, 0, restock_items, available_items])
    
    

    
    return available_items


'''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''

    
