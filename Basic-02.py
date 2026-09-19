# --- Step 1: Dabbey (Variables) Banana ---
phone_model = "iPhone 15"    # String (Text)
price = 79999              # Integer (Number)
discount_percentage = 10.5  # Float (Decimal Number)
is_in_stock = True         # Boolean (True/False)

# --- Step 2: Dabbey Ke Andar Ki Values Print Karna ---
print("--- PRODUCT DETAILS ---")
print("Model Name:", phone_model)
print("Original Price:", price)
print("Discount Offer:", discount_percentage, "%")
print("Available in Shop?:", is_in_stock)

# --- Step 3: f-string Se Clean Message Print Karna ---
# Quotes ke pehle 'f' lagane se hum {} mein direct variable likh sakte hain
print(f"Special Offer: Buy {phone_model} at just Rs. {price} with {discount_percentage}% off!")