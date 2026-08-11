# This function calculates the total price
def calculate_total(price, quantity):
    """
    Calculate the total cost of items.

    Parameters:
        price: The price of one item.
        quantity: The number of items.

    Output:
        The total price.
    """
    
    # Multiply the price by the quantity
    total = price * quantity
    
    # Return the calculated total
    return total


# Call the function
total_price = calculate_total(50, 3)

# Display the result
print("Total price:", total_price)