import datetime
date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print("\n========Grocery Store==========")

#customer Details

name = input("Enter customer name = ").title()
num = input("Enter customer contact number = ")

#Predifined items with price( ₹ per unit)

items={"rice":50,
       "oil":120,
       "takatak":5,
       "sugar":45,
       "salt":19,
       "dal":70,
       "tea":20,
       "soap":45,
       "milk":60}

bill = 0
purchased_items={}

while True:
    product=input("Enter product name (or 'total' to finish ): ").lower()

    if product=="total":
        break
    elif product in items:
        qty= int(input(f"Enter a Quantity of {product}: "))
        cost = items[product]*qty
        bill+=cost
        purchased_items[product]=purchased_items.get(product,0)+qty
    else:
        print("This item is not avilable ")

#Payment method 

payment_method = input("Enter Payment mode (Cash/UPI) = ")

# discount logic

discount = 0

if bill>=500:
    discount= bill*0.10 #for 10% discount
elif bill>=200:
    discount= bill*0.05 #for 5% discount

final_amount = bill - discount

# GST

gst = final_amount*0.05

final_amount+=gst

# Print bill

print(f"\n=========Final Bill==========")

print(f"Customer Name  : {name}\n")
print(f"Phone number   : {num} \n")
print(f"Date : {date}")
print("Items Purchased:")
for item,qty in purchased_items.items():
    print(f"{item.capitalize()} x {qty}       = ₹{items[item]*qty}")

print("\n-----------------------------")
print(f"Subtotal       : ₹{bill}")
print(f"Discount       : ₹{discount:.2f}")
print(f"GST (5%)       : ₹{gst:.2f}")
print(f"Total Payable  : ₹{final_amount:.2f}")
print(f"Payment Mode   : {payment_method.upper()}")
print("-----------------------------")

#Save bill to file

with open("bill.txt","w",encoding="utf-8") as f:
    f.write("=====================================\n")
    f.write("           Grocery Store Bill        \n")
    f.write("=====================================\n")

    f.write(f"Date : {date}\n\n")
    f.write(f"Name = Mr/mrs {name}\n")
    f.write(f"Phone number : {num} \n")

    for item ,qty in purchased_items.items():
        f.write(f"{item.capitalize()} x {qty}      = ₹{items[item]*qty}\n")
    
    f.write("\n-----------------------------")
    f.write(f"\nSubtotal      : ₹{bill}")
    f.write(f"\nDiscount      : ₹{discount:.2f}")
    f.write(f"\nGST (5%)      : ₹{gst:.2f}")
    f.write(f"\nTotal Payable : ₹{final_amount:.2f}\n")
    f.write(f"Payment Mode    : {payment_method.upper()}\n")
    f.write("-----------------------------\n")

print("\nBill saved as bill.txt")