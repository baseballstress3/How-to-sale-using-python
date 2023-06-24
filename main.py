originalPrice = float(input("Original price before discount: "))
Determine the discount rate.
if originalPrice < 128 :
discount_Rate = 0.92
else :
discount_Rate = 0.84
# Compute & print the discount.
discounted_Price = discount_Rate * originalPrice
print("Discounted Price: %.2f" % discounted_Price)
