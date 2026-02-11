

# Prices per kg (integers)
price_rice = 45
price_sugar = 40
price_oil = 130

# Quantities purchased (floats)
qty_rice = 3.0
qty_sugar = 2.5
qty_oil = 1.8

# Calculate total price for each item (float)
total_rice = price_rice * qty_rice
total_sugar = price_sugar * qty_sugar
total_oil = price_oil * qty_oil

# Print individual totals
print("Total price of Rice:", total_rice)
print("Total price of Sugar:", total_sugar)
print("Total price of Oil:", total_oil)

# Calculate final total bill (float)
final_total = total_rice + total_sugar + total_oil
print("Final Total (float):", final_total)

# Convert float to integer explicitly
final_total_int = int(final_total)
print("Final Total (integer):", final_total_int)

# Convert integer to string explicitly
final_total_str = str(final_total_int)
print("Final Total (string):", final_total_str)

# Generate random delivery charge between 5 and 10
import random
delivery_charge = random.randint(5, 10)
print("Delivery Charge:", delivery_charge)

# Final bill including delivery (float)
final_bill_with_delivery = final_total + float(delivery_charge)

print("Final Bill including Delivery:", final_bill_with_delivery)
