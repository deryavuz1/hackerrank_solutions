def bonAppetit(bill, k, b):
    
    notPay = bill[k]
    anna = sum(bill)
    totalAnna = (anna - notPay) / 2
    
    if b == int(totalAnna):
        print("Bon Appetit")
    else:
        print(int(b-totalAnna))
        
