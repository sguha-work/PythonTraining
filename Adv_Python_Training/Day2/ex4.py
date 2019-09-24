## bill calculation
print('==============================================================')
sgst = 2.5
cgst = 2.5
burgerPrice = 30
pizzaPrice = 100
soupPrice = 40
priceList = [burgerPrice, pizzaPrice, soupPrice]
displayString ="""
    Food Items
        1. Burger
        2. Pizza
        3. Soup
    Enter your choice of item:"""
print(displayString,end='')

userChoiceOfFood = int(input())-1

print ('    Enter quantity:',end='')
userChoosenQuantity = int(input())

basicFoodPrice = priceList[userChoiceOfFood]*userChoosenQuantity
calculatedCGST = (basicFoodPrice * 2.5)/100
calculatedSGST = (basicFoodPrice * 2.5)/100
actualFoodPrice = basicFoodPrice + calculatedCGST + calculatedSGST

displayString = f"""
    Food price:             {basicFoodPrice} rupees
    Total tax to be paid:   {calculatedCGST+calculatedSGST} rupees
    Total paybel ammount:   {actualFoodPrice} rupees
    Thank you visit again
"""
print(displayString)
print('==============================================================')