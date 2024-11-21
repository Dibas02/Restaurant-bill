def calc(subtotal_bill, tip_percentage):

    total = subtotal_bill*(1 + 0.01*tip_percentage)
    total = round(total, 2)
    print("Your total bill is", total) 

subtotal_bill = float(input("enter the amount of sub total bill: "))
tip_percentage = int(input("Enter the tip percentage: "))
calc(subtotal_bill, tip_percentage)