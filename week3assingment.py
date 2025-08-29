def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# QUESTION 2 Get user input
try:
    original_price = float(input("Enter the original price of the item:"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Display results
    if discount_percent >= 20:
        print(f" {discount_percent}% discount applied!")
        print(f"Original price: ${original_price:.2f}")
        print(f"Discount amount: ${(original_price - final_price):.2f}")
        print(f"Final price: ${final_price:.2f}")
    else:
        print(f"Discount too low ({discount_percent}% < 20%) - no discount applied")
        print(f"Price: ${final_price:.2f}")
        
except ValueError:
    print(" Please enter valid numbers for price and discount percentage!")